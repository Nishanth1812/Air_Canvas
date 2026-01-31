"""
Air Canvas Studio - Drawing Engine
Handles drawing operations on the canvas.
"""

import cv2
import numpy as np


def initialize_canvas(width, height, background_color=(255, 255, 255)):
    """
    Create a blank drawing canvas.
    
    Parameters:
        width, height: Canvas dimensions in pixels
        background_color: BGR color tuple (default white)
    
    Returns:
        numpy.ndarray: Blank canvas array
    """
    return np.full((height, width, 3), background_color, dtype=np.uint8)


def clear_canvas(canvas, background_color=(255, 255, 255)):
    """Reset canvas to background color."""
    canvas[:] = background_color
    return canvas


def draw_stroke(canvas, current_point, previous_point, color, thickness):
    """
    Draw a continuous stroke segment on the canvas.
    
    Parameters:
        canvas: Canvas array to draw on
        current_point: Current fingertip (x, y)
        previous_point: Previous fingertip (x, y) or None for stroke start
        color: BGR color tuple
        thickness: Stroke thickness in pixels
    
    Returns:
        Modified canvas
    
    TODO: Implement stroke drawing
        - If previous_point is None, draw a dot at current_point
        - Otherwise, draw a line from previous_point to current_point
        - Use cv2.line() with cv2.LINE_AA for smooth lines
    """
    # YOUR CODE HERE
    pass
    return canvas


def draw_shape(canvas, shape_type, start_point, end_point, color, thickness):
    """
    Draw a geometric shape on the canvas.
    
    Parameters:
        canvas: Canvas array
        shape_type: 'rectangle', 'circle', or 'line'
        start_point, end_point: Shape boundary points (x, y)
        color: BGR color tuple
        thickness: Outline thickness (-1 for filled)
    
    TODO: Implement shape drawing using cv2 drawing functions
    """
    # YOUR CODE HERE
    pass
    return canvas


def erase_stroke(canvas, center_point, eraser_size, background_color=(255, 255, 255)):
    """
    Erase portion of canvas at specified location.
    
    Parameters:
        canvas: Canvas array
        center_point: Eraser center (x, y)
        eraser_size: Eraser radius in pixels
        background_color: Color to erase with
    
    TODO: Draw filled circle of background_color at center_point
    """
    # YOUR CODE HERE
    pass
    return canvas


def blend_canvas_with_frame(frame, canvas, alpha=0.5):
    """
    Blend drawing canvas with video frame.
    
    Parameters:
        frame: Video frame from webcam
        canvas: Drawing canvas with strokes
        alpha: Blend factor (0.0=frame only, 1.0=canvas only)
    
    Returns:
        Blended output frame
    
    TODO: Implement blending using cv2.addWeighted() or mask-based blending
    """
    # YOUR CODE HERE
    pass
    return frame
