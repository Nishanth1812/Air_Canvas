"""
Air Canvas Studio - Main Application
Gesture-controlled drawing using OpenCV and MediaPipe Hands.

Run with venv activated: python main.py
Controls: 'q' to quit, 'c' to clear canvas
"""

import cv2
import numpy as np
import mediapipe as mp

from drawing_engine import draw_stroke, clear_canvas, initialize_canvas
from tool_palette import render_palette, check_palette_selection
from gesture_controller import detect_hand_landmarks, interpret_gesture
from visual_feedback import draw_cursor, display_mode_indicator, show_color_preview

# Configuration
WINDOW_NAME = "Air Canvas Studio"
CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
DEFAULT_COLOR = (255, 0, 0)
DEFAULT_THICKNESS = 5


class ApplicationState:
    """Maintains shared application state."""
    
    def __init__(self):
        self.canvas = initialize_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.current_color = DEFAULT_COLOR
        self.current_thickness = DEFAULT_THICKNESS
        self.current_mode = "draw"
        self.previous_point = None
        self.is_drawing = False


def initialize_mediapipe():
    """Initialize MediaPipe Hands detector."""
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    )
    mp_drawing = mp.solutions.drawing_utils
    return mp_hands, hands, mp_drawing


def initialize_webcam(camera_index=0):
    """Initialize webcam capture."""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CANVAS_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CANVAS_HEIGHT)
    return cap


def process_frame(frame, hands, mp_hands, state):
    """Process frame for hand detection and gesture recognition."""
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    landmarks = None
    gesture = None
    
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        landmarks = detect_hand_landmarks(hand_landmarks, frame.shape)
        gesture = interpret_gesture(landmarks, mp_hands)
        
        # TODO: Add gesture handling logic here
        # - Connect gestures to drawing actions
        # - Update state.previous_point for continuous strokes
    
    return frame, landmarks, gesture


def render_output(frame, state, landmarks, gesture):
    """Render final output combining video feed, canvas, and UI."""
    output = frame.copy()
    
    output = render_palette(output, state.current_color, state.current_mode)
    
    if landmarks is not None:
        output = draw_cursor(output, landmarks, state.current_mode)
        output = show_color_preview(output, landmarks, state.current_color)
    
    output = display_mode_indicator(output, state.current_mode)
    
    # TODO: Implement canvas overlay blending with cv2.addWeighted()
    
    return output


def main():
    """Main application entry point."""
    print("Air Canvas Studio - Starting...")
    
    mp_hands, hands, mp_drawing = initialize_mediapipe()
    cap = initialize_webcam()
    state = ApplicationState()
    
    print("Running. Press 'q' to quit, 'c' to clear.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        
        processed_frame, landmarks, gesture = process_frame(frame, hands, mp_hands, state)
        output = render_output(processed_frame, state, landmarks, gesture)
        
        cv2.imshow(WINDOW_NAME, output)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            state.canvas = clear_canvas(state.canvas)
    
    cap.release()
    cv2.destroyAllWindows()
    hands.close()


if __name__ == "__main__":
    main()
