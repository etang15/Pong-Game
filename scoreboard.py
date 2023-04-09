from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lScore, align="center", font=("Courier", 80,"normal"))
        self.goto(100,200)
        self.write(self.rScore, align="center", font=("Courier", 80,"normal"))
    
    def lPoint(self):
        self.lScore += 1
        self.update()
    
    def rPoint(self):
        self.rScore += 1
        self.update()
        