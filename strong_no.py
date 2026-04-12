def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Input from user
num = int(input("Enter a number: "))

# Store original number
temp = num
sum_of_fact = 0

# Calculate sum of factorials of digits
while temp > 0:
    digit = temp % 10
    sum_of_fact += factorial(digit)
    temp //= 10

# Check if strong number
if sum_of_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")
