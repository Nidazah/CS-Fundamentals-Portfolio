# --- Libraries ---
import turtle as tu
import random as ra
import winsound as w
import time
from playsound import playsound as ps

# --- Setup Screen ---
screen = tu.Screen()
screen.title("Catch Gojo Satoru Game 🎮")
screen.bgcolor("black")
screen.setup(width=800, height=580)

# --- Register Image --- 
screen.register_shape("GOJO_CUP.gif")

# --- Create Sprite ---
t = tu.Turtle()
t.shape("GOJO_CUP.gif")
t.penup()
t.speed(0)
t.hideturtle()

# --- Variables ---
score = 0
timer = 20
game_over = False

# --- Score Display Turtle ---
score_turtle = tu.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.color("#7DF9FF")

# --- Timer Display Turtle ---
timer_turtle = tu.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.color("#7DF9FF")

# --- Beep Sound ---
def beep_sound():
    w.Beep(1000, 100)
    time.sleep(0.8)

# --- Intro Turtle ---
intro = tu.Turtle()
intro.hideturtle()
intro.color("#7DF9FF")
intro.penup()

# --- STARTING SECTION ---
def starting_section():
    intro.clear()
    intro.goto(0, 50)
    intro.write("✨ Welcome to Catch Gojo Satoru ✨",
                align="center",
                font=("Times New Roman", 22, "bold"))
    # Play intro MP3
    ps("game-start-6104.mp3")  
    time.sleep(2)
    intro.clear()

# --- Title and How to Play ---
    intro.goto(0, 80)
    intro.write("🎮 Catch Gojo Satoru 🎮",
                align="center",
                font=("Times New Roman", 20, "bold"))
    beep_sound()

    intro.goto(0, 40)
    intro.write("HOW TO PLAY:",
                align="center",
                font=("Times New Roman", 18, "bold"))
    beep_sound()

    intro.goto(-150, 5)
    intro.write("\t• Click on Gojo to score points",
                align="left",
                font=("Times New Roman", 16, "bold"))
    beep_sound()

    intro.goto(-150, -25)
    intro.write("\t• Gojo moves randomly",
                align="left",
                font=("Times New Roman",16, "bold"))
    beep_sound()

    intro.goto(-150, -55)
    intro.write("\t• You have 20 seconds",
                align="left",
                font=("Times New Roman",16, "bold"))
    beep_sound()

    intro.goto(0, -90)
    intro.write("🖱 Click anywhere to START!",
                align="center",
                font=("Times New Roman", 18, "bold"))
    beep_sound()

starting_section()

# --- Game Functions ---
def start_game(x, y):
    global score, timer, game_over

    intro.clear()          # remove instructions
    screen.onclick(None)   # prevent multiple starts

    score = 0
    timer = 20
    game_over = False

    t.showturtle()         # show Gojo
    # Show Score and Timer during gameplay
    score_turtle.goto(-360, 260)
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", 
                       font=("Times New Roman", 16,"bold"))

    timer_turtle.goto(250, 260)
    timer_turtle.clear()
    timer_turtle.write(f"Time: {timer}", 
                       font=("Times New Roman", 16, "bold"))

    move_turtle()
    countdown()

def move_turtle():
    if not game_over:
        t.goto(ra.randint(-300, 300), ra.randint(-250, 200))
        screen.ontimer(move_turtle, ra.randint(200, 800))

def update_score(x, y):
    global score
    if not game_over:
        score += 1
        ps("ouch-sound-effect-30-11844.mp3")
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", 
                           font=("Times New Roman", 16, "bold"))

def countdown():
    global timer, game_over
    if timer > 0:
        timer -= 1
        timer_turtle.clear()
        timer_turtle.write(f"Time: {timer}", 
                           font=("Times New Roman", 16, "bold"))
        
        # --- WARNING SOUND  ---
        if timer == 5:
            w.Beep(1500, 500) 

        screen.ontimer(countdown, 1000)
    else:
        game_over = True
        t.hideturtle()

        # --- Clear Score and Timer titles ---
        score_turtle.clear()
        timer_turtle.clear()

        # --- Display final score in the CENTER ---
        score_turtle.goto(0, 20)
        score_turtle.write("Game Over!", 
                           align="center",
                           font=("Times New Roman",24,"bold"))

        score_turtle.goto(0, -20)
        score_turtle.write(f"Your Score: {score}",
                           align="center",
                           font=("Times New Roman",24,"bold"))

        # Play the game over sound
        ps("game-over-31-179699.mp3")  

# --- Event Binding ---
screen.onclick(start_game)
t.onclick(update_score)

screen.mainloop()