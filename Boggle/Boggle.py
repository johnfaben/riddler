f = open('enable1.txt','r')
wordlist = []
for line in f:
    wordlist.append(line.strip())
f.close()


for word in wordlist: 
    if word in 'alphabetispaghetti':
        print word

