n=input("Enter a string:")
lowercount=uppercount=0
digitcount=alphacount=0
for i in n:
    if i.islower():
        lowercount+=1
    elif i.isupper():
        uppercount+=1
    elif i.isdigit():
        digitcount+=1
    if i.isalpha():
        alphacount+=1
print(lowercount)
print(uppercount)
print(digitcount)
print(alphacount)
