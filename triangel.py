import turtle
turtle.setup(1300,1500,0,0)
turtle.pensize(30)
turtle.bgcolor("green")
colors=["red","yellow","blue"]
for i in range (3):
    turtle.color(colors[i % 3])
    turtle.fd(200)
    turtle.seth(120*(i+1))
