import turtle
t = turtle.Turtle()
sc = turtle.Screen()

t.speed(0)
sc.bgcolor('black')
colors = ['red', 'green', 'blue', 'yellow']
for i in range(100):
    t.color(colors[i%4])
    t.circle(i*2, steps=2)
    t.left(i)
    t.pensize(i/10)

turtle.mainloop()