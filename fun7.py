AIM:PYTHON PROGRAM TO ILLUSTRATE FUNCTIONS CAN BE PASSED AS ARGUMENTS TO OTHER FUNCTIONS
def shout(text):
    return text.upper()
def out(text):
    return text.lower()
def greet(func):
    greeting=func("hello,this is a function program")
    print(greeting)
greet(shout)
greet(out)
"""
OUTPUT:
HELLO,THIS IS A FUNCTION PROGRAM
hello,this is a function program
"""
