# IF STATEMENTS
#
# In this problem, write a function named "lossy_transform" that takes an
# integer parameter and returns the corresponding value found in this table
# | Input                                          | Output                 |
# |------------------------------------------------|------------------------|
# | Less than 10                                   | 0                      |
# | Greater than or equal to 10 and less than 47   | The input times 2      |
# | Greater than or equal to 47 and less than 1001 | The input divided by 3 |
# | Greater than or equal to 1001                  | None                   |
#
# That last output is the literal None, not a string.
#
# Your code must include at least one of each of the following keywords:
# * if
# * elif
# * else
#
# All inputs are guaranteed to be greater than 0.
#
# There are four sample data calls for you to use.

#______________________________YOUR CODE BELOW______________________________#

# Your code here
def lossy_transform(i):
    if i < 10:
        return 0
    elif i >= 10 and i < 47:
        return i * 2
    elif i >= 47 and i < 1001:
        return i / 3
    elif i >= 1001:
        return None

# __________SAMPLE TEST DATA__________ #
print(lossy_transform(8))     # > 0
print(lossy_transform(33))    # > 66
print(lossy_transform(99))    # > 33
print(lossy_transform(1002))  # > None
