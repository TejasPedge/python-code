# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"




def Add(key, value) :
    dictionary[key] = value

def update(key, value) :
    if(key in dictionary) :
        dictionary[key] = value

def Delete(key) :
    if(key in dictionary) :
        del dictionary[key]


dictionary = {}

Add("john",25)
print(dictionary)

update("john",26)
print(dictionary)

Delete("john")
print(dictionary)