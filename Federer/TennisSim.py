#vim tabstop=8 expandtab shiftwidth=4 softtabstop=4
import random as rn
import matplotlib.pyplot as plt
import numpy as np

class Score:
    def __init__(self,sets=(0,0),games=(0,0),points=(0,0)):
        self.sets = sets
        self.games = games
        self.points = points
        self.final_score = []
	self.is_over = False
	self.winner = -1
	self.point_total = 0

    def add_point(self,player):
	self.point_total+=1
        if self.games == (6,6):
           required_p = 7 
        else:
            required_p = 4
        if player == 0:
            self.points = (self.points[0]+1,self.points[1])
            if self.points[0] > required_p-1:
                if self.points[0] > self.points[1] + 1:
                    self.points = (0,0)
                    self.add_game(0)
        elif player == 1:
            self.points = (self.points[0],self.points[1]+1)
            if self.points[1] > required_p - 1:
                if self.points[1] > self.points[0] +1:
                    self.points = (0,0)
                    self.add_game(1)

    def add_game(self,player):
        if self.games == (6,6):
            self.add_set(player)
            
        elif player == 0:
            self.games = (self.games[0]+1,self.games[1])
            if self.games[0]>=6 and self.games[0]> self.games[1]+1:
                self.add_set(player)
        
        elif player == 1:
            self.games = (self.games[0],self.games[1]+1)
            if self.games[1] >= 6 and self.games[1] > self.games[0]+1:
                self.add_set(player)
    
    def add_set(self,player):
        self.final_score.append(self.games)
        if self.sets[player] == 2:
            #print 'player %d won the match %s' %(player,self.final_score)

	    self.is_over = True
	    self.winner = player
        else:
            if player == 0: self.sets = (self.sets[0]+1,self.sets[1])
            if player == 1: self.sets = (self.sets[0],self.sets[1]+1)
            self.games = (0,0)

    def __str__(self):
	return 'sets: %s \ngames %s\npoints %s'%(self.sets,self.games,self.points)

def play_match(score,prob):
    while not score.is_over:
        if rn.random() > prob:
	    score.add_point(1)
	else:
            score.add_point(0)
    return score.winner

def sim_matches(prob,sets,games,points,matches):
    totals = [0,0]
    for i in range(matches):
        score = Score(sets,games,points)
        winner = play_match(score,prob)
        totals[winner] +=1
    return totals[0]/(1.0*matches)

#just to work out how many points are played in average match
point_total = 0
match_total = 0
for i in range(10000):
    score = Score((0,0),(0,0),(0,0))
    match_total += play_match(score,0.58)
    point_total += score.point_total

print point_total/10000.0
print match_total/10000.0

#code for generating plots
win_tiebreak = []
for i in np.arange(50,65,0.1):
    win_tiebreak.append(sim_matches(i/100.0,(0,0),(0,0),(0,0),num_matches))

print 'done simulation'
num_matches = 10000
tiebreak = plt.plot(np.arange(50,65,0.1),win_tiebreak,'ro',label = 'probability of winning match')

#win_game = []
#for i in np.arange(35,50,0.2):
    #win_game.append(sim_matches(i/100.0,(2,0),(5,0),(3,0),num_matches))
 
#print win_tiebreak
#print win_game

#games = plt.plot(np.arange(35,50,0.2),win_game,'g^',label = '(5,0) (40-0) up)')
plt.legend(loc = 4)
plt.set_ylabel = 'Probability of winning match'
plt.set_xlabel = 'Probability of winning game'
plt.gcf().subplots_adjust(bottom=0.15)
plt.show()
