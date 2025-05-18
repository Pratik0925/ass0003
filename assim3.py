

n=int(input("Enter a number: "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
result=factorial(5)
print("Factorial of 5 is: ",result)


#task 2

import math

x=float(input("Enter a number: "))

n = math.sqrt(x)
p= math.log(x)
q=math.sin(x)

print("Square root: ",n)
print("Logarithm: ",p)
print("Sine: ",q)