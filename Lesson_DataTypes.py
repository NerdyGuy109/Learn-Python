


#---------------------------------------
#---------------------------------------
#---------------------------------------
# Data Types

#--- string
#--- multiline string
#--- integer
#--- float
#--- boolean
#--- list
#--- tuple
#--- dictionary
#--- loop
#--- conditional (if/else)
#--- function
#--- classes

#---------------------------------------
#---------------------------------------
#---------------------------------------
# Assignment

# 1) Declare the following
#    ----- a list of words starting with the letter "M"
#    ----- a list of the vowels from the alphabet
#    ----- a list of any 3 integers between (-7 and 7)
#    ----- a dictionary for chemistry (key = atomic number, value = element name)
#
# 2) Create a function called "temperatureNow"
#    that takes one parameter "temp". The function
#    should print out "The Current Temperature is ____".
#
#
# 3) Create a class for a Vehicle.
#    Assign it properties such as color and number of wheels.
#
#    Include a method "changeColor" that will reassign the
#    color of the vehicle by passing in a parameter "color".
#
#    Include a method "checkLogic" that will use an if/else
#    statement to determine if the vehicle is:
#    --- motorcycle with 2 wheels
#    --- car with 4 wheels
#    --- semi with 18 wheels



#---------------------------------------
#---------------------------------------
#---------------------------------------
#--- string

name = "adam"


#---------------------------------------
#--- multiline string

address = """
123 Fake Street,
Springfield, MN 00100
"""

#---------------------------------------
#--- integer

age = 32


#---------------------------------------
#--- float

gravity = 9.81


#---------------------------------------
#--- boolean

isMammal = True
isFemale = False


#---------------------------------------
#--- list

myGroceries = ["eggs", "chicken", "milk"]


#---------------------------------------
#--- tuple

primes = (2, 3, 5, 7, 11)


#---------------------------------------
#--- dictionary

translate_numbers = {
    #number: [english, spanish, german]
    0: ["zero", "cero", "null"],
    1: ["one", "uno", "ein"],
    2: ["two", "dos", "zwei"]
    }

#---------------------------------------
#--- loops

for n in range(5):
    print(n)

for letter in "word":
    print(letter)

for item in ["apple", "orange", "banana"]:
    print(item)

x = 8
while (x > 0):
    print(x)
    x = x - 1


#---------------------------------------
#--- conditional (if/else)

secretNumber = 9

if secretNumber < 0:
    print("the number is negative and less than 0")
elif secretNumber > 0:
    print("the number is positive and greater than 0")
else:
    print("the number is 0")
    


#---------------------------------------
#--- function

def jumbleWord(word):
    letterList = list(word)
    used = []

    while (len(used) < len(word)):
        i = random.randrange(0, len(word))
        if i not in used:
            used.append(i)

    jumble = ""

    for index in used:
        jumble += word[index]

    print(jumble)
    

jumbleWord("jurassic")        
jumbleWord("world")
        
        
#---------------------------------------
#--- classes

class Dog:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def greeting(self):
        print("I'm a Dog, my name is %s" % self.name)

    def speak(self):
        print("Woof or Bark are acceptable")

    def eat(self, foodType):
        print("%s just ate %s" % (self.name, foodType))

    def lick(self, where):
        print("%s just licked %s" % (self.name, where))


kirby = Dog("kirby", "male")
kirby.greeting()
kirby.eat()


        

