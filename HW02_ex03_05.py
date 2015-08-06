#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body
	
			
def plus_line(n):
	str1="+"
	str2=" - - - - "
	new=n*(str1+str2)
	print (new+str1)

def pipe_line(n):
	str1="|"
	str2="         "
	new=n*(str1+str2)
	for i in range(0,4):
		print (new+str1)
		
def n_by_n(n):
	for i in range(0,n):
		plus_line(n)
		pipe_line(n)
	plus_line(n)	


# Write your functions above:
################################################################################
def main():
	"""Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
	"""
#   print("Hello World!")
	n_by_n(4)
	
    



if __name__ == "__main__":
    main()