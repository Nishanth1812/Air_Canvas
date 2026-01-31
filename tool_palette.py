"""
Air Canvas Studio - Tool Palette
Handles tool and color selection UI.
"""

import cv2
import numpy as np

# Color options (BGR format)
COLOR_OPTIONS = [
    ("Red", (0, 0, 255)),
    ("Green", (0, 255, 0)),
    ("Blue", (255, 0, 0)),
    ("Yellow", (0, 255, 255)),
    ("Cyan", (255, 255, 0)),
    ("Magenta", (255, 0, 255)),
    ("White", (255, 255, 255)),
    ("Black", (0, 0, 0)),
]

# Layout settings
PALETTE_START_X = 10
PALETTE_START_Y = 10
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 60
BUTTON_SPACING = 10


class PaletteButton:
    """Represents a clickable palette button."""
    
    def __init__(self, x, y, width, height, color, label, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.label = label
        self.action = action
        self.is_hovered = False
    
    def contains_point(self, point):
        """
        Check if point is within button bounds.
        
        TODO: Return True if point (x, y) is inside the button rectangle
        """
        # YOUR CODE HERE
        pass
        return False


def create_color_buttons():
    """
    Create color selection buttons.
    
    Returns:
        List of PaletteButton objects
    
    TODO: Create buttons for each COLOR_OPTIONS entry
        - Position buttons horizontally with BUTTON_SPACING
        - Set action to ("color", color_value)
    """
    # YOUR CODE HERE
    pass
    return []


def render_palette(frame, current_color, current_mode):
    """
    Render tool palette on the frame.
    
    Parameters:
        frame: Video frame to draw on
        current_color: Currently selected color (BGR)
        current_mode: Current tool mode string
    
    Returns:
        Frame with palette rendered
    
    TODO: Draw color buttons and highlight selected color
        - Use cv2.rectangle() for buttons
        - Add border for selected button
    """
    # YOUR CODE HERE
    pass
    return frame


def check_palette_selection(finger_position, buttons):
    """
    Check if finger is hovering over any palette button.
    
    Parameters:
        finger_position: Fingertip (x, y)
        buttons: List of PaletteButton objects
    
    Returns:
        (button_index, button.action) if hovering, else None
    
    TODO: Check each button and return first match
    """
    # YOUR CODE HERE
    pass
    return None


def is_in_palette_region(point, palette_height=150):
    """Check if point is within the palette area at top of screen."""
    # YOUR CODE HERE
    pass
    return False
