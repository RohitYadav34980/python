# operations in tuple
# first convert the tuple in list
tup2 = (1, 2, 3, 4, 5, 6, 7, 8)

tuple1 = list(tup2)

print(type(tuple1))

# now we can do operations in tuple1 list
# and after operation we can again change it into tuple
tuple1.append(3)  # add an item in the last of the list

tuple1.pop(3)  # remove the item that is at index '3'

print(tuple1)

tup2 = tuple(tuple1)

print(type(tup2))

print(tup2.count(1))  # give the number that much time '1' occurs in the list

print(tup2.index(1))  # give the index of value '1' in the list # give the first index of occurrence of '1'
# to get the value of index in a specifc group
x = tup2.index(2, 1,7)  # we can use this format in which firstly it will slice the tuple like list and the return the index
# to find the length of tuple we can use len() function
length = len(tup2)
print(length)