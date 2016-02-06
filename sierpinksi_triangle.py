import turtle

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
            leo.forward(size/2)
            leo.pendown()

            make_triangles(size/2, depth-1)

            #Position for third triangle
            leo.penup()
            leo.left(120)
            leo.forward(size/2)
            leo.right(120)
            leo.pendown()

            make_triangles(size/2, depth-1)

            #Position at origin relative to current depth
            leo.penup()        
            leo.left(60)
            leo.back(size/2)
            leo.right(60)
            leo.pendown()

    make_triangles(size, depth)

draw_sierpinksi(400, 4)
