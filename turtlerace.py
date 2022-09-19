from turtle import Turtle,Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard
screen=Screen()
# tim=Turtle("turtle")
screen.setup(width=600,height=600)
screen.tracer(0)
p=Player()
c=Car()
s=Scoreboard()
ison=True
while ison:
    time.sleep(0.1)
    screen.update()
    c.create()
    c.movecare()
    for car in c.allcar:
        if car.distance(p) < 19:
            ison=False
            s.gameover()
    if p.cross():
        p.rest()
        c.level()
        s.inc()



screen.exitonclick()