#!/usr/bin/env python
# HW02_ex03_04

# A function object is a value you can assign to a variable or pass as an 
# argument. For example, do_twice is a function that takes a function object 
# as an argument and calls it twice:

# def do_twice(f):
#     f()
#     f()

# Here's an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
#     print 'spam'

# do_twice(print_spam)

# 1. Type this example into this script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value,
#  and calls the function twice, passing the value as an argument.
# 3. Write a more general version of print_spam, called print_twice, that takes a 
# string as a parameter and prints it twice.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam'
#  as an argument.
# 5. Define a new function called do_four that takes a function object and a value 
# and calls the function four times, passing the value as a parameter. There 
# should be only two statements in the body of this function, not four.
################################################################################
# Write your functions below:
# Body
#>>> def do_twice(f):
#...     f()
#...     f()
#...
# def print_spam():
#	print 'spam'

#>>> do_twice(print_spam)***
#spam
#spam

def do_twice(f,v):
	f(v)
	f(v)

def test(v):
	print v

def print_twice(string1):
	print string1
	print string1

def mod_do_twice(f,s):
	f(s)
	f(s)

def do_four(f,s):
	for i in range(0,4):
		f(s)
	

# Write your functions above:
################################################################################
def main():
   """Call your functions within this function.
   When complete have one function call in this function:
   do_four([function object], [some_value])
   """
   print("Hello World!")
   do_twice(test,5)
   print_twice("hello")
   mod_do_twice(print_twice,'spam')
   do_four(print_twice,'printfour')
   
	
	

if __name__ == "__main__":
    main()