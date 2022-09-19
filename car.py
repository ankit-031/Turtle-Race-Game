color=['red','green','purple','pink','orange','lightgreen','yellow']
startmove=5
moveinc=10
from turtle import Turtle
import  random
class  Car:
        def __init__(self):
            self.allcar=[]
            self.sped=moveinc
        def create(self):
            ran=random.randint(1,5)
            if ran==1:
                tim=Turtle()
                tim.shape("square")
                tim.color(random.choice(color))
                tim.shapesize(1,2)
                tim.penup()
                y=random.randint(-250,250)
                tim.goto(300,y)
                self.allcar.append(tim)
        def movecare(self):
            for car in self.allcar:
                car.backward(self.sped)

        def level(self):
            self.sped +=10
