# Q1. Write a program to check whether a given number is Armstrong or not.

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    
    # Calculate 
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    return sum == num

number = int(input("Enter a number to check: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")