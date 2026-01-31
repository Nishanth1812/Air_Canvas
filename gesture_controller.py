"""
Air Canvas Studio - Gesture Controller
Handles hand landmark detection and gesture interpretation.
"""

import numpy as np

# MediaPipe landmark indices
FINGERTIP_INDICES = {"thumb": 4, "index": 8, "middle": 12, "ring": 16, "pinky": 20}
FINGER_PIP_INDICES = {"thumb": 3, "index": 6, "middle": 10, "ring": 14, "pinky": 18}
FINGER_MCP_INDICES = {"thumb": 2, "index": 5, "middle": 9, "ring": 13, "pinky": 17}


def detect_hand_landmarks(hand_landmarks, frame_shape):
    """
    Extract hand landmarks as pixel coordinates.
    
    Parameters:
        hand_landmarks: MediaPipe hand landmarks
        frame_shape: Frame dimensions (height, width, channels)
    
    Returns:
        dict with keys: 'raw', 'fingertips', 'palm_center'
    """
    height, width, _ = frame_shape
    
    # Convert normalized coords to pixels
    raw_landmarks = []
    for landmark in hand_landmarks:
        pixel_x = int(landmark.x * width)
        pixel_y = int(landmark.y * height)
        raw_landmarks.append((pixel_x, pixel_y))
    
    # Extract fingertips
    fingertips = {}
    for finger_name, idx in FINGERTIP_INDICES.items():
        fingertips[finger_name] = raw_landmarks[idx]
    
    # Calculate palm center (average of wrist and middle finger base)
    wrist = raw_landmarks[0]
    middle_base = raw_landmarks[9]
    palm_center = ((wrist[0] + middle_base[0]) // 2, (wrist[1] + middle_base[1]) // 2)
    
    return {"raw": raw_landmarks, "fingertips": fingertips, "palm_center": palm_center}


def is_finger_up(landmarks, finger_name):
    """
    Check if a finger is extended.
    
    Parameters:
        landmarks: Landmarks dict from detect_hand_landmarks()
        finger_name: 'thumb', 'index', 'middle', 'ring', or 'pinky'
    
    Returns:
        True if finger is up, False if down
    """
    raw = landmarks["raw"]
    
    tip_idx = FINGERTIP_INDICES[finger_name]
    pip_idx = FINGER_PIP_INDICES[finger_name]
    
    tip = raw[tip_idx]
    pip = raw[pip_idx]
    
    # For thumb, check horizontal extension
    if finger_name == "thumb":
        return abs(tip[0] - pip[0]) > 30
    
    # For other fingers, check if tip is above PIP (Y increases downward)
    return tip[1] < pip[1] - 10


def get_extended_fingers(landmarks):
    """
    Get list of extended finger names.
    
    TODO: Check each finger with is_finger_up() and collect names
    """
    extended = []
    for finger in ["thumb", "index", "middle", "ring", "pinky"]:
        if is_finger_up(landmarks, finger):
            extended.append(finger)
    return extended


def interpret_gesture(landmarks):
    """
    Interpret hand pose as gesture command.
    
    Parameters:
        landmarks: Landmarks dict
    
    Returns:
        Gesture string: 'draw', 'select', 'erase', 'stop', 'palm', or None
    """
    if landmarks is None:
        return None
    
    extended = get_extended_fingers(landmarks)
    num_extended = len(extended)
    
    # Map finger combinations to gestures
    if num_extended == 0:
        return 'stop'
    elif num_extended == 5:
        return 'palm'
    elif num_extended == 1 and 'index' in extended:
        return 'draw'
    elif num_extended == 2 and 'index' in extended and 'middle' in extended:
        return 'select'
    
    return None


def get_index_finger_position(landmarks):
    """Get index fingertip position (x, y) or None."""
    if landmarks is None or "fingertips" not in landmarks:
        return None
    return landmarks["fingertips"].get("index")


def detect_pinch_gesture(landmarks, threshold=40):
    """
    Detect thumb-index pinch gesture.
    
    Returns:
        (is_pinching, pinch_midpoint) tuple
    """
    if landmarks is None or "fingertips" not in landmarks:
        return (False, None)
    
    thumb_tip = landmarks["fingertips"]["thumb"]
    index_tip = landmarks["fingertips"]["index"]
    
    # Calculate distance
    distance = np.sqrt((thumb_tip[0] - index_tip[0])**2 + (thumb_tip[1] - index_tip[1])**2)
    
    is_pinching = distance < threshold
    midpoint = ((thumb_tip[0] + index_tip[0]) // 2, (thumb_tip[1] + index_tip[1]) // 2) if is_pinching else None
    
    return (is_pinching, midpoint)
