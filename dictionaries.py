#delcaring an empty dictionary
dictionary = dict()

#adding keys and values to the dictionary
#dictionary[<key>] = <value>
dictionary[1] = "a"
dictionary[2] = "b"
dictionary[3] = 100
dictionary[4] = ('alpha', 'beta')
print(dictionary)

#printing value in a dictionary from a given key
print(dictionary[1])

#deleting a key-value pair by specifying the key
del dictionary[1]
print(dictionary)

#can also use .pop to remove a value
dictionary[1] = "a"
print(dictionary)
dictionary.pop(1)
print(dictionary)

#changing a key's value
dictionary[2] = "B"
print(dictionary)

#use .update to update values in a dictionary
dictionary.update({4: ('gamma', 'theta')})
print(dictionary)

#mathematical operation on value
dictionary[3] = dictionary[3] + 100
print(dictionary)

#dictionary's length
length = len(dictionary)
print(length)

#the .keys() method returns the keys of the dictionary
print(dictionary.keys())
print(list(dictionary.keys())) #print as a list
for i in dictionary.keys():
    print("Key", i, "maps to", dictionary[i])

#the .values() method returns the values of the dictionary
print(dictionary.values())
print(list(dictionary.values())) #print as a list

#the .items method returns all entries in the dictionary as tuples (<key>, <values>)
print(dictionary.items())
print(list(dictionary.values())) #print as a list
for (key, value) in dictionary.items():
    print("Key", key, "maps to", value)

#use in and not in to determine whether a key is in the dictionary
print(1 in dictionary)
print(1 not in dictionary)
print(4 in dictionary)
print(4 not in dictionary)

#.get outputs the values of the specified key. Outputs something else if key is not found
print(dictionary.get(4))
print(dictionary.get(1, "Not found"))
