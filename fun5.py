AIM:A FUNCTION TO CHECK IF A NUMBER IS PRIME OR NOT
def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
        return x
num=int(input("enter a number:"))
result=prime(num)
if result==1:
    print(num,"is prime")
else:
    print(num,"is not prime")
"""
OUTPUT AND INPUT:
INPUT:
enter a number:7
OUTPUT:
7 is prime
"""
