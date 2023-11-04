import turtle
t = turtle.Turtle()
sc = turtle.Screen()

t.speed(0)
sc.bgcolor('black')
colors = ['red', 'green', 'blue', 'yellow']
for i in range(100):
    t.color(colors[i%4])
    t.forward(i*2)
    t.left(90)
    t.forward(i+5)
    # t.pensize(i/5 +1)

turtle.mainloop()