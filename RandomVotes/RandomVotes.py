import numpy as np
import scipy.stats  
import random
import math

def get_prob_win_vote(n,fixed_votes = 1,prob = 0.5):
    rv = scipy.stats.binom(n-fixed_votes,prob)
    return rv.sf(math.floor(n/2)-fixed_votes)

def get_prob_win_vote_approx(n,fixed_votes = 1, prob = 0.5):
    return scipy.stats.norm.sf(math.floor(n/2)-fixed_votes,(n-fixed_votes)*prob,math.sqrt((n-fixed_votes)*prob*(1-prob)))

def get_prob_vote_matters(n,fixed_votes = 1,prob = 0.5):
    rv = scipy.stats.binom(n-fixed_votes,prob)
    return rv.sf(math.floor(n/2)-fixed_votes)-rv.sf(math.floor(n/2))

def get_num_votes_to_fix(n,prob_of_victory):
    for i in range(n+1):  
        if n > 1000:
            prob_i = get_prob_win_vote_approx(n,i)
        else:
            prob_i = get_prob_win_vote(n,i)
        if prob_i > prob_of_victory: return i

print get_prob_win_vote_approx(7000000000,100000)

#print get_num_votes_to_fix(7000000000,0.5)


#n = 1025
#for i in range(n):
#    if i%100 == 0:
#        print 'if I fix %d out of %d votes, I have a probablity of %f of winning the election. The probability my cheating matters is %f' %(i,n,get_prob_win_vote(n,i),get_prob_vote_matters(n,i))
