#Import turtle
#Move turtle to 0,-100
#Pen down Move down 50 units
#turn left and move 50 units
#Turn up, move 50 units
#Goto 0,-100
#movue up 50 units
#move left 50 units
#move right 100 units
#pen up
#move to 0,0
#move right 50 units
#pen down
#move down 50 units
#move right 50 units
#move up 100 untis
#move left 50 units
#move down 50 units
#move right 50 units

import turtle
turtle.pencolor('purple')
turtle.pensize(6)
turtle.showturtle()
north = 90
south = 270
east = 0
west = 180

turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.setheading(south)
turtle.forward(50)
turtle.setheading(west)
turtle.forward(50)
turtle.setheading(north)
turtle.forward(50)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.setheading(north)
turtle.forward(50)
turtle.setheading(west)
turtle.forward(50)
turtle.setheading(east)
turtle.forward(100)

turtle.penup()
turtle.goto(75, 0)
turtle.pendown()
turtle.setheading(south)
turtle.forward(50)
turtle.setheading(east)
turtle.forward(50)
turtle.setheading(north)
turtle.forward(100)
turtle.setheading(west)
turtle.forward(50)
turtle.goto(75, 0)
turtle.setheading(east)
turtle.forward(50)




