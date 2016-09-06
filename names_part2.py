def names(users):

		j = 0
		while j < len(users.values()):
			arr1 = users.values()[j]
			arr2 = users.keys()[j]
			print arr2

			k = 0
			while k < len(arr1):
				name = " ".join(arr1[k].values())
				
				count = 0
				for i in name:
					if i != " ":
						count += 1
				print str(k+1) + " - " + name + " - " + str(count)
				k += 1
			j += 1
	


users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
names(users)