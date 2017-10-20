from tkinter import *
from tkinter.ttk import *
import turtlefigures
from turtle import *
from tkinter import PhotoImage


# contruct the Tk window
root = Tk()
root.geometry("300x100+0+300")
root.title("Turtle Fractals")
root.configure(background="old lace")

#contruct pen and screen
pen = Pen()
screen = Screen()
pen.color("LemonChiffon4")
pen.speed(10)
pen.width(3)
screen.bgcolor("lavender")




# define handlers

def onClear():
    # reset the entry-s
    orderStr.set("")
    lengthStr.set("")
    # reset the screen
    pen.reset()
    pen.color("LemonChiffon4")
    pen.speed(100)
    pen.width(3)
#end onClear


def onTree():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()
    pen.color("LemonChiffon4")

    # draw the tree
    turtlefigures.tree(order, length, pen)


def onTree4():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()
    pen.color("LemonChiffon4")

    # draw the tree
    turtlefigures.tree4(order, length, pen)


def onfern():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.down()
    pen.color("LemonChiffon4")
    

    # draw the fern
    turtlefigures.fern(order, length, pen)


def ongasket():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-150);pen.sety(-100);pen.down()
    pen.color("LemonChiffon4")
    
    
    # draw the gasket
    turtlefigures.gasket(order, length, pen)


def onSquare():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.sety(-200);pen.setx(-150);pen.down()
    pen.color("LemonChiffon4")

    # draw the tree
    turtlefigures.square(order, length, pen)


def onhexagon():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(-100);pen.down()
    pen.color("LemonChiffon4")

    # draw the hexagon
    turtlefigures.hexagon(order, length, pen)
    

def oncircle():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.sety(-200);pen.down()
    pen.color("LemonChiffon4")


    # draw the circle
    turtlefigures.circle(order, length, pen)


def onflake():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-150);pen.sety(100);pen.down()
    pen.color("LemonChiffon4")

    # draw the flake
    turtlefigures.koch(order, length, pen)


def onSnow():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-100);pen.sety(-100);pen.down()
    pen.color("LemonChiffon4")

    # draw the Snow
    turtlefigures.Snow(order, length, pen)


def oncircleSquare():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.sety(-200);pen.down()
    pen.color("LemonChiffon4")

    # draw the circleSquare
    turtlefigures.circleSquare(order, length, pen)


def onSierpiński():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.sety(200);pen.down()
    pen.color("LemonChiffon4")

    # draw the Sierpiński
    turtlefigures.sss(order, length, pen)


def onstar():
    # get the order and length
    order = int(orderStr.get())
    length = int(lengthStr.get())

    # get a better initial position
    pen.up();pen.setx(-200);pen.sety(200);pen.down()
    pen.color("LemonChiffon4")

    # draw the star
    turtlefigures.star(order, length, pen)

def makeCommandMenu():
    CmdBtn = Menubutton(text='Select Figure')

    CmdBtn.menu = Menu(CmdBtn)
    CmdBtn.menu.choices = Menu(CmdBtn.menu)
    CmdBtn.menu.choices.tree = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.tree4 = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.fern = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Gasket = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Square = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Hexagon = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Circle = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Flake = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Snow = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.CircleSquare = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Sierpiński = Menu(CmdBtn.menu.choices)
    CmdBtn.menu.choices.Star = Menu(CmdBtn.menu.choices)

    CmdBtn.menu.choices.tree.add_command(label='This constructs a binary tree.', command=onTree)
    CmdBtn.menu.choices.tree4.add_command(label='This constructs a quad tree with 4 similar branches symetrically positioned.', command=onTree4)
    CmdBtn.menu.choices.fern.add_command(label='This constructs a fern with 3 branches angled with 45, 30, 10 degree.', command=onfern)
    CmdBtn.menu.choices.Gasket.add_command(label='This constructs the sierpinsky triangle on equilateral triangle.', command=ongasket)
    CmdBtn.menu.choices.Square.add_command(label='This constructs the sierpinsky square on equilateral square.', command=onSquare)
    CmdBtn.menu.choices.Hexagon.add_command(label='This constructs the Polyflake on equilateral hexagon.', command=onhexagon)
    CmdBtn.menu.choices.Circle.add_command(label='This constructs the sierpinsky circle on equilateral circle.', command=oncircle)
    CmdBtn.menu.choices.Flake.add_command(label='This constructs the flake.', command=onflake)
    CmdBtn.menu.choices.Snow.add_command(label='This constructs another form of flake.', command=onSnow)
    CmdBtn.menu.choices.CircleSquare.add_command(label='This construction combine the circle and square.', command=oncircleSquare)
    CmdBtn.menu.choices.Sierpiński.add_command(label='This constructs the Sierpiński curve.', command=onSierpiński)
    CmdBtn.menu.choices.Star.add_command(label='This construction using Sierpiński curve to create the star.', command=onstar)
    
    CmdBtn.menu.add_cascade(label='Tree', menu=CmdBtn.menu.choices.tree)
    CmdBtn.menu.add_cascade(label='Tree4', menu=CmdBtn.menu.choices.tree4)
    CmdBtn.menu.add_cascade(label='Fern', menu=CmdBtn.menu.choices.fern)
    CmdBtn.menu.add_cascade(label='Gasket', menu=CmdBtn.menu.choices.Gasket)
    CmdBtn.menu.add_cascade(label='Square', menu=CmdBtn.menu.choices.Square)
    CmdBtn.menu.add_cascade(label='Hexagon', menu=CmdBtn.menu.choices.Hexagon)
    CmdBtn.menu.add_cascade(label='Circle', menu=CmdBtn.menu.choices.Circle)
    CmdBtn.menu.add_cascade(label='Flake', menu=CmdBtn.menu.choices.Flake)
    CmdBtn.menu.add_cascade(label='Snow', menu=CmdBtn.menu.choices.Snow)
    CmdBtn.menu.add_cascade(label='CircleSquare', menu=CmdBtn.menu.choices.CircleSquare)
    CmdBtn.menu.add_cascade(label='Sierpiński', menu=CmdBtn.menu.choices.Sierpiński)
    CmdBtn.menu.add_cascade(label='Star', menu=CmdBtn.menu.choices.Star)


    
    CmdBtn.pack()

    CmdBtn['menu'] = CmdBtn.menu
    return CmdBtn



#end onhandlerF


# make the interface

# add all component as self.widget

titleLabel = Label(root, text = " Turtle Interface",font=('Times', '18', 'italic'))
titleLabel.grid(row = 0, column = 1, columnspan = 3)

orderLabel = Label(root, text = "Order")
orderLabel.grid(row = 2, column = 0)

lengthLabel = Label(root, text = "Length")
lengthLabel.grid(row = 3, column = 0)

orderStr = StringVar()
orderEntry = Entry(root, width = 10, textvariable = orderStr)
orderEntry.grid(row = 2, column = 1)

lengthStr = StringVar()
lengthEntry = Entry(root, width = 10, textvariable = lengthStr)
lengthEntry.grid(row = 3, column = 1)

clearButton = Button(root, text = "Clear", command = onClear)
clearButton.grid(row = 3, column = 2)

CmdBtn = makeCommandMenu()
CmdBtn.grid(row = 2, column =2 )

'''
titleLabel = Label(root, text = "Select Figure")
titleLabel.grid(row = 2, column = 1, columnspan = 4)

treeButton = Button(root, text = "Tree", command = onTree)
treeButton.grid(row = 3, column = 0)

fernButton = Button(root, text = "Fern", command = onfern)
fernButton.grid(row = 3, column = 1)

gasketButton = Button(root, text = "Gasket", command = ongasket)
gasketButton.grid(row = 3, column =2)

hexagonButton = Button(root, text = "Hexagon", command = onhexagon)
hexagonButton.grid(row = 3, column =3)

circleButton = Button(root, text = "Circle", command = oncircle)
circleButton.grid(row = 3, column =4)

flakeButton = Button(root, text = "Flake", command = onflake)
flakeButton.grid(row = 4, column =0)

SnowButton = Button(root, text = "Snow", command = onSnow)
SnowButton.grid(row = 4, column =1)

circleSquareButton = Button(root, text = "CircleSquare", command = oncircleSquare)
circleSquareButton.grid(row = 4, column =2)

SierpińskiButton = Button(root, text = "Sierpiński", command = onSierpiński)
SierpińskiButton.grid(row = 4, column =3)

starButton = Button(root, text = "Star", command = onstar)
starButton.grid(row = 4, column =4)
'''


mainloop()  

