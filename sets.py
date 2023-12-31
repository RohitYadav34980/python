# sets are defined as "" name = {values} ""
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 11}
print(s)

# to make an empty set
# a ={}
# this is not a set bur it is a empty dictionary
# to make an empty set we have to write it like this -----
a = set()
print(type(a))

info = {"hello", 2, 3, True}
# to print all the elements of set 'info' we can do it by using for loop
for i in info:
    print(i)
## order is not maintained in sets


print(
    "--------------------------------------------------------------------------------------------------------------------------------")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# to find the union of 's1' and 's2'
s3 = s1.union(s2)
print(s3)
## to update s1 with s2 means s1 = s3 and s2 remains same we cane use update function
# s1.update(s2)
# print(s1,s2)

# for intersection of 's1' and 's2'
s4 = s1.intersection(s2)
print(s4)
## to update s1 with the intersection we can use this function ------
# s1.intersection_update(s2)
# print(s1,s2)

# to find the symmetric diffrence
s5 = s1.symmetric_difference(s2)
print(s5)
print('\n\n\n\n\n\n\n\n')

# s1.isdisjoint(s2) function --- the function is used to check wheather the two sets are disjoint or not if the two
# sets are disjoint it means that there is nothing common between them
print(s1.isdisjoint(s2))
# s1.issuperset(s2) function --- the function is used to check weather the set 's1 is superset of 's2'
print(s1.issuperset(s2))
# s1.issubset(s2) function --- the function is used to check weather the set 's1 is subset of 's2'
print(s1.issubset(s2))

# by simply using add function u can add an element in the set
s1.add("hello")
print(s1)

# remove and discard function - they both remove the element from set but if the element is not in set and used remove function you get an error and if you are using discard function you will not get any error
s1.remove("hello")
s1.discard("hello")#this will not give an error
# s1.remove("hello")#this will give n error

# we can use a pop function to raise an elemnt form the set
item = s1.pop()
print(item)

# del function is used to delet a whole set
# del s1
# print(s1)#will rase a error because the set is deleted

# clear function is used to clear the set not to delet the set
# s1.clear()
# print(s1)


# if you want to check wather the elements is present in the set or not we can use if loop
if 2 in s1:
    print('2 is present in the set s1')
else:
    print('2 is not present in the set s1')