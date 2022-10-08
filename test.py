from turtle import *
import math
# from PIL import Image

setup(1200,600)
speed(10)
bgcolor("black")

width = 500 + 500
height = 240 + 240
height_belang = height/14

def jalur_merah():
  penup()
  goto(-250 - 250,120 + 120)
  pendown()
  fillcolor('red')
  begin_fill()
  for i in range(2):
    forward(width)
    right(90)
    forward(height)
    right(90)
  end_fill()

def jalur_putih():
  x = 120 +120 -height_belang
  setheading(0)
  for i in range(7):
    penup()
    goto(-250 - 250,x)
    pendown()
    fillcolor('white')
    begin_fill()
    for j in range(2):
      forward(width)
      right(90)
      forward(height_belang)
      right(90)
    end_fill()
    x = x-(height_belang*2)

def biru():
  goto(-250 -250,120 + 120)
  begin_fill()
  fillcolor('blue')
  for i in range(2):
    forward(width*45/100)
    right(90)
    forward(height_belang*8)
    right(90)
  end_fill()

def bulan():
  penup()
  goto(-220- 205,120+120-(height_belang*4))
  pendown()
  pencolor("yellow")
  setheading(270)
  begin_fill()
  fillcolor('yellow')
  circle(100)
  end_fill()
  penup()
  goto(-200-190,120+120-(height_belang*4))
  pendown()
  begin_fill()
  pencolor('blue')
  fillcolor('blue')
  circle(100*3.5/4)
  end_fill()
  
# def bulan():
#   penup()
#   goto(-160,100)
#   pendown()
#   pencolor("yellow")
#   setheading(180)
#   begin_fill()
#   fillcolor('yellow')
#   circle(50)
#   penup()
#   goto(-148,93)
#   pendown()
#   circle(50*3.5/4)
#   end_fill()

def correction():
  penup()
  goto(-140-120,93+120)
  pendown()
  setheading(0)
  begin_fill()
  fillcolor('blue')
  pencolor('blue')
  for g in range(2):
    forward(50*2)
    right(90)
    forward(100*2)
    right(90)
  end_fill()
  pencolor('black')

diameter = 48*2
radius = diameter/2
bucu = 360/24
z = (180*(14-2))/14
y = (180-bucu)/2
w = (360-(2*y)-z)
antara_bucu = (2*math.pi*radius)*w/360
satu_darjah = math.pi/180
i = satu_darjah*w
k = antara_bucu/i

def bintang():
  penup()
  goto(-148-125,120+120-(height_belang*4))
  forward(diameter-22*2)
  left(90)
  forward(diameter-10*2)
  pendown()
  pencolor("yellow")
  print(position())
  setheading(360-bucu/2)
  right(90)
  fillcolor('yellow')
  begin_fill()
  for q in range(14):
    forward(k)
    right(180-w)
    forward(k)
    left(180-bucu)
  end_fill()
  print(position())
  
jalur_merah()
jalur_putih()
biru()
bulan()
correction()
bintang()
penup()
goto(1200,0)
done()