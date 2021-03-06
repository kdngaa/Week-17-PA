# LIST COMPREHENSION
#
# In this problem, write a function named "my_comprehension" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are longer than five characters. The function must use
# a list comprehension in its implementation. Your function body must contain
# only one line.
#
# There are two sample data calls for you to use.

#______________________________YOUR CODE BELOW______________________________#

# Your code here
def my_comprehension(arr):
  return [word for word in arr if len(word) > 5]

# __________SAMPLE TEST DATA__________ #
test = ["nope", "yes this one", "not", "uhuh", "here's one", "narp"]
print(my_comprehension(test))  # > ["yes this one", "here's one"]

test = ["plop", "", "drop", "zop", "stop"]
print(my_comprehension(test))  # > []

test = []
print(my_comprehension(test))  # > []
