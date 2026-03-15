import turtle as t

# --- Setup the screen ---
screen = t.Screen()
screen.bgcolor("black")
screen.title("Turtle Graphics Project")

# --- Setup the turtle ---
t.color("white")
t.pensize(1.5)

# --- Draw head ---
def head():
    t.circle(25)  # Head

# --- Draw body ---
def body():
    t.right(90)
    t.forward(25)

# --- Draw arms ---
def arms():
    t.right(45)
    t.forward(50)   # Right arm
    t.backward(50)  # Back to body

    t.left(90)
    t.forward(50)   # Left arm
    t.backward(50)  # Back to body

# --- Draw legs ---
def legs():
    t.right(45)     # Facing downward again

    t.forward(50)  # Move down to leg start
    t.left(45)
    t.forward(50)   # Left leg
    t.backward(50)

    t.right(90)
    t.forward(50)   # Right leg
    t.backward(50)

# --- Execute drawing functions ---
head()
body()
arms()
legs()

# --- Finish up ---
t.hideturtle()
screen.mainloop()

