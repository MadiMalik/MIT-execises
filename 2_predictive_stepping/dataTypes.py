# Assertions
# n = assert 4 > 3

# assert 4 > 3, 'four is greater than three'

# assert 4 == 3, 'it is false, cause four is not equal to 3'


# The data type used for storing and manipulating text data

# string length
# print(len(""))
# print(len(" "))
# print(len("Madiha Malikzada"))

# indexed access
print("abc"[-1])
print("abc"[1])
print("abc"[0])

# ---- string methods -------
print("HELLO".lower())
print("hello".upper())

print("h" in "madiha" ) #true
print("z" in "madiha" ) #false

print("m#a#d#i#h#a".replace("#", "")) # madiha

# remove spaces from the beggining and the end of the str
print("         Muqtader is kind           ".strip())

str = "Muqtader is kind"
# finds the index of the charecter
print(str.find("M"))
print(str.find("k"))
print(str.find(" "))

# getting a sub string by index
print(str[:4]) # Muqt
print(str[4:]) # ader is kind
print(str[9:]) # is kind
print(str[:9]) # Muqtader


print(str[9:11]) # is
print(str[12:16]) # kind
print(str[12:12]) # ''
print(str[-4:-2]) # ''


# Variables

# assign name 
name = "Madiha"

#read name 
print(name )

# assign exclaim 
exclaim = "!"

#  read: name, exclaim 
# assign: name
name = name + exclaim

#  read name
print(name)

# cannot read a variable before assigning it 
# print(pooop) # NameError: name 'noop' is not defined


# lists 
letters = ['b', 'c']

#  add an item to the beginning of the list 
letters.append('d')
print(letters) # ['b', 'c', 'd']

# add an item to the beginning of the list
letters.insert(0, 'a')
print(letters) # ['a', 'b', 'c', 'd']

# get the length of a list
len(letters) # 4

# get a specific letter by it's index
letters[0] # 'a'
letters[1] # 'b

# slice a part of the list to a new list
letters[1:3] # ['b', 'c']

# While Loops
# Repeat a block of code as long as an expression evaluates to true.

# while an_expression:
#    print('still looping') # executed each time the expression is evaluated to True

# next line after the loop

# For-In Loops
#  Iterate over a string or list, executing the loop body once for each character or item.

for char in str:
    print(char) #  'M' -> 'u' -> 'q' -> 'd'....

numbers = [1, 2, 3, 4,5] 

for number in numbers: 
    print(number)  # 1 -> 2 -> 3 -> 4 -> 5


# Functions
""" Wrap useful lines of code in a function so you can write them in one place and reuse as many times as you want."""

# --- function declaration ---
def add(x, y):
    sum = x + y
    return sum

# --- call the function and save the result to a variable ---
seven = add(3, 4)
print(seven) # 7

eight = add(2, 6)
print(eight) # 8

# Pass
# pass allows you to write the control flow structure of a program before writing all of the logic. Without using pass, Python throws a syntax error if a block is empty.
an_expression = 7 > 9
expression_1= 7 > 9
expression_2 = 7 > 9

if an_expression:
  pass

if expression_1:
  pass
elif expression_2:
  pass
else:
  pass

while an_expression:
  pass

for char in 'a string':
  pass

for item in []:
  pass

def funky():
  pass