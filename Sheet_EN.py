# DATA SCIENCE CHEAT SHEET - English


# s - A Python string variable
# i - A python integer variable
# f - A python float variable
# l - A Python list variable
# d - A Python dictionary variable

# LISTS
l.pop(3) # Returns the fourth item from l and deletes it from the list
l.remove(x) # Removes the fist item in l that is equals to x
l.reverse() # Reverses the order in the items in l
l[1::2] # Returns every seconde item from l, commencing from the 1st item
l[-5] # Returns the last 5 items from l specific axis

# STRINGS
s.lower() # Returns a lowercase version of s
s.title() # Returns s with the first letter of every word capitalized
"23".zfill(4) # Returns "0023" by left-filling the string with 0's to make it's lenght 4
s.splitlines() # Returns a list by splitting the string on any newline characters
s[:5] # Returns the first 5 characters of s
"fri" + "end" # Returns "friend"
"end" in s # Returns True if the substring "end" is found in s

# RANGE - Range objects are useful for creating sequences of integers for looping.
range(5) # Returns a sequence from 0 to 4
range(2000, 2018) # Returns a sequence from 2000 to 2017
range(0, 11, 2) # Returns a sequence from 0 to 10 with each item incrementing by 2
range(0, -10, -1) # Returns a sequence from 0 to #9
list(range(5)) # Returns a list fro 0 to 4

# DICTIONARIES
max(d, key = d.get) # Returns the key that corresponds to the largest value in d
min(d, key = d.get) # Returns the key that corresponds to the lowest value in d

# SETS
mv_set = set(l) # Returns a set object containing the unique values from l
len(my_set) # Returns the number of objects in my_set or the number of unique values from l
a in my_set # Returns True if tho value a in my_set

# REGULAR EXPRESSIONS
import re # Imports the regular expressions module
re.search("abc", s) # Returns a mathch object if the regex "abc" is found in s, otherwise None
re.sub("abc", "xyz", s) # Returns a string where all instances matching regex "abc" are replaced by "xyz"

# LIST COMPREHENSION - A one#line expression for a loop
[i ** 2 for i in range(10)] # Returns a list of the squares of values from 0 to 9
[s.lower() for s in l_strings] # Returns the list l_strings, with each item having the .lower() method applied
[i for i in l_floats if i < O.5] # Returns the items from l_floats that are less than 0.5

# FUNCTION FOR LOOPING
for i, value in enumerate(1): # Iterates over the list l, printing the index location of each item and its value
	print("The value of item {} is {}", format(i, value))
for one, two in zip(l_one, l_two): # Iterates over 2 lists, l_one and l_two and print each value
	print("one: {}, two: {}", format(one, two))
while x < 10: # Runs the code in the body for a loop until the value of x in no longer less than 10
	x += 1

# DATETIME
import datetime as dt # Imports the datetime module
now = dt.datetime.now() # Assigns datetime object representing the current time to now
wks4 = dt.datetime.timedelta(weeks = 4) # Assigns a timedelta object representing a timespan of 4 weeks to wks4
now - wks4 # Returns a datetime objectrepresenting the time 4 weeks prior to now
newyear_2020 = dt.datetime(year = 2020, month = 12, day = 31) # Assigns a datetime object representing December 25, 2020 to newyear_2020
newyear_2020.strftime("%A, %b %d, %Y") # Returns "Thursday, Dec 31, 2020"
dt.datetime.strptime('Dec 31, 2020', "%b %d, %Y") # Returns a datetime object representing December 31, 2020

# RANDOM
import random # Imports the random module
random.random() # Returns a random floatbetween 0.0 and 1.0
random.randint(0, 10) # Returns a random integer between 0 and 10
random.choice(l) # Returns a random item from the list l

# COUNTER
from collections import Counter # Imports the Counter class
c = Counter(l) # Assigns a Counter (dict#like) object with the counts of each unique item from 1 to c
c.most_common(3) # Returns the 3 most common items from l

# TRY/EXCEPT - Catch deal with errors
l_ints = [1, 2, 3, "", 5] # Assigns a list of integers with one missing value to l_ints
l_floats = [] # Converts each value of l_intsto a float, catching and handling ValueError : could not convert string to float : where values are missing
for i in l_ints:
	try:
		l_floats.append(float(i))
	except:
		l_floats.append(i)
