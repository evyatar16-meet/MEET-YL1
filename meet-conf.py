import turtle

def col1():
	turtle.color("red")
turtle.getscreen().onkey(col1,"r")

def circle(x,y):
	turtle.begin_fill()
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.circle(30)
	turtle.color("red", "green")
	turtle.color()
	('red', 'green')
	color("#285078", "#a0c8f0")
	color()
	((40.0, 80.0, 120.0), (160.0, 200.0, 240.0))
	
turtle.onscreenclick(circle,btn=1,add=True)
turtle.ondrag(circle)

evyatar=turtle.Turtle()

def square(x,y):
	evyatar.penup()
	evyatar.goto(x,y)
	evyatar.pendown()
	evyatar.goto(x-40,y)
	evyatar.goto(x-40,y-40)
	evyatar.goto(x,y-40)
	evyatar.goto(x,y)

turtle.onscreenclick(square,btn=3,add=True)
evyatar.ondrag(square)

turtle.mainloop()



