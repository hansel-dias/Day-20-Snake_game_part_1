from shutil import move
from turtle import Turtle

POSITION = [(0,0),(-20,0),(-40,0)]
MOVE = 20

UP  = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
       def __init__(self):
              self.instances = []
              self.create_snake()
              self.head = self.instances[0]


       def create_snake(self):
              for position in POSITION:
                     self.add_snake(position)

       def add_snake(self,position):
                     tim = Turtle("square")
                     tim.color("white")
                     tim.penup()
                     tim.goto(position)
                     self.instances.append(tim)

       def extend_snake(self):
              self.add_snake(self.instances[-1].position())


       def move(self):
                     for seg_num in range(len(self.instances) - 1, 0, -1):
                            new_x = self.instances[seg_num - 1].xcor() # new_x = object at 2 .xcor()
                            new_y = self.instances[seg_num - 1].ycor() # new_y = object at 2 .ycor()
                            self.instances[seg_num].goto(new_x,new_y)
                     
                     self.head.forward(MOVE)

# CONTROL SNAKE USING KEYS

       def up(self):
              if self.head.heading() != DOWN:
                     self.head.setheading(UP)
       
       def down(self):
              if self.head.heading() != UP:
                     self.head.setheading(DOWN)
    
       def left(self):
              if self.head.heading() != RIGHT:
                     self.head.setheading(LEFT)

       def right(self):
              if self.head.heading() != LEFT:
                     self.head.setheading(RIGHT)