
import datetime
from random import randint

def create_arr():
	arr = []
	for i in range(1, 10001):
		arr.append(randint(1,10000))
	return arr

t1 = datetime.datetime.today()

def bubble_sort(arr):
	i = 0 
	while i < len(arr):
		j = 0
		while j < len(arr) - i - 1:
			if arr[j] > arr[j + 1]:
				temp = arr[j]
				arr[j] = arr[j + 1]
				arr[j + 1] = temp
			j += 1
		i += 1
	return arr

arr = create_arr()
print bubble_sort(arr)
t2 = datetime.datetime.today()
print (t2 - t1)