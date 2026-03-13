a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Entert third number"))
sum1=0
sum1=a+b+c
print("Sum of three numbers is ",sum1)
sum2=0
if a!=b and a!=c:
    sum2+=a
if b!=a and b!=c:
    sum2+=b
if c!=a and c!=b:
    sum2+=c
print("Sum of non-repeated number is",sum2)

