import turtle
t = turtle.Turtle()
t.screen.bgcolor("white")#Background
t.pensize(2)
t.color("red")#Root
t.left(90)

t.backward(100)
t.speed(200)
t.shape("turtle")

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color("blue")#Branch
        t.circle(2)
        t.color("orange")#Leaf
        t.left(30)
        tree(3*i/4)#Left Branch
        t.right(60)
        tree(3*i/4)#Right Branch
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()
