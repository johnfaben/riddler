import csv
import operator
import random as rn

def get_initial_strategies(filename):
    count = 0    
    strategies = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile,delimiter = ',', quotechar='"')
        for row in csvreader:
    	    if count > 0:
    	        strategies.append(','.join([i for i in row[:-1]]))
    	    count += 1
    return strategies

def to_strat(name):
    return [int(i) for i in name.split(',')]


def battle(strat1,strat2):
    score = 0
    for i in range(10):
        if strat1[i] > strat2[i]:
            score += i+1
        elif strat1[i] < strat2[i]:
            score -= i+1
    if score > 0:
        return 1
    if score < 0: 
        return -1
    return 0

def crossover(strat1,strat2,mutations=0):
    child = [ 0 for k in range(10)]
    for i in range(10):
        child[i] = int((strat1[i]+strat2[i])/2)
    while sum(child) != 100:
        child[rn.randint(0,9)] += 1
    mutate(child,mutations)

    return ','.join([str(k) for k in child])

def mutate(strat,num_mutations):
    for i in range(num_mutations):
        j = rn.randint(0,9)
        if strat[j] > 0:
            k = rn.randint(0,9)
            strat[j] -= 1
            strat[k] += 1

def get_random_strats(n):
    rn_strats = []
    for i in range(n):
        rn_strats.append([0 for k in range(10)])
        for j in range(100):
            k = rn.randint(0,9)
            rn_strats[i][k] += 1
    for i in range(len(rn_strats)):
        rn_strats[i] = ','.join([str(k) for k in rn_strats[i]])
    return rn_strats

def get_parents(initial_pop,test_pop,num_parents=10):
    scores = dict()
    best_score = 0
    for strat in test_pop:
        
        scores[strat] = 0
        for opponent in initial_pop:
            scores[strat] += battle(to_strat(strat),to_strat(opponent))
        for opponent in test_pop:
            scores[strat] += battle(to_strat(strat),to_strat(opponent))
    top_k = sorted(scores,key= scores.get,reverse=True)[:num_parents]
    return top_k,scores

def get_children(parents,num_children,num_mutations=1):
    children = []
    for k in range(num_children):
        parent1 = rn.choice(parents)
        parent2 = rn.choice(parents)
        children.append(crossover(to_strat(parent1),to_strat(parent2),num_mutations))
    return children
        
filename = 'castle-solutions.csv'
initial_population = get_initial_strategies(filename)

top_10,scores = get_parents(initial_population,initial_population,10)
g = get_random_strats(500)
print g[:10]
print top_10[:10]

best_score = 0
best_strat = None
static_pop = []
for strat in top_10:
    for i in range(100):
        static_pop.append(strat)


top_1000,scores = get_parents(initial_population,initial_population,1000)
for strat in top_1000:
    static_pop.append(strat)


for i in range(1000):
    parents,scores = get_parents(static_pop,g)
    if int(scores[parents[0]])>best_score:
        print parents[0],scores[parents[0]]
        best_score = scores[parents[0]]
        best_strat = parents[0][0]
    if i%50 == 0: print [(parent,scores[parent]) for parent in parents]
    g = get_children([strategy for strategy in parents],100,2)

