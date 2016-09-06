def draw_star(arr):
	i = 0 
	while i < len(arr):
		if type(arr[i]) == int:
			print arr[i] * "*"
		elif type(arr[i]) == str:
			letter = arr[i][0] * len(arr[i])
			print letter.lower()
		i += 1

draw_star([1,4,5,"dsfasdf", 3,2])

