def names(arr):
	i = 0
	while i < len(arr):
		print " ".join(arr[i].values())
		i += 1

arr = [ 
	{'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
names(arr)