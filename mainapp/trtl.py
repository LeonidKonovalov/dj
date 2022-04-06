import turtle as t
import random
t.speed(500)
for i in range(88):
  red = random.random()
  green = random.random()
  blue = random.random()
  t.color(red, green, blue)
  t.begin_fill()
  t.circle(50) 
  t.end_fill()
  t.rt(45)