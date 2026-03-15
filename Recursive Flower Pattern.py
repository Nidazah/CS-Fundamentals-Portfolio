import turtle
import colorsys

# --- SETTINGS ---
PETALS = 12         # number of petals around the flower
DEPTH = 6           # recursion depth
LENGTH = 25         # main petal length
ANGLE = 45          # recursive branching angle

# Setup screen
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

# Convert recursion depth into gradient color
def gradient(step):
    hue = step / DEPTH
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

# Recursive petal function
def petal(length, depth):
    if depth == 0:
        return
    
    t.color(gradient(depth))
    t.circle(length, 60)

    # branch 1
    t.left(ANGLE)
    petal(length * 0.75, depth - 1)

    # branch 2
    t.right(2 * ANGLE)
    petal(length * 0.75, depth - 1)

    t.left(ANGLE)
    t.circle(-length, 60)

# --- DRAW FULL FLOWER ---
for i in range(PETALS):
    petal(LENGTH, DEPTH)
    t.right(360 / PETALS)   # rotate around center for full flower symmetry

turtle.done()
