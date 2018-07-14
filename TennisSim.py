class Score:
    def __init__(self,sets=(0,0),games=(0,0),points=(0,0)):
        self.points = points
        self.sets = sets
        self.games = games

    def add_point(self):
        if self.points[0] > 3:
            if self.points[0] > self.points[1] + 1:
       
