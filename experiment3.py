# 3. Write a program having a parameterised function that returns True or False 
# depending on whether the parameter passed is even or odd.

def is_even(num):
    return num % 2 == 0

# Test the function
number = int(input("Enter a number: "))
if is_even(number):
    print("True (Even)")
else:
    print("False (Odd)")
