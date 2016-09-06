from random import randint

def coin_toss():
	i = 0 
	count_head = 0
	count_tail = 0
	while i < 5001:
		coin = randint(0,1)
		if coin == 0:
			count_head += 1
			print "Attemp #" + str(i) + " Throwing a coin... It's a head!... Got " + str(count_head) + " head(s) so far and " + str(count_tail) + " tail(s) so far" 
		elif coin == 1:
			count_tail += 1
			print "Attemp #" + str(i) + " Throwing a coin... It's a tail!... Got " + str(count_head) + " head(s) so far and " + str(count_tail) + " tail(s) so far" 
		i += 1
	print "Ending the program, thank you!"

coin_toss()