import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Ping-pong")
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
ball = Ball()
l_score = Score(-200)
r_score = Score(200)


def in_contact(p, b):
    # print(p.distance(b))
    if p.distance(b) < 50:
        return True
    else:
        return False


game_is_on = True
h_angle = 45
h_angle2 = 225
cs = 0.1
while game_is_on:
    ball.move_ball()
    time.sleep(cs)
    screen.update()
    # print(ball.pos())
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if in_contact(left_paddle, ball) and ball.xcor() < -320:
        ball.p_bounce()
    if in_contact(right_paddle, ball) and ball.xcor() > 320:
        ball.p_bounce()
    if ball.xcor() > 380:
        ball.reset_ball()
        cs *= 0.9
        l_score.update()
    if ball.xcor() < -380:
        cs *= 0.9
        ball.reset_ball()
        r_score.update()

screen.exitonclick()
