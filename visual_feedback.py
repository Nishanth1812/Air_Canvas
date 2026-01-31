"""
Air Canvas Studio - Visual Feedback
Handles cursor, mode indicators, and visual cues.
"""

import cv2
import numpy as np

# Visual settings
CURSOR_RADIUS = 10
CURSOR_THICKNESS = 2
MODE_COLORS = {
    "draw": (0, 255, 0),
    "select": (255, 255, 0),
    "erase": (0, 0, 255),
    "idle": (128, 128, 128)
}
FONT = cv2.FONT_HERSHEY_SIMPLEX


def draw_cursor(frame, landmarks, current_mode):
    """
    Draw cursor at fingertip position.
    
    Parameters:
        frame: Video frame
        landmarks: Landmarks dict with fingertip positions
        current_mode: Current mode string
    
    Returns:
        Frame with cursor drawn
    
    TODO: Get index fingertip from landmarks and draw circle
        - Use MODE_COLORS for cursor color
        - Different cursor styles for different modes
    """
    # YOUR CODE HERE
    pass
    return frame


def display_mode_indicator(frame, current_mode):
    """
    Display current mode text on screen.
    
    Parameters:
        frame: Video frame
        current_mode: Current mode string
    
    Returns:
        Frame with mode indicator
    
    TODO: Draw mode text at bottom-left corner
        - Add background rectangle for readability
        - Use cv2.putText()
    """
    # YOUR CODE HERE
    pass
    return frame


def show_color_preview(frame, landmarks, current_color, size=30):
    """
    Show color preview square near cursor.
    
    Parameters:
        frame: Video frame
        landmarks: Landmarks dict
        current_color: Current color (BGR)
        size: Preview square size in pixels
    
    TODO: Draw filled rectangle near fingertip showing current color
    """
    # YOUR CODE HERE
    pass
    return frame


def draw_fingertip_trail(frame, trail_points, color, max_points=20):
    """
    Draw fading trail behind fingertip.
    
    TODO: Draw circles at trail points with decreasing size/opacity
    """
    # YOUR CODE HERE
    pass
    return frame


def show_status_message(frame, message, position="top"):
    """
    Display temporary status message.
    
    TODO: Draw centered text message at specified position
    """
    # YOUR CODE HERE
    pass
    return frame
