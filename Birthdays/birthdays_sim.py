import random as rn
import numpy as np

def get_num_shared(n):
    year = [0 for i in range(365)]
    for i in range(n):
        birthday = rn.randint(0,364)
        year[birthday] = year[birthday] + 1
    return max(year),year.count(max(year))

def get_dist(n,trials = 1000):
    hist = [0 for i in range(n+1)]
    for i in range(trials):
        num_shared,freq = get_num_shared(n)
        hist[num_shared] = hist[num_shared] +1
    return hist
n = 100
num_trials = 50000
dists = dict()

p_2_or_more = [0 for i in range(n)]
p_3_or_more = [0 for i in range(n)]
p_4_or_more = [0 for i in range(n)]

for k in range(1,n):
    print k
    dists[k] = get_dist(k,num_trials)

    p_2_or_more[k] = float(sum(dists[k][2:]))/num_trials
    p_3_or_more[k] = float(sum(dists[k][3:]))/num_trials
    p_4_or_more[k] = float(sum(dists[k][4:]))/num_trials

    
print p_2_or_more
print p_3_or_more

import matplotlib.pyplot as plt

plt.xlabel('Number of People')
plt.plot(range(n),p_2_or_more,'r--',label='P(2 or more)')
plt.plot(range(n),p_3_or_more,'b--',label='P(3 or more)')
plt.plot(range(n),p_4_or_more,'b--',label='P(4 or more)')
plt.annotate('probability of 3 or more matches in 23 people is %0.3f'%p_3_or_more[23],xy = np.array((23,p_3_or_more[23])),xytext = (20,-0.1),arrowprops = dict(facecolor='black',shrink=0.05))
plt.annotate('probability of 3 or more matches in 88 people is %0.3f'%p_3_or_more[88],xy = np.array((88,p_3_or_more[88])),xytext = (75,0.65),arrowprops = dict(facecolor='black',shrink=0.05),wrap = True)
plt.legend()
plt.axis([0,n,-0.2,1])
plt.show()
