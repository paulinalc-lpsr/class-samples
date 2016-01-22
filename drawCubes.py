# import turtle too be able to draw the cubes
import turtle
# this will draw the top part of the cube
# only needs to draw that part only one time
# the top part of the cube will be dark blue
def drawTopRhombus(myTurtle):
  count = 0
  while count < 1:
    myTurtle.fillcolor("dark blue")
    myTurtle.begin_fill()
    myTurtle.left(30)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(30)
    myTurtle.end_fill()
    count = count + 1
# this will draw the right side of the cube
# the color will be blue    
def drawRightRhombus(myTurtle):
    count = 0
    while count < 1:
      myTurtle.fillcolor("blue")
      myTurtle.begin_fill()
      myTurtle.left(90)
      myTurtle.forward(20)
      myTurtle.right(60)
      myTurtle.forward(20)
      myTurtle.right(120)
      myTurtle.forward(20)
      myTurtle.right(60)
      myTurtle.forward(20)
      myTurtle.end_fill()
      count = count + 1
# this will draw the left side of the cube
# this side of the cube will be light blue      
def drawLeftRhombus(myTurtle):
  count = 0 
  while count < 1:
    myTurtle.fillcolor("light blue")
    myTurtle.begin_fill()
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.end_fill()
    count = count + 1      
# set a name for your turtle so it can run the code    
shawn = turtle.Turtle()
# this will make the top rows for all of them
# set a while loop too create only the top  part 4 times
def makeFirstTopRow(myTurtle):
  count = 0 
  while count < 4:
    drawTopRhombus(shawn)
    shawn.penup()
    shawn.forward(35)
    shawn.pendown()
    count = count + 1
# this will make the right side on the first, second and third row
def makeFirstRightSideRow(myTurtle):
  count = 0
  while count < 4:
    drawRightRhombus(shawn)
    shawn.penup()
    shawn.left(150)
    shawn.forward(35)
    shawn.pendown()
    count = count + 1
# this wil create te left side of the cube after the top and the right side of the cube is created
def makeFirstLeftSideRow(myTurtle):
  count = 0
  while count < 4:
    drawLeftRhombus(shawn)
    shawn.penup()
    shawn.right(90)
    shawn.forward(35)
    shawn.right(150)
    shawn.pendown()
    count = count + 1
# to make the process go faster add speed to your turtle
shawn.speed(0)
# this will creat th first row of cubes
def makeFirstRow(myTurtle):
  makeFirstTopRow(shawn)
  shawn.penup()
  shawn.goto(0,-20)
  shawn.pendown()
  makeFirstRightSideRow(shawn)
  shawn.penup()
  shawn.goto(0,0)
  shawn.right(150)
  shawn.pendown()
  makeFirstLeftSideRow(shawn)
# this will make the second row of cubes
def makeSecondRow(myTurtle):
  shawn.penup()
  shawn.goto(18,10)
  shawn.right(210)
  shawn.pendown()
  makeFirstRightSideRow(shawn)
  shawn.penup()
  shawn.goto(18,30)
  shawn.pendown()
  makeFirstTopRow(shawn)
  shawn.penup()
  shawn.goto(18,30)
  shawn.right(150)
  shawn.pendown()
  makeFirstLeftSideRow(shawn)
# this will make the third row of cubes
# this is the final row of cubes that will be created
def makeThirdRow(myTurtle):
  shawn.penup()
  shawn.goto(37,40)
  shawn.right(210)
  shawn.pendown()
  makeFirstRightSideRow(shawn)
  shawn.penup()
  shawn.goto(37,60)
  shawn.pendown()
  makeFirstTopRow(shawn)
  shawn.penup()
  shawn.goto(37,60)
  shawn.right(150)
  shawn.pendown()
  makeFirstLeftSideRow(shawn)

# this will mae the three rows of cubes
makeFirstRow(shawn)
makeSecondRow(shawn)
makeThirdRow(shawn)

exitturtleonclick()
