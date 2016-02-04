import turtle
import math

#Instantiate turtle object
leo = turtle.Turtle()

leo.shape("turtle")
leo.color("black", "green")
leo.hideturtle()
leo.speed(10)

#Recursive function to draw the triangles
def draw_sierpinksi(size, depth):
    if depth==0:
        leo.begin_fill()
        for x in range (0,3):
            leo.forward(size)
            leo.left(120)
        leo.end_fill()

    else:
        draw_sierpinksi(size/2, depth-1)

        #Position for second triangle
        leo.penup()
        leo.setpos((leo.xcor() + size/2),leo.ycor())
        leo.pendown()

        draw_sierpinksi(size/2, depth-1)

        #Position for third triangle
        leo.penup()
        leo.setpos((leo.xcor()-(size/2)*math.cos(math.pi/3)),(leo.ycor()+(size/2)*math.sin(math.pi/3)))
        leo.pendown()

        draw_sierpinksi(size/2, depth-1)

        #Position at origin relative to current depth
        leo.penup()
        leo.setpos((leo.xcor()-(size/2)*math.cos(math.pi/3)),(leo.ycor()-(size/2)*math.sin(math.pi/3)))
        leo.pendown()

#Call the drawing function
draw_sierpinksi(400, 4)
