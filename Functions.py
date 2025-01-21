# question 1

# The len() function in Python returns the number of items in an object.
# It can be used to find the length of various data structures
# such as strings, lists, tuples, dictionaries, and sets.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length=len(numbers)
print("The Length of the list is:",length)

# question 2
def greet(name):
    print(f"hello,{name}!")

name=str(input("enter the name: "))
greet(name)

# question 3
def find_maximum(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

numbers = [5,10,11,50,100,3]
print(find_maximum(numbers))

# question 4

# Local Variables
# Local variable are defined within a function and are only accessible within that function.
# They are created when the function is called and destroyed when the function returns.
def m1():
    mess="my name is john"
    print(mess)
m1()
# local variable called outside/
# m1()
# print(mess)

# global variable
# Global variables are defined outside of any function and are accessible from anywhere in the program.
def h():
    print("hello",B) #inside
B="my name is john"
h()
print("hello",B) #outside

# question 5
def area_of_rectangle(length, width=5):
    area = length * width
    return(area)

Area_with_Width = area_of_rectangle(15,3)
print(f"The area of rectangle with length and width is {Area_with_Width} square units.")

Area_with_Default_Width = area_of_rectangle(17)
print(f"The area of rectangle with length and default width is {Area_with_Default_Width} square units.")











