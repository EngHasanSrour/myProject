import turtle
t = turtle.Turtle()
sc = turtle.Screen()

sc.bgcolor('black')
colors = ['red', 'green', 'blue', 'yellow']
for i in range(400):
    t.color(colors[i%4])
    t.forward(i*2)
    t.left(144)
    t.pensize(i*2)