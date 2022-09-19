startingpos=(0,-280)
movedis=10
endline=280
from turtle import Turtle,Screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color('black')
        self.rest()
        self.left(90)
        screen = Screen()
        screen.listen()
        screen.onkey(self.move,'Up')
    def rest(self):
        self.goto(0, -280)

    def move(self):
        self.forward(10)

    def cross(self):
        if self.ycor() > endline:
            return True
        else:
            return False