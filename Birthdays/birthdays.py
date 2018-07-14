import math
import numpy as np
from math import factorial

def k_pairs_share(n,k):
    prob = 1.0
    #choose k pairs, each of them gets one birthday, so we'll use up k birthdays 
    for i in range(0,k):
        #number of ways of choosing the birthday
        prob *= (n-2*i)*(n-2*i-1)/2.0
        prob *= 1/365.0
        prob *= (365-i)/365.0
    #there were k! ways of choosing those pairs
    prob *= 1.0/math.factorial(k)  
    #and now everyone else must have a different birthday
    for i in range(k,n-k):
        prob *= (365.0-i)/365.0 
    return prob

prob_2_or_less = 0

people = 14
for i in range(4):
    print i,k_pairs_share(people,i)
    if i< 3:
        prob_2_or_less += k_pairs_share(people,i)


print prob_2_or_less, 1-prob_2_or_less

prob_2_or_less = 0

people = 23
for i in range(4):
    print i,k_pairs_share(people,i)
    if i< 3:
        prob_2_or_less += k_pairs_share(people,i)


print prob_2_or_less, 1-prob_2_or_less
