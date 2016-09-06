julia = ("Julia", "Robers", 1967, "Dubli", 2009, "Actress", "Atlanta")

print julia[2]

for data in julia:
	print data

# julia[0] = "X"
julia = julia + ("fasf ", 230)
print julia
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]

value = ("Michael", "Instructor", "Coding Dojo")
(name, position, company) = value
print name
print position
print company
am = (a, b, c, d) = (1,2,3,4)
print am

tuple_data = ('physics', 'chemistry', 1997, 2000)
print len(tuple_data)
print max(tuple_data)
print min(tuple_data)

num = (1,4,5,6,7)
for index, item in enumerate(num):
	print (str(index) + "=" + str(item))

print tuple(reversed(num))

