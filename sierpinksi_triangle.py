import turtle
import math

#Instantiate Leonardo the turtle
window = turtle.Screen()
window.bgcolor("#e1e1ea")
leo = turtle.Turtle()
leo.shape("turtle")
leo.color("blue", "green")
leo.speed(10)

def draw_sierpinksi(size, depth):
    #Center the triangle on screen
    leo.penup()
    leo.setpos(-size/2, -size/2)
    leo.pendown()

    #Recursive function to draw the triangles
    def make_triangles(size, depth):
        if depth==0:
            leo.begin_fill()
            for x in range (0,3):
                leo.forward(size)
                leo.left(120)
            leo.end_fill()

        else:
            make_triangles(size/2, depth-1)

            #Position for second triangle
            leo.penup()
            leo.setpos((leo.xcor() + size/2),leo.ycor())
            leo.pendown()

            make_triangles(size/2, depth-1)

            #Position for third triangle
            leo.penup()
            leo.setpos((leo.xcor()-(size/2)*math.cos(math.pi/3)),(leo.ycor()+(size/2)*math.sin(math.pi/3)))
            leo.pendown()

            make_triangles(size/2, depth-1)

            #Position at origin relative to current depth
            leo.penup()
            leo.setpos((leo.xcor()-(size/2)*math.cos(math.pi/3)),(leo.ycor()-(size/2)*math.sin(math.pi/3)))
            leo.pendown()

    make_triangles(size, depth)

draw_sierpinksi(400, 4)
