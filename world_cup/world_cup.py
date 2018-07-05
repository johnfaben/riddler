import numpy as np

matches = ['A1B2','C1D2','E1F2','G1H2','B1A2','D1C2','F1E2','H1G2']

def play(team1,team2,returnboth = False):
    if returnboth:
        return np.random.choice([team1,team2],2,False)
    else:
        return np.random.choice([team1,team2])
    
def worldcup(matches):
    pairings = [(match[:2],match[2:4] ) for match in matches]
    quarterfinals = [play(team1,team2) for team1,team2 in  pairings]
    semis = [play(quarterfinals[2*i],quarterfinals[2*i+1]) for i in range(4)]
    third,winner = play(semis[0],semis[1],True)
    
    fourth,second = play(semis[2],semis[3],True)
    #print winner, second
    #print third, fourth
    return (winner[0] == second[0] or third[0] == fourth[0],winner[0] == second[0] and third[0] == fourth[0])

tot = 0.0
tot_both = 0.0
num_its = 100000

for i in range(num_its):
    results = worldcup(matches)
    if results[0]:
        tot += 1
        if results[1]:
            tot_both +=1

print tot,tot_both,tot/num_its,tot_both/num_its