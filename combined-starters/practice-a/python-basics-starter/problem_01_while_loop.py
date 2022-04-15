# WHILE LOOP
#
# In this problem, write a function named "my_while_loop" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are longer than five characters. The function must use
# a while loop in its implementation.
#
# There are two sample data calls for you to use.

#______________________________YOUR CODE BELOW______________________________#

# Your code here
def my_while_loop(arr):
  newList = []
  i = 0
  while i < len(arr):
    word = arr[i]
    if len(word) > 5:
      newList.append(word)
    i+=1
  return newList

# __________SAMPLE TEST DATA__________ #
test = ["nope", "yes this one", "not", "uhuh", "here's one", "narp"]
print(my_while_loop(test))  # > ["yes this one", "here's one"]

test = ["plop", "", "drop", "zop", "stop"]
print(my_while_loop(test))  # > []

test = []
print(my_while_loop(test))  # > []
