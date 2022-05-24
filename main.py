from turtle import Screen, Turtle, distance
import time
from snake import Snake
from food_part2 import Food
from score_part2 import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()


# turtle = Turtle()
# turtle.write("Home = ", True, align="center")
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:  # while game_is_on move the instances.i.e all tims
       screen.update()
       time.sleep(0.1)

       snake.move()
      

       # detect collision with food
       if snake.head.distance(food) < 15:
              # score.score = score.score + 1
              food.refresh()
              score.increase_score()
              snake.extend_snake()
              # score = Scoreboard()

       # detect collision with wall
       if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300 :
              game_is_on = False
              score.game_over()


       # detect collision with tail or body of snake
              
       for body in snake.instances[1:]:
              if snake.head.distance(body) < 10:  # if distance of the head from the body < 10
                     game_is_on = False
                     score.game_over()






















screen.exitonclick()