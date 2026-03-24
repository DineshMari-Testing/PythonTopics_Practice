#Check whether a number is positive, negative, or zero
num = int(input("Enter the number = "))
if num >0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")


#Check whether a number is even or odd
num2 = int(input("Enter the number = "))
if num2 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#Check whether a number is divisible by 5
num3 = int(input("Enter the number = "))
if num3 % 5 == 0:
    print("The number is divisble by 5")
else:
    print("The number is not divisible by 5")


#Check whether a number is divisible by both 3 and 5
num4 = int(input("Enter the number = "))
if num4 % 3 and num4 % 5 == 0:
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 and 5")


#Find the greater number between two numbers
num5 = int(input("Enter the number = "))
num6 = int(input("Enter the number = "))
if num5 > num6 and num6 > num5:
    print(" Num5 is greater than Num6")
else:
    print(" Num6 is greater than Num5")

#Check whether a number is within range 1 to 100
num7 = int(input("Enter the number = "))
if num7 >1 and num7 < 100:
    print ("the number is in range")
else:
    print ("the number is not in range")

#Check whether a character is vowel or consonant
word = str(input("Enter the word = "))
if word == ( "a", "e", "i" ,"o" , "u"):
    print("The word is in vowels")
else:
    print("The word is not in vowels")

#Check whether a number is single digit, double digit, or more
num8 = int(input("Enter the number = "))
if num8 < 10:
    print("number is single digit")
elif num8 < 100:
    print("number is double digit")
else:
    print("number is more than double digit")


#Find the greatest of three numbers
a = int(input("Enter the a = "))
b = int(input("Enter the b = "))
c = int(input("Enter the c = "))

if a>=b and a>=c:
    print(" A is greater :",a)
elif b >= a and b >= c:
    print(" B is greater :" ,b)
else:
    print(" C is greater :" ,c)

#Find the smallest of three numbers
x = int(input("Enter the x = "))
y = int(input("Enter the y = "))
z = int(input("Enter the z = "))

if x <= y and x<=z:
    print ("x is smallest :" , x)
elif y <= z and y <= x:
    print ("y is smallest :" , y)
else:
    print ("z is smallest :" , z)



