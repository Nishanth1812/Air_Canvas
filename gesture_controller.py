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
    
    TODO: Convert normalized coords to pixels
        - pixel_x = int(normalized_x * width)
        - pixel_y = int(normalized_y * height)
        - Extract fingertips using FINGERTIP_INDICES
    """
    # YOUR CODE HERE
    pass
    return {"raw": [], "fingertips": {}, "palm_center": None}


def is_finger_up(landmarks, finger_name):
    """
    Check if a finger is extended.
    
    Parameters:
        landmarks: Landmarks dict from detect_hand_landmarks()
        finger_name: 'thumb', 'index', 'middle', 'ring', or 'pinky'
    
    Returns:
        True if finger is up, False if down
    
    TODO: Compare fingertip.y with PIP.y (tip above joint = finger up)
        - Note: Y increases downward in image coordinates
        - Thumb uses X comparison (extends sideways)
    """
    # YOUR CODE HERE
    pass
    return False


def get_extended_fingers(landmarks):
    """
    Get list of extended finger names.
    
    TODO: Check each finger with is_finger_up() and collect names
    """
    # YOUR CODE HERE
    pass
    return []


def interpret_gesture(landmarks, mp_hands):
    """
    Interpret hand pose as gesture command.
    
    Parameters:
        landmarks: Landmarks dict
        mp_hands: MediaPipe Hands module
    
    Returns:
        Gesture string: 'draw', 'select', 'erase', 'stop', 'palm', or None
    
    TODO: Map finger combinations to gestures
        - Index only -> 'draw'
        - Index + Middle -> 'select'
        - No fingers -> 'stop'
        - All fingers -> 'palm'
    """
    # YOUR CODE HERE
    pass
    return None


def get_index_finger_position(landmarks):
    """Get index fingertip position (x, y) or None."""
    # YOUR CODE HERE
    pass
    return None


def detect_pinch_gesture(landmarks, threshold=40):
    """
    Detect thumb-index pinch gesture.
    
    Returns:
        (is_pinching, pinch_midpoint) tuple
    
    TODO: Calculate distance between thumb and index tips
    """
    # YOUR CODE HERE
    pass
    return (False, None)
