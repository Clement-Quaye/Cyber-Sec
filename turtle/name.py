#This is a program to write the name of a saturday born using turtle

import turtle

joy = turtle.Turtle()
joy.color("blue")
joy.width(3)
joy.speed(0)

#Letter A
joy.goto(0,0)
joy.left(80)
joy.forward(50)
joy.right(180-22)
joy.forward(35)
joy.right(100)
joy.forward(12)
joy.backward(12)
joy.left(100)
joy.forward(15)

#Letter M
joy.penup()
joy.goto(25,0)
joy.pendown()
joy.left(155)
joy.forward(50)
joy.right(155)
joy.forward(50)
joy.left(155)
joy.forward(50)
joy.right(155)
joy.forward(50)

#Letter A
joy.penup()
joy.goto(75,0)
joy.left(160)
joy.pendown()
joy.forward(50)
joy.right(160)
joy.forward(35)
joy.right(100)
joy.forward(12)
joy.backward(12)
joy.left(100)
joy.forward(15)

joy.penup()
joy.left(160)
joy.forward(10)


input()