import turtle
from Tkinter import *
def regular_pentagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        while side_count < 5:
                myTurtle.forward(side)
                myTurtle.left(73)


# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text = 'right', command =lambda: shawn.right(90))
penup = Button(frame, text = 'penup', command=lambda: shawn.penup())
pendown = Button(frame, text = 'pendown', command=lambda: shawn.pendown())
pentagonbtn = Button(frame, text = 'pentagonbtn', command=lambda: shawn.pentagon(5))

# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
frame.pack()
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
pentagonbtn.pack(side=LEFT)

turtle.exitonclick()
