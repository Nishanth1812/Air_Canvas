# Air Canvas Studio

Gesture-controlled drawing application using Python, OpenCV, and MediaPipe Hands.

## Structure

```
├── main.py               # Application entry point
├── drawing_engine.py     # Drawing operations
├── tool_palette.py       # Tool/color selection UI
├── gesture_controller.py # Hand landmark detection
└── visual_feedback.py    # Cursor and indicators
```

## Setup

Activate venv and install dependencies:

```bash
.\venv\Scripts\Activate          # Windows
pip install opencv-python mediapipe numpy
```

## Run

```bash
python main.py
```

**Controls:** `q` = quit, `c` = clear canvas

## Gestures (To Implement)

| Gesture | Action |
|---------|--------|
| Index finger up | Draw mode |
| Two fingers up | Select mode |
| Fist | Stop drawing |
| Open palm | Special action |

## Implementation Tasks

**drawing_engine.py**
- `draw_stroke()` - Continuous stroke drawing
- `draw_shape()` - Shape drawing
- `erase_stroke()` - Eraser
- `blend_canvas_with_frame()` - Canvas overlay

**gesture_controller.py**
- `detect_hand_landmarks()` - Landmark extraction
- `is_finger_up()` - Finger state detection
- `interpret_gesture()` - Gesture classification

**tool_palette.py**
- `PaletteButton.contains_point()` - Hit detection
- `render_palette()` - UI rendering
- `check_palette_selection()` - Selection logic

**visual_feedback.py**
- `draw_cursor()` - Cursor rendering
- `display_mode_indicator()` - Mode display
- `show_color_preview()` - Color preview