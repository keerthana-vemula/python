#AIM:FUNCTION TO CALCULATE FACTORIAL VALUES OF NUMBERS
n=int(input("enter n value"))
def fact(n):
    prod=1
    while n>1:
        prod*=n
        n-=1
    return prod
    print("factorial",n)
