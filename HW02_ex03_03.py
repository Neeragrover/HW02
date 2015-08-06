#!/usr/bin/env python
# HW02_ex03_03

# Python provides a built-in function called len that returns the length 
# of a string, so the value of len('allen') is 5.

# Write a function named right_justify that takes a string named s as a 
# parameter and prints the string with enough leading spaces so that the
# last letter of the string is in column 70 of the display.

# Example:
# >>> right_justify('allen')
#                                                                  allen
################################################################################
# Write your function below:
# Body


def right_justify(str):
#	print(str)
	length=len(str)
	num_spaces=70-length
	space=" "
	space_append=num_spaces*space
	final=space_append+str
	print final
	
 # Write your function above:
################################################################################
def main():
    """Call your functions within this function."""
    print("Hello World!")
    right_justify("Python")
    right_justify("Neera Grover")

if __name__ == "__main__":
    main()