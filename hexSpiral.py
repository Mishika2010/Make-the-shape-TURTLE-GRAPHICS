import turtle
colors = ["pink","green","red","magenta","blue","purple"]
hex = turtle.Pen()
turtle.bgcolor("aqua")
for i in  range(360):
    hex.pencolor(colors[i%6])
    hex.width(i/150+1)
    hex.forward(i)
    hex.left(59)
