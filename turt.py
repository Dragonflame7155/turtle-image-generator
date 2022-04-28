import turtle
import random
from time import sleep
turt = 0
colorlist = ['red', 'green', 'blue', 'yellow', 'black', 'purple']
turtle.colormode(255)
angle1 = random.randint(0, 360)
angle2 = random.randint(0, 360)
angle3 = random.randint(0, 360)
angle4 = random.randint(0, 360)
angle5 = random.randint(0, 360)
angle6 = random.randint(0, 360)
turtle.speed(0)
check = input('random color?(y/n):')
if check == 'y':
    turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
usrin = 'black'
if check != 'y':
    usrin = input('color:')
    turtle.color(usrin)
print(angle1, angle2, angle3, angle4, angle5, angle6)
turtle.tracer(1, 0)
turtle.hideturtle()

while True:
    turtle.reset()
    turtle.speed(0)
    turtle.ht()
    turtle.home()
    turtle.color(usrin)
    if check == 'y' or 'Y':
        turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    angle1 = random.randint(0, 360)
    angle2 = random.randint(0, 360)
    angle3 = random.randint(0, 360)
    angle4 = random.randint(0, 360)
    angle5 = random.randint(0, 360)
    angle6 = random.randint(0, 360)
    turt = 0
    for i in range(500):
        turtle.speed(0)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.right(angle1)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.forward(turt)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.left(angle2)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.forward(turt)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.right(angle3)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.forward(turt)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.left(angle4)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.forward(turt)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.right(angle5)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.forward(turt)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.left(angle6)
        #turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.forward(turt)
        turt = turt + 1
        print(i)
