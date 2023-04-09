from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# 1. Create the main screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Elliott's Pong Game")
screen.tracer(0)

# 2. Create & move a paddle
rPaddle = Paddle((350,0))
lPaddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(rPaddle.up,"Up")
screen.onkey(rPaddle.down,"Down")
screen.onkey(lPaddle.up,"w")
screen.onkey(lPaddle.down,"s")

game_on = True
while game_on:
    time.sleep(ball.moveSpeed)
    screen.update()
    
# 3. Create another paddle - refer to rPaddle & lPaddle

# 4. Create the ball & make it move
    ball.move()
# 5. Detect collision with wall & bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
# 6. Detect collision with paddle
    if ball.distance(rPaddle) < 50 and ball.xcor() > 320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()
# 7. Detect when a paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.lPoint()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.rPoint()
# 8. Keep score
screen.exitonclick()