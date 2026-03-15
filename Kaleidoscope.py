import turtle
import random
import math

# ----------------------------
# Setup screen and turtle
# ----------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.colormode(255)

# ----------------------------
# Parameters
# ----------------------------
num_reflections = 8
tree_depth = 5
angle = 25
particle_count = 50
particles = []

# ----------------------------
# Particle class
# ----------------------------
class Particle:
    def __init__(self):
        self.x = random.randint(-400, 400)
        self.y = random.randint(-300, 300)
        self.size = random.randint(2, 5)
        self.color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.dot(self.size, self.color)
    
    def fall(self):
        self.y -= random.uniform(0.5, 2)
        if self.y < -300:
            self.y = 300
            self.x = random.randint(-400, 400)

# Initialize particles
for _ in range(particle_count):
    particles.append(Particle())

# ----------------------------
# Recursive fractal tree
# ----------------------------
def fractal_tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.left(angle)
        fractal_tree(branch_len - 15)
        t.right(2 * angle)
        fractal_tree(branch_len - 15)
        t.left(angle)
        t.backward(branch_len)

# ----------------------------
# Kaleidoscope reflection
# ----------------------------
def draw_kaleidoscope_tree():
    for i in range(num_reflections):
        t.penup()
        t.goto(0, -200)
        t.setheading(i * (360 / num_reflections))
        t.pendown()
        t.color(random.randint(50,255), random.randint(50,255), random.randint(50,255))
        fractal_tree(100)

# ----------------------------
# Main loop
# ----------------------------
def animate():
    t.clear()
    draw_kaleidoscope_tree()
    
    # Draw particles
    for p in particles:
        p.draw()
        p.fall()
    
    screen.ontimer(animate, 100)

animate()
screen.mainloop()
