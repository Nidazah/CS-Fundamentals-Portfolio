import turtle as tu
import random as ra

# --- Setup Screen ---
screen = tu.Screen()
screen.title("Catch the Turtle Game 🐢")
screen.bgcolor("blue")
screen.setup(width=800, height=600)

# --- Create the Turtle ---
t = tu.Turtle()
t.shape("turtle")
t.color("red")
t.penup()
t.speed(0)  # Fastest movement

# --- Create Score Display ---
score = 0
timer = 20   # seconds
game_over = False

score_turtle = tu.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-360, 260)
score_turtle.write(f"Score: {score}", font=("Times New Roman", 16, "bold"))

timer_turtle = tu.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(250, 260)
timer_turtle.write(f"Time: {timer}", font=("Times New Roman", 16, "bold"))

# --- Define Functions ---
def move_turtle():
    """Move the turtle to a random position on the screen."""
    if not game_over:
        x = ra.randint(-300, 300)
        y = ra.randint(-250, 200)
        t.goto(x, y)
        screen.ontimer(move_turtle, 800)  # Move every 0.8 seconds

def update_score(x, y):
    """Increase score when turtle is clicked."""
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", font=("Times New Roman", 16, "bold"))

def countdown():
    """Countdown timer for the game."""
    global timer, game_over
    if timer > 0:
        timer -= 1
        timer_turtle.clear()
        timer_turtle.write(f"Time: {timer}", font=("Times New Roman", 16, "bold"))
        screen.ontimer(countdown, 1000)
    else:
        game_over = True
        t.hideturtle()
        score_turtle.goto(-70, 0)
        score_turtle.write("Game Over!", font=("Times New Roman", 24, "bold"))

# --- Event Binding ---
t.onclick(update_score)

# --- Start Game ---
move_turtle()
countdown()

# --- Keep the window open ---
screen.mainloop()
