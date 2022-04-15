# FOR LOOP
#
# In this problem, write a function named "my_for_loop" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are longer than five characters. The function must use
# a for loop in its implementation.
#
# There are two sample data calls for you to use.

#______________________________YOUR CODE BELOW______________________________#

# Your code here
def my_for_loop(arr):
    newArr = []
    for word in arr:
        if len(word) > 5:
            newArr.append(word)
    return newArr  # must return the new arr separately

# __________SAMPLE TEST DATA__________ #
test = ["nope", "yes this one", "not", "uhuh", "here's one", "narp"]
print(my_for_loop(test))  # > ["yes this one", "here's one"]

test = ["plop", "", "drop", "zop", "stop"]
print(my_for_loop(test))  # > []

test = []
print(my_for_loop(test))  # > []
