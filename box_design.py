import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Simple Home Design")
screen.bgcolor("lightblue")

# Create turtle object
pen = turtle.Turtle()
pen.speed(5)

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Function to draw a triangle
def draw_triangle(size, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

# Function to draw a square
def draw_square(size, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

# Draw the main house body (walls)
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.pensize(3)
pen.pencolor("brown")
draw_rectangle(200, 150, "wheat")

# Draw the roof (triangle)
pen.penup()
pen.goto(-100, 50)
pen.pendown()
pen.pencolor("darkred")
draw_triangle(200, "darkred")

# Draw the door
pen.penup()
pen.goto(-25, -100)
pen.pendown()
pen.pencolor("brown")
draw_rectangle(50, 80, "saddlebrown")

# Draw door handle
pen.penup()
pen.goto(15, -60)
pen.pendown()
pen.pencolor("gold")
pen.dot(8)

# Draw left window
pen.penup()
pen.goto(-80, -20)
pen.pendown()
pen.pencolor("blue")
draw_square(40, "lightcyan")

# Draw window panes
pen.penup()
pen.goto(-60, -20)
pen.pendown()
pen.pencolor("blue")
pen.forward(0)
pen.goto(-60, 20)

pen.penup()
pen.goto(-80, 0)
pen.pendown()
pen.goto(-40, 0)

# Draw right window
pen.penup()
pen.goto(40, -20)
pen.pendown()
pen.pencolor("blue")
draw_square(40, "lightcyan")

# Draw window panes
pen.penup()
pen.goto(60, -20)
pen.pendown()
pen.pencolor("blue")
pen.forward(0)
pen.goto(60, 20)

pen.penup()
pen.goto(40, 0)
pen.pendown()
pen.goto(80, 0)

# Draw chimney
pen.penup()
pen.goto(70, 50)
pen.pendown()
pen.pencolor("darkred")
draw_rectangle(20, 60, "darkred")

# Hide the turtle and display
pen.hideturtle()
turtle.done()
