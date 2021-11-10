#TurtleDrawKR - Part 3
#Reading a text file line by line
#
#By: Kevin Reyes
#
#All rights reserved.

import turtle

TEXTFILENAME = 'turtle-draw.txt'

print('turtleDrawKR - Part 3')

turtleDrawKR = turtle.Turtle()
turtleDrawKR.speed(10)
turtleDrawKR.penup()


print('Reading a text file line by line')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDrawKR.color(color)
        turtleDrawKR.goto(x,y)
        turtleDrawKR.pendown()

    if (len(parts) == 1):
        turtleDrawKR.penup()

    line = turtleDrawTextfile.readline()


turtle.done()
turtleDrawTextfile.close()
print('\nEnd')


