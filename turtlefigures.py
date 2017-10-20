from turtle import *
import math

def drawing():
     pen = Pen()
     screen = Screen()
     pen.color("black")
     pen.speed(10)
     pen.width(1)
     screen.bgcolor("white")

 

def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

# end tree



def tree4(n, l, pen):
     '''
     tree4 constrcts a quad tree with 4 simila branches symetrically positioned.
     '''
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1,l/2, pen)
     pen.right(60)
     tree4(n-1,l/2, pen)
     pen.left(90)
     pen.backward(l)

# end tree



def fern(n, l, pen):
    '''
    this constructs a fern with 3 branches angled with 45, 30, 10 degree.
    '''
    if n==0 or l<2:
        return
    #endif
    pen.forward(0.3*l)
    pen.right(45);fern(n-1,l/2, pen);pen.left(45)
    pen.forward(0.7*l)
    pen.left(30);fern(n-1,l/2, pen);pen.right(30)
    pen.forward(l)
    pen.right(10);fern(n-1,0.75*l, pen);pen.left(10)
    pen.backward(2*l)

#end fern



def gasket(n, l, pen):
     '''
     gasket to draw the sierpinsky gasket on equilateral triangle.
     '''
 
     if n==0 or l<2:
          for i in range(3):
               pen.forward(l);pen.left(120)
          #end for
          return
     #endif
     for i in range(3):
 
          gasket(n-1, l/2, pen);pen.forward(l);pen.left(120)
     #endfor
#end gasket



def square(n, l, pen):

     if n==0 or l<2:
          for i in range(4):
               pen.forward(l);pen.left(90)
          #end for
          return
     #endif
     for i in range(4):
          square(n-1, 2*l/5, pen);pen.forward(l);pen.left(90)
     #endfor
#end square



def hexagon(n, l, pen):

     if n==0 or l<2:
          for i in range(6):
               pen.forward(l);pen.left(60)
          #end for
          return
     #endif
     for i in range(8):
          hexagon(n-1, l/4, pen);pen.forward(l/2);pen.left(45)
     #endfor
#end square



def circle(n, l, pen):
     pen.circle(l)
     if n == 0 or l < 2:
         return
     for i in range(4):
          circle(n-1, l/3, pen);
          pen.up();pen.forward(l);pen.left(90);pen.forward(l);pen.down()
          pen.circle(l/3)


     
#end circle

          
     
def koch(n,l, pen):
     if n==0 or l<2:
          pen.forward(l)
          return
     #end if

     koch(n-1,l/3, pen)
     pen.left(60)
     koch(n-1,l/3, pen)
     pen.right(120)
     koch(n-1,l/3, pen)
     pen.left(60)
     koch(n-1,l/3, pen)

#end koch
     
def flake(n, l, pen):
     for i in range(3):
          koch(n,l, pen)
          pen.right(120)

#end flake


def s(n, l, pen):

     if n==0 or l<2:

          pen.forward(l)
          return
     #end if

     s(n-1,l/3, pen)
     pen.right(90)
     s(n-1,l/3, pen)
     pen.left(90)
     s(n-1,l/3, pen)
     pen.left(90)
     s(n-1,l/3, pen)
     pen.right(90)
     s(n-1,l/3, pen)   

#end s

def Snow(n, l, pen):
 
     for i in range(9):
          s(n, l/3, pen)
          pen.left(40)
#end snow



def circleSquare(n, l, pen):

     if n==0 or l<2:         
          return
     #end if
    
     for i in range(4):

          circleSquare(n-1, l/3, pen);
          pen.circle(l/3);
          pen.forward(l);pen.left(90);pen.forward(l);

#end circleSquire



def sss(n, l, pen):
     if n==0 or l<2:
     
          return
     #endif

     sss(n-1, l, pen)
     pen.right(45)
     pen.forward(l)
     pen.right(45)
     sss(n-1, l, pen)
     pen.left(90)
     pen.forward(l)
     pen.left(90)
     sss(n-1, l, pen)
     pen.right(45)
     pen.forward(l)
     pen.right(45)
     sss(n-1, l, pen)
#end sss
     
def Sierpiński(n, l, pen):
     if n==0 or l<2:
          return
     for i in range(4):
 
          sss(n, l/9, pen);pen.right(90)
#end Sierpinski


    
def ssr(n, l, pen):
     if n==0 or l<2:
     
          return
     #endif

     sss(n-1, l/3, pen)
     pen.right(45)
     pen.forward(l/3)
     pen.right(45)
     sss(n-1, l/3, pen)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     sss(n-1, l/3, pen)
     pen.right(45)
     pen.forward(l/3)
     pen.right(45)
     sss(n-1, l/3, pen)
#end ssr
     
def star(n, l, pen):
     if n==0 or l<2:
          return
     for i in range(6):
 
          ssr(n, l/9, pen);pen.right(60)
#end star



 
 

     

     
     
     
          


     





















    

