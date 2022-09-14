from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.color('white')
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Courier', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Courier', 12, 'normal'))

    def game_over(self):
        if self.score > self.high_score:
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.score))
                self.high_score = self.score
            self.clear()
            self.write(f'Score: {self.score} High Score: {self.high_score}', align='center',
                       font=('Courier', 12, 'normal'))
        self.score = 0
        self.goto(0, 0)
        self.write('Game Over.', align='center', font=('Courier', 12, 'normal'))
