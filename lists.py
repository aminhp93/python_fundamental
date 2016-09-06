fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetabels = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetabels
print fruits_and_vegetables
salad = 3 * vegetabels
print salad

drawer = ['documents', 'envelopes', 'pens']
print drawer[0]
print drawer[1]
print drawer[2]

x = [1,2,3,4,5]
x.append(99)
print x

x = [1,2,3,4,5]
x.insert(2,99)
print x

x = [1,2,3,4,5]
x.remove(3)
print x

x = [1,2,3,4,5]
x.pop()
print x
y = [10,11,12,13,14,15]
y.pop(1)
print y

x = [99,4,2,5,-3]
x.sort()
print x

x = [99, 4,2,5,-3]
print x[:]
print x[1:]
print x[:4]
print x[2:4]

my_list = [1, 'Zen', 'hi']
print len(my_list)

my_list = [1,7,3]
print max(my_list)

my_list = [1,7,3]
print min(my_list)

my_list = [0, 'hi', '']
print any(my_list)
my_list = [0, '']
print any(my_list)

my_list = [0, 'Zen', '']
print all(my_list)
my_list = [4, 'hi']
print all(my_list)























