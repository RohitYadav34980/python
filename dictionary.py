dict = {
    "name": "Rohit",  # here 'name' is 'key' and 'rohit' is 'value'
    "age": 17
}

# remember if you want to excess the dict you such use it like
# dict["age"/"name"]
print(dict["name"])
print(dict["age"])

# if you want to print whole dict you can directly print it
print(dict)
# we can also use get function
print(dict.get("name2"))  # it will give none but if we print the key name2 directy will get error
# to print all the keys we use dictname.keys()
# to print all the values we use dictname.values()
print(dict.keys())
print(dict.values())

# we can print all the values correponding to keys one by one by for loop
# we mainy use this thing to take it in fstring
for key in dict:
    print(f"the value corresponding to {key} is {dict[key]}")

# the below code will print all dict items
print(dict.items())
for key, value in dict.items():
    print(f"the key corresponding to {key} is {value}")

print(
    '------------------------------------------------------------------------------------------------------------------------------------------------------------')

# method in dictaniory

ep = {1: 10, 2: 20, 3: 30, 4: 40}
ep1 = {"name": "John", "age": 19}

# the update function is used to add the value of one dict to another
ep.update(ep1)  # this means that ep will get updated(means ep2 will be added to ep)
print(ep)

# we use clear function to clear the dictionary and make it empty dictionary
# ep.clear()
# print(ep)

# we can use pop function to remove a key value pair from the dictionary
ep.pop(1)
print(ep)
# to remove the last pair of key and value we use popitem function
ep.popitem()
print(ep)

# to delete whole dictionary we can use del function
del ep1
# print(ep1)#this will give an error

# in del function you can provide key to only delete that key from the dictionary
del ep[2]
print(ep)
