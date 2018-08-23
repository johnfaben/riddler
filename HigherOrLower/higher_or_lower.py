#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:28:46 2018

@author: faben
"""

import numpy as np


def higher_or_lower(n=10):
    order = list(range(n))
    np.random.shuffle(order)
    deck = [1 for i in range(n)]
    current = -1
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
        

for k in range(1,21):
    n = 100000    
    wins = 0.0
    for i in range(n):    
        wins += higher_or_lower(k)

    print(k,wins/n)