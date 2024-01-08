import turtle
from random import randint
import time

screen = turtle.Screen()
screen.title('Catch The Turtle')
screen.setup(1000, 1000)
screen.bgcolor('light blue')

ask_seconds = int(turtle.textinput('Welcome', "How many seconds game ?"))

timer_text = turtle.Turtle()
timer_text.hideturtle()

ibi_score = turtle.Turtle()
ibi_score.hideturtle()
ibi_score.penup()
ibi_score.setpos(-20, 390)

ibi = turtle.Turtle('turtle')
ibi.color('green')
ibi.speed('fast')
ibi.shapesize(1)
ibi.turtlesize(stretch_len=2.5, stretch_wid=2.5)

start = time.time()
timer_text.penup()
timer_text.setpos(-20, 450)
timer_text.pendown()

score = 0


def turtle_onclick(a, b):
    global score
    score += 1
    print(a, b)


while time.time() - start < ask_seconds + 1:
    timer_text.clear()
    timer_text.write(f"Time:{int(time.time() - start)}", font=('Verdana', 20, 'bold'))

    ibi.penup()
    ibi.hideturtle()
    ibi.goto(randint(-400, 400), randint(-400, 400))
    ibi.pendown()
    ibi.showturtle()
    time.sleep(0.5)

    ibi.onclick(turtle_onclick)

    print(score)

    ibi_score.clear()
    ibi_score.write(f"Score: {score}", font=('Italic', 20, 'bold'))

ibi.penup()
ibi.setposition(x=0, y=0)
ibi.pendown()
ibi.write('GameOver', align='center', font=('Italic', 30, 'bold'))
ibi.hideturtle()

screen.mainloop()
