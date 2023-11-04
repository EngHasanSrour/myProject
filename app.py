import turtle
t = turtle.Turtle()
sc = turtle.Screen()

t.speed(0)
sc.bgcolor('black')
colors = ['red', 'green', 'blue', 'yellow']
for i in range(200):
    t.color(colors[i%4])
    t.circle(i, steps=4)
    t.left(45)
    t.pensize(i/10 + 1)

turtle.mainloop()