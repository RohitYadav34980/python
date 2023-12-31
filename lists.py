l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(l)
l.append(10)  # add '10' at the last of the list
print(l)
l.sort()  # turn the list in ascending order
print(l)
l.sort(reverse=True)  # turn the list in descending order
print(l)
l.reverse()  # reverse the list
print(l)
print(l.index(1))  # give the index of value '1' in the list # give the first index of occurrence of '1'
print(l.count(1))  # give the number that much time '1' occurs in the list
"""
    m = l         #this will not make another list m which is copy of l but m is the reference of l 
    m[0] = 0      #this will not change the the value at 0 index in m but it will change the value at 0 index in l
    
    to make a copy of list we use a function ---->  l.copy()
"""
m = l.copy()
print(m)
m[0] = 0
print(m)
print(l)  # there is no change in the list l because we have done change in the new list m
l.insert(2, 10)  # this function will insert a value in the list at index '2' and the value is '10',,previously the
# value at index 2 is now at 3 ,3 at 4 so on...
# if you want to add a list at the end of other list we use a function
# __listname__.extend(__listname1__ that you want to attach)
l.extend(m)
print(l)
# if you don't want to do any change in the list you can make a new list by simply writing:-----> k = l + m
k = l + m
print(k)
