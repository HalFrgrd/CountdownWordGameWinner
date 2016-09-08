'''import itertools
words = list(open('words.txt', 'r'))
print(len(words))

new_words = []
for x in words:
	if len(x) < 11:
		new_words.append(x[:-1])

new_words.sort(key=len,reverse=True)

print(new_words)
'''

import goodwords

permletters = "jauporked"


words = goodwords.goodwords

def check():
	global permletters
	counter = [0] 
	for x in words:
		ticks = 0
		letters = permletters
		temp = x
		for y in range(9):
			if letters[0] in temp:
				ticks+=1
				temp = temp[0:temp.find(letters[0])] + temp[temp.find(letters[0])+1:]


			#print(ticks,len(temp),temp,letters[0],letters)

			letters = letters[1:]

			if ticks == len(x):
				counter[0] += 1
				counter.append(x)
				
			if counter[0] == 30:
				return counter

print(check())
