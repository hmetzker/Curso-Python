from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

def poligono(t, n, comprimento):
   angulo = 360.0 / n
   for i in range(n):
       fd(t, comprimento)
       lt(t, angulo)



def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    comprimento = circumference / n
#    polygon(t, n, length)
    poligono(t, n, comprimento)

circle(bob, 50)
wait_for_user()
