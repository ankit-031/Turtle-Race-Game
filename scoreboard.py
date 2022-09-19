from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-260, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {self.level}",align="left",font=("Courier",24,"normal"))

    def inc(self):
        self.level+=1
        self.update()
    def gameover(self):
        self.goto(-70,0)
        self.write(f"Game Over",align="left",font=("Courier",50,"normal"))