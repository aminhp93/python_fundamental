weekend = {"Sun": "Sunday", "Mon": "Monday"}
capitals = {}
capitals["svk"] = "Bratislava"
capitals["due"] = "Berlin"
capitals["dnk"] = "Copenhagen"


d = {i: object() for i in range(4)}
print d
for data in capitals:
	print data
for key in weekend.iterkeys():
	print key

# print cmp(weekend, vals)
# vals = vals.clear()
# print vals
vals = dict(one=1, two=2, three=3)

vals = vals.copy()
print vals
weekend = weekend.copy()
print weekend

