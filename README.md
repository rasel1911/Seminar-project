# Simple Home Design with Python Turtle Graphics

## Overview
This project creates a simple 2D house illustration using Python's `turtle` graphics library. The program draws a complete house with walls, a roof, a door, windows, and a chimney on a light blue background.

## Features
- **House Walls**: A rectangular beige/wheat-colored structure serving as the main body of the house
- **Roof**: A dark red triangular roof drawn on top of the walls
- **Door**: A brown door with a gold handle positioned on the front wall
- **Windows**: Two light cyan windows with blue borders and visible panes on either side of the door
- **Chimney**: A dark red rectangular chimney extending from the roof

## Technical Details

### Dependencies
- **Python 3.x**
- **turtle** module (built-in with Python)

### Screen Configuration
- **Canvas Size**: 800 x 600 pixels
- **Background Color**: Light blue
- **Pen Speed**: 5 (animation speed)

### Key Functions

#### `draw_rectangle(width, height, color)`
Draws a filled rectangle with specified dimensions and color.
- Parameters:
  - `width`: Horizontal dimension of the rectangle
  - `height`: Vertical dimension of the rectangle
  - `color`: Fill color of the rectangle

#### `draw_triangle(size, color)`
Draws a filled equilateral triangle with specified size and color.
- Parameters:
  - `size`: Length of each side of the triangle
  - `color`: Fill color of the triangle

#### `draw_square(size, color)`
Draws a filled square with specified size and color.
- Parameters:
  - `size`: Length of each side of the square
  - `color`: Fill color of the square

## How It Works

1. **Screen Setup**: Initializes a turtle graphics window with dimensions and background color
2. **Component Drawing**: Uses the helper functions to draw each house component in sequence:
   - Main house body positioned at coordinates (-100, -100)
   - Roof positioned at (-100, 50)
   - Door in the center-front of the house
   - Door handle as a small circle
   - Left and right windows with decorative panes
   - Chimney on the upper right portion of the roof

3. **Pen Control**: Uses `penup()` and `pendown()` to move without drawing, and specific pen colors for each component for visual distinction

## Colors Used
- `lightblue`: Background
- `wheat`: House walls
- `darkred`: Roof and chimney
- `brown`: Pen color for walls
- `saddlebrown`: Door
- `gold`: Door handle
- `lightcyan`: Window fill
- `blue`: Window border and panes

## Usage

### Running the Program
```bash
python box_design.py
```

### What to Expect
A window will open displaying a simple 2D house drawing. The house is drawn from bottom to top and left to right, with the turtle animation visible during the drawing process.

## Customization Ideas
- Modify color values to change the house appearance
- Adjust `pen.goto()` coordinates to reposition components
- Change rectangle/triangle/square sizes for different proportions
- Add more features like a garage, garden, or clouds
- Add animation by modifying the pen speed or adding delays

## Notes
- The turtle is hidden after drawing is complete using `pen.hideturtle()`
- `turtle.done()` keeps the window open until manually closed by the user
- The program uses relative coordinates and forward/turn commands for shape drawing
