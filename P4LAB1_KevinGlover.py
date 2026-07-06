# Kevin Glover
# 2026-7-5
# P4 LAB1
# Use turtle and loops to draw shapes

import turtle

win = turtle.Screen ()
pen = turtle.Turtle ()

pen.pensize(3)
pen.pencolor ("orange")
pen.shape("arrow")

for side in range(4):
    pen.forward(100)
    pen.right(90)

sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

win.mainloop()
