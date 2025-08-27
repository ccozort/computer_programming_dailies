
'''
Create a pixel art character using the code below.

Things to think about:
Use of global variables
Use of color
Use of functions
Use of parameters
Use of arguments
Use of lists
Use of for loops

'''
MAP = ["xoooxxoxoxoooxooox",
       "xoooxxoxoxoooxooox",
       "xoooxxoxoxoooxooox"]

PIXEL_SIZE = 20

import turtle
import time
from turtle import *
from random import randint

turtle.colormode(255)

pen = turtle.Turtle()

pen.pensize(0)
pen.speed(0)

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=640, height=640)

side_length = PIXEL_SIZE

ELAP = 0

start_time = time.perf_counter()

def draw_pixel(x,y,color):
    print('draw func')
    global end_time
    end_time = time.perf_counter()
    global ELAP
    global start_time
    ELAP += end_time-start_time
    start_time = end_time
    pen.penup()

    pen.goto(x,y)

    pen.pendown()

    pen.fillcolor(color)
    pen.begin_fill()

    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)             

    pen.end_fill()



for i in range(32):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    print(color)
    draw_pixel(-320+PIXEL_SIZE*i,320,color)
    
    print(ELAP)





# turtle.done()    



elapsed_time = end_time - start_time



# drawing a grid
for y in range(3):
    for x in range(3):
        print(f"y: {y}, x: {x}")


# traversing a list (array)
# for i in MAP:
#     print(i)
#     for j in i:
#         print(j)
#         if j == "x":
#             # print("make it blue")