AIM:WRITE A PYTHON PROGRAM TO RETURN MULTIPLE VALUES FROM A FUNCTION

def addavg():
    return(a+b,(a+b)/2)
def sub():
    return(a-b)
def mul():
    return(a*b)
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print("sum,average",addavg())
print("subtraction",sub())
print("multiplication",mul())
"""
OUTPUT AND INPUT:
INPUT:
enter a value:6
enter b value:4
OUTPUT:
sum,average (10, 5.0)
subtraction 2
multiplication 24
"""
