

# Lists

foodsThatStartWith_Q = ["quince", "quiche", "quahog"]

upTo10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# String --> List using .split()

letterList = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

wordList = "world, earth, water, life, art, periodic table of elements".split(",")


# List Comprehension

A = [0, 1, 2, 3, 4]

B = [x for x in range(5)]

C = [(2*x + 11) for x in range(5)]


# Length of a list

len(upTo10)

len(letterList)


# Add an item to a list

cities = ["singapore", "toronto", "rome", "cairo"]

cities.append("london")

cities.insert(2, "tokyo")


# Item at Index
colors = ["red", "blue", "green"]

colors[1]  # --> blue

colors[0]  # --> red

colors[-1] # --> green


# Count a specific item

myList = ["a","b","c","a","a","c","d","a","c","b"]

myList.count("a")
myList.count("b")



################################################################
################################################################

#1) Given a list of numbers,
#   --- define a function that returns the largest integer in the list.
#   --- define a function that returns the total sum of all the integers in the list.
#   --- define a function that returns a list of only the even numbers from the list.
#   --- define a function that returns a list of the numbers divisible by 3.

numList = [13, 3, 18, 24, 94, 75, 59, 41, 35]




#2) Given a list of strings,
#   --- define a function that returns a list of the strings that start with "b".
#   --- define a function that returns a list of the strings that are 5 characters in length.
#   --- define a function that returns a list of the strings that don't contain the letter "e" or "E".

wordList = ["blue", "orange", "brown", "white", "black", "yellow", "red", "green"]



#3) Use List Comprehension to produce the following output list
#   --- every odd number between 1 to 20. --> output = [1,3,5,7,9,11,13,15,17,19]
#   --- represents f(x) = x^2 for range of -3 to 3. --> output = [9,4,1,0,1,4,9]







