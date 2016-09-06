from random import randint

def prompts():
	for i in range(1, 11):
		score = randint(60, 100)
		if score >= 90 and score <= 100:
			print "Score: " + str(score) + "; Your grade is A" 
		elif score >= 80 and score <= 89: 
			print "Score: " + str(score) + "; Your grade is B" 
		elif score >= 70 and score <= 79:
			print "Score: " + str(score) + "; Your grade is C" 
		elif score >= 60 and score <= 69:
			print "Score: " + str(score) + "; Your grade is D" 

prompts()	
