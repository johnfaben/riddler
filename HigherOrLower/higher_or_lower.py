#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:28:46 2018

@author: faben
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools


def higher_or_lower(n=10):
    order = list(range(n))
    np.random.shuffle(order)
    deck = [1 for i in range(n)]
    current = -1
    lower = False
    for card in order:
        #print(card)
        if current > -1:
            if lower and card > current:
                return 0
            if not lower and card < current:
                return 0
        current = card
        deck[card] = 0
        if sum(deck[:card]) > sum(deck[card:]):
            lower = True
        else:
            lower = False
    return 1
        
win_probs = [1]
for k in range(1,25):
    n = 100000    
    wins = 0.0
    for i in range(n):    
        wins += higher_or_lower(k)
    win_probs.append(wins/n)


powers = [1,1] + [0.75**n for n in range(25)]

plt.plot(powers, label = '0.75^n-2')
plt.plot(win_probs, label = 'win probability')

plt.annotate('(%d,%.3f)' %(4,win_probs[4]),xy=(4,win_probs[4]))
plt.annotate('(%d,%.3f)' %(9,win_probs[9]),xy=(9,win_probs[9]))
plt.annotate('(%d,%.3f)' %(20,win_probs[20]),xy=(20,win_probs[20]))
plt.legend()
plt.xticks(range(0,25,4))
plt.show()
    



    
    
    

    
