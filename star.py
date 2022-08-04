import turtle
colors=['yellow','white','green','blue','red','cyan']
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(20)
for i in range(100):
    t.color(colors[i%6])
    t.fd(i*5)
    t.left(200)
    t.width(2)