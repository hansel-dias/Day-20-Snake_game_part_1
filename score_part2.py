from msilib.schema import Font
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",23, "normal")


class Scoreboard(Turtle):
       def __init__(self):
              super().__init__()
              self.hideturtle()
              self.goto(0,265)
              self.score = 0
              self.color("white")
              self.speed("fastest")
              self.update_score()


       def update_score(self):
              self.write(f"Score: {self.score} ",align=ALIGNMENT,font=FONT)


       def increase_score(self):
              self.score += 1
              self.clear()
              self.update_score()

       def game_over(self):
              self.goto(0,0)
              self.write(f"Game Over",align=ALIGNMENT,font=("Courier",26, "normal"))
