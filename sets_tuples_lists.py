# collection = single variable used to store multiple values
#  List  = [] ordered and changeable. Duplicates OK
#  Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#  Tuple = () ordered and unchangeable. Duplicated OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "kiwi", "watermelon", "mango", "blueberry"]

# print(fruits[2:]) 
# # index of 0 = apple, 1 = orange and so forth. Index of 4 gives you an error
# # Each value in a collection is also known as an element
# # second spot left empty just gives you the last element of the list
# print(fruits[::2]) # Gives you every second element beginning from index = 0.
# print(fruits[::-1]) # Gives you the list but with the elements' positions reversed.
# print(len(fruits)) # Gives you the length of your list.\

# Iteration: It loops through the entie list, set or collection and does something with each one. One of the hardest things to get for beginner programmers.
# I am going to assign a variable that will take the place of each element in the list.

#for fruit in fruits:
    #print(fruit)

# Every time that he goes through the list right here in this iteration, fruit is going to take the place of every last variable in here. It will go through the collection as many times as there are elements and fruit will equal apple, fruit will equal orange, fruit will equal banana and so forth. 

# print(dir(fruits)) # Gives you all of the attributes for the list.

# print(help(fruits)) # Gives you a little manual for all the stuff that you can do with the list now. Gives you all of the helpful documentation for what each part does.

# print(len(fruits)) # Gives you the length.

# print("apple" in fruits) # Returns a boolean and tells you if whether or not this value is in your list; True or False

# print("dragonfruit" in fruits)

# fruits[0] = "pineapple" # Changes the value of the fist element
# fruits[2] = "starfruit" # Changes the value of the third element
# fruits[-1] = "strawberry" # Changes the value of the last element

# fruits.append("pineapple") # Adds an element to the end of the list.
# fruits.append("tomato")
# fruits.append("grape")

# fruits.remove("coconut") # Removes an element from a list.

# fruits.insert(0, "pineapple") # Puts something right there in the middle--this specific spot--and pushing everything over. Does not replace.

# fruits.sort() # Puts everything in alphabetical order.

# fruits.reverse() # Reverses the list based on the order that we placed them. If you want reverse alphabetical order, you can first sort and then reverse the list.

# fruits.clear() # Removes everything from a list.

print(fruits.index("apple"))

for fruit in fruits:
    print(fruit)