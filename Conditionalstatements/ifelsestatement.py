#Write a Python program to check whether a given number is even or odd using
num = int(input("Enter the number :"))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")



#Check whether a number is positive or negative
number = int(input("Enter the number :"))
if number > 0:
    print(number, "is positive")
else:
    print(number, "is negative")


#Check whether a number is greater than 100 or not
num_ber = int(input("Enter the number :"))
if num_ber <= 100:
    print(num_ber, "is less than 100")
else:
    print(num_ber, "is greater than 100")


#Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter the age :"))
if age >=18:
    print(age ," Eligible for vote")
else:
    print(age ," Not Eligible for vote")


#Check whether a number is divisible by 5 or not
number = int(input("Enter the number :"))
if number % 5 == 0:
    print(number, "is divisible by 5")
else:
    print(number, "is not divisible by 5")


#Check whether a number is zero or not
number = int(input("Enter the number :"))
if number == 0:
    print(number, "is zero")
else:
    print(number, "is not zero")

#Find the greater number between two numbers
a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
if a > b:
    print(a, "is greater than ", b)
else:
    print(b, "is less than ", a)


#Check whether a number is a multiple of 3 or not.
number = int(input("Enter the number :"))
if number % 3 == 0:
    print(number, "is multiple by 3")
else:
    print(number, "is not multiple by 3")

is_logged_in = bool(input("Is logged in?"))
if not is_logged_in == True:
    print("please login first")