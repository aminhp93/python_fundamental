for count in range(0,5):
	print "looping - ", count

my_list = [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world']
for element in my_list:
	print element

count = 0 
while count < 5:
	print "looping - ", count
	count += 1

for val in "string":
	if val == "i":
		break
	print(val)

for val in "string":
	if val == "i":
		continue
	print(val)

class EmptyClass:
	pass

x = 3
y = x
while y > 0:
	print y
	y -= 1
else: 
	print "Final else statement"

x = 3
y = x
while y > 0:
	print y
	y -= 1
	if y == 0:
		break
else:
	print "final else statement"