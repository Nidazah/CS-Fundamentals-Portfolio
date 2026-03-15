import turtle
import datetime
import time
import random

# ---------------- Screen Setup ----------------
screen = turtle.Screen()
screen.title("🎆 New Year Countdown App 🎆")
screen.bgcolor("black")
screen.setup(900, 600)
screen.tracer(0)

# ---------------- Text Turtle ----------------
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()

# ---------------- Firework Turtle ----------------
fire = turtle.Turtle()
fire.hideturtle()
fire.speed(0)
fire.width(2)

# ---------------- User Input ----------------
name = screen.textinput("New Year App", "Enter your name:")

if not name:
    name = "Friend"

# ---------------- Firework Function ----------------
def firework(x, y):
    fire.penup()
    fire.goto(x, y)
    fire.pendown()

    colors = ["red", "yellow", "cyan", "orange", "magenta", "lime"]

    for _ in range(36):
        fire.color(random.choice(colors))
        fire.forward(80)
        fire.backward(80)
        fire.right(10)

# ---------------- Fireworks Show ----------------
def fireworks_show():
    for _ in range(20):
        x = random.randint(-400, 400)
        y = random.randint(-250, 250)
        firework(x, y)
        screen.update()
        time.sleep(0.15)

# ---------------- Countdown Function ----------------
def new_year_countdown():
    while True:
        now = datetime.datetime.now()
        new_year = datetime.datetime(now.year + 1, 1, 1)
        remaining = new_year - now

        if remaining.total_seconds() <= 0:
            break

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        text.clear()
        text.goto(0, 50)
        text.write(
            f"{days} Days {hours} Hours {minutes} Minutes {seconds} Seconds",
            align="center",
            font=("Arial", 24, "bold")
        )

        text.goto(0, -30)
        text.write(
            "⏳ Countdown to New Year ⏳",
            align="center",
            font=("Arial", 18, "normal")
        )

        screen.update()
        time.sleep(1)

# ---------------- Main Program ----------------
new_year_countdown()

text.clear()
text.goto(0, 150)
text.color("gold")
text.write(
    f"🎉 HAPPY NEW YEAR 🎉",
    align="center",
    font=("Arial", 40, "bold")
)

text.goto(0, 90)
text.write(
    f"{name} ✨",
    align="center",
    font=("Arial", 30, "bold")
)

fireworks_show()

screen.mainloop()
