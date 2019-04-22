

# Learn about Strings

# Declare a string

word = "WAFFLE"

randomWord = random.choice(['cat', 'stomach', 'pancake', 'prairie'])

sentence = "my uncle's favorite phrase is 'strong dynamic moves'"


# Capitalize
sentence.capitalize()

# Upper
randomWord.upper()

# Lower
word.lower()

# Count
word.count("F")
word.count("W")
randomWord.count("o")

# Find
word.find("L")
sentence.find("u")

# Reverse Find
word.rfind("F")
sentence.rfind("y")

# Replace
word.replace("F", "Z")
randomWord.replace("a", "A")

# Index
word.index("A")
sentence.index("p")

# Letter at Index
word[3]
randomWord[-1]
sentence[-3]

# Index All
bucket = []
i = 0
for char in word:
    if char == "t":
        bucket.append(i)
    i += 1

######################################################################

# Problem Set
#1) For each variable below, assign it to a value.
# For Example
# --- city = "Minneapolis"
# --- fruit = "apple"

vegetable =

animal =

quote = 


#2) Define a function that capitalizes only the last letter in a word.
# For example
# --- capLast("Waffle") --> "wafflE"
# --- capLast("happy BIRTHDAY") --> "happy birthdaY"



#3) Define a function that will search a word for a specific letter.
#   When it finds the letter, the index of the letter is stored in a list.
# For example
# --- findAll("mississippi river", "s") ---> [2,3,5,6]
# --- findAll("mississippi river", "i") ---> [1,4,7,10,13]



#4) Define a function that is equivalent to the method "count".
#   Use a for-loop and if-statement count how many times a specific
#   letter occurs in a word.



#5) Define a function that replaces all occurrances of a specific letter with
#   the "$" symbol.
# For Example
# --- replaceItWith(word, letter, symbol)
# --- replaceItWith("waffle", "a", "$") ---> w$ffle
# --- replaceItWith("minivan", "i", "_") ---> m_n_van


#6) Define a function that rearranges the letters in a word and jumbles the word.
# For Example
# --- jumble(word)
# --- jumble("river") ---> verir


