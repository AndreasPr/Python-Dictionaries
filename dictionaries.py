# Dictionaries are a collection data type which are Unordered, Mutable and it consist of Key-Value pairs

mydictionary = {"name": "Andreas", "state": "New York", "age": 23}
print(mydictionary)

mydictionary2 = dict(name="Andreas", state="New York", age=23)
print(mydictionary2)

#--------------------------------------------------------Access elements-----------------
value = mydictionary["name"]
print(value)

#------------------------------------------------ -------Add key-value pairs--------------
mydictionary["country"] = "USA"
print(mydictionary)

# -------------------------------------------------------Delete key-value pairs----------
#First way:
del mydictionary["age"]
print(mydictionary)

#Second way:
# Using the pop method to delete elements
mydictionary.pop("name")
print(mydictionary)

#Third way:
# In Python 3.7, remove the last inserted key-pair item with the methood popitem
mydictionary.popitem()
print(mydictionary)

#--------------------------------------------------------Check if a key exists in dictionary----------------------
mydictionary3 = {"name": "John", "age": 56, "phone-number": 1234567890} 

#First way:
if "name" in mydictionary3:
    print(mydictionary3["name"])

#Second way:
try:
    print(mydictionary3["name"])
except:
    print("Error")

#---------------------------------------------------------Loop in Dictionary----------------------------
#Iterate the keys:
for key in mydictionary3.keys():
    print(key)

#Iterate the values:
for value in mydictionary3.values():
    print(value)

#Loop for keys and values at the same time:
for key, value in mydictionary3.items():
    print(key,":",value)

#---------------------------------------------------------Copying a Dictionary--------------------
mydictionary_org = {"name": "Mike", "state": "TX", "age": 56}

mydictionary_copy = mydictionary_org
print(mydictionary_copy)

# If I modify the copy, I modify and the original one in the above case of assignment
mydictionary_copy["country"] = "France"
print(mydictionary_copy)
print(mydictionary_org)

#To build an actual copy:
mydictionary_copy2 = mydictionary_org.copy()
#OR
# mydictionary_copy2 = dict(mydictionary_org)

mydictionary_copy2["country"] = "Germany"
print(mydictionary_copy2)
print(mydictionary_org)


#---------------------------------------------------------Merge Dictionaries----------------------------
dictionary_merge1 = {"name": "George", "age": 90, "email": "george45@gmail.com"}
dictionary_merge2 = dict(name="Michelle", age=67, city="Manhattan")

dictionary_merge1.update(dictionary_merge2)
print(dictionary_merge1) #{'name': 'Michelle', 'age': 67, 'email': 'george45@gmail.com', 'city': 'Manhattan'}

#---------------------------------------------------------Types of keys-------------------------
mydictionary5 = {3:5, 4:9, 2:8}
print(mydictionary5)

#Access the values with the actual key:
value = mydictionary5[4]
print(value)

#---------------------------------------------------------Use of Tuples-------------------------------
mydictionary6 = {3:5, 4:9, 2:8}
print(mydictionary6)

#Using tuple as the key of the dictionary 
mytuple = (8,5)
mydictionary6 = {mytuple: 45}
print(mydictionary6)

#DON'T USE THE LIST, because List is mutable, so can be changed after the creation, therefore it is not hashable and CANNOT be used as a key
