# CLASS DECLARATION
#
# Declare a class named "Airport" with the following features:
#
# * A constructor that takes two values: a name and an abbreviation
# * A method named "number_of_planes" that returns the number of planes parked
#   at the airport. That number should be 0 when the object is first created.
# * A method named "plane_arrives" that increases the number of planes parked
#   at the airport by 1.
# * A method named "plane_departs" that decreases the number of planes parked
#   at the airport by 1
# * A method named "get_number_of_planes" that returns the current number of
#   planes parked at the airport
# * A method named "__repr__" that returns a string with the following format:
#     "<{airport abbreviation} {number of planes at the airport}"
#   An example would be
#     "<LAX 12>"

#______________________________YOUR CODE BELOW______________________________#

# Your code here
class Airport:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.planes = 0

    def number_of_planes(self):
        self.planes = 0

    def plane_arrives(self):
        self.planes += 1

    def get_number_of_planes(self):
        self.planes -= 1

    def __repr__(self):
        return f'{self.abbreviation} {number_of_planes}'
