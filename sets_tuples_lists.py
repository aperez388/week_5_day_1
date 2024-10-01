# collection = single variable used to store multiple values
#  List  = [] ordered and changeable. Duplicates OK
#  Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#  Tuple = () ordered and unchangeable. Duplicated OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut", "kiwi", "watermelon", "mango", "blueberry"]

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

# print(fruits.index("apple"))

# for fruit in fruits:
#     print(fruit)

# cars = ["Ford", "Volvo", "BMW"]
# Add 4 new cars in the list
# cars.append("Honda")
# # print out the list of cars in an f-string that says "The cars in the list are:"
# print(f"The cars in the list are: {cars}")
# # Replace the last element in the list with another car
# cars[-1] = "Aston Martin"
# print(cars)
# # Replace the 3rd element in the list with another car
# # Print out the list of cars in an f-string
# cars[2] = "Nissan"
# print(f"The cars in the list are: {cars}")
# # insert a new car in the 2nd position
# # print out the list of cars in an f-string
# cars.insert(0, "KIA")
# print(f"The cars in the list are {cars}")
# # remove the 3rd element in the list
# # print out the list of cars in an f-string
# cars.remove("Volvo")
# print(f"The cars in the list are: {cars}")
# #check if the list contains the car "Ford"
# # print out the result in an f-string
# print("Ford" in cars)

# for car in cars:
#     requestCar = input("Enter a car: ")
#     cars.append(requestCar)
#     print(f'The cars in the list are: {cars}')
#     if len(cars) >= 10:
#         print("You have reached the maximum number of cars.")
#         break

# # challenge
# #create a list of friends
# friends = ["Vikshay"]
# # add 4 new friends in the list
# for friend in friends:
#     requestFriend = input("Enter the name of a friend: ")
#     friends.append(requestFriend)
#     if len(friends) >= 5:
#         print("You have reached the maximum number of friends.")
#         break
# # print out the list of friends in an f-string
# print(f"Your friends are: {friends}")
# # replace the last element in the list with another friend
# friends[-1] = "Sally"
# # print out the list of friends in an f-string
# print(f"Your friends are: {friends}")
# # insert a new friend in the 2nd position
# friends.insert(2, "Hayden")
# # print out the list of friends in an f-string
# print(f'Your friends are: {friends}')

#######################sets#############################################
# sets are unordered and unindexed
# they are defined using curly brackets
# they do not allow duplicates
# fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# print(fruits)
# print(dir(fruits)) methods/attributes that can be used with sets
# print(help(fruits)) # documentation/methods that can be used with sets
# print(len(fruits)) # number of elements in the set
# print("volvo" in fruits) # Check if an element is in the set
#add element to the set
# print(fruits.add("orange"))
# print(fruits.add("kiwi"))
# print(fruits.add("dragonfruit"))
# print(fruits.add("blueberry"))
# add multiple elements to a set
# print(fruits.update(["orange", "kiwi", "pineapple"]))
# print(fruits)
#remove an element from the set
# print(fruits.remove("banana"))
# print(fruits)
# print(fruits.pop()) #removes the last element in the set
# print(fruits)
# print(fruits.clear()) # clears the set
# print(fruits)
# when do we want to use sets?
# sets are useful when you want to store a collection of items that should not be changed, and you do not care about the order of the items.
#example: a collection of unique items
# social_security_numbers = {123456789, 987654321, 123654789}
# print(social_security_numbers)
#remove the last element in this set
# add another social security number
# print(social_security_numbers.pop())
# print(social_security_numbers)
# print(social_security_numbers.add(345678129))
# print(social_security_numbers)
# print(social_security_numbers.add(50289977))
# print(social_security_numbers)

##################tupples###############################################
 # tuples are immutable and are defined using parenthesis
# Create a tuple called my_tuple with the following values:
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(example_tuple)
# print(example_tuple.count(2)) # count the number of times the value of 2 appears in the tuple
# print(dir(example_tuple)) # attributes that can be used with tuples
# print(help(example_tuple)) # documentation/methods that can be used with tuples
# print(len(example_tuple)) # number of elements in the tuple
# print(2 in example_tuple) # check if an element is in the tuple
#when are they useful?
# Tuples are useful when you want to store a collection of items that should not be changed, such as days of the week, months of a year, etc. If you want to find the index of a value in a tuple
# print(example_tuple.index(2))
# lymeric = "Peter piper picked a peck of pickled peppers peppers"
#convert the string to a tuple
#split it first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
#find how many times the letter "p" appears in the tuple
# print(lymeric_tuple.count("peppers"))

# loops with tupples
for item in example_tuple:
    print(item)

########################dictionaries###################################

# Dictionaries are unordered, changeable and indexed. They are defined usin=g curly brackets. They have keys and values. A collection of {key:value} pairs, no duplicates. Keys are unique. 
# Values can be of any data type
capitals = {"Kenya":"Nairobi",
            "Uganda":"Kampala",
            "Tanzania":"Dodoma",
            "Rwanda":"Kigali",
            "China":"Beijing",
            "USA":"Washington DC"}
print(capitals)
# print(dir(capitals)) # attributes that can be used with dictionaries
# print(help(capitals)) #documentation/methods that can be used with dictionaries
# print(len(capitals))#number of items in a dictionary
#if you want to check the value of a key in the dictionary
print(capitals["Kenya"])
print(capitals.get("Kenya"))
# add an item ti the dictionary #two ways
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
# add three more countries and their capitals to the dictionary
capitals.update({"Mexico":"CDMX", "Egypt":"Cairo", "UK":"London"})
print(capitals)

capitals.pop("China") # remove an item from the dictionary
print(capitals)
# clear the dictionary
# capitals.clear() # do not run this
# loop through the dictionary
for key in capitals:
    print(f"these are the {key}")

for value in capitals.values():
    print(value)

# print the key value pairs in the dictionary
items_all = capitals.items() # key value pairs
for key, value in items_all:
    print(f"{key} is the capital of {value}")