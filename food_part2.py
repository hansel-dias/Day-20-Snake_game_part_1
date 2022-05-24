from random import random


import random
from turtle import Turtle


class Food(Turtle):  #inherit from turtle class

       def __init__(self):
              super().__init__()
              # self.food = Turtle() 
              self.shape("circle")   # same as Turtle.shape() --> Food.shape()
              self.penup()
              self.color("blue")
              self.shapesize(stretch_len=0.5, stretch_wid=0.5)
              self.speed("fastest")
              self.refresh()

       

       def refresh(self):
              new_x = random.randint(-280, 280)
              new_y = random.randint(-280, 280)
              self.goto(new_x, new_y)