#Create variables to store your name, age, and city. Print them
from pydoc import text

name =  "Dinesh"
age = 27
city = "Chennai"
print(name)
print(age)
print(city)

#Assign two numbers to variables and print their sum.
x = 100
y = 200
print(x + y)

#Store a float value and an integer value. Print their data types
num1 = 20.5
num2 = 50
print(type(num1))
print(type(num2))

#Create a variable for price and quantity. Calculate total cost
price = 1000
quantity = 8

calculate = price * quantity
print(calculate)

#Swap two variables (without using third variable is optional).
a = 5
b = 10
a,b = b,a
print("a =",a)
print("b =",b)

#Store your full name in one variable and print it in uppercase
name = "Dinesh"
print(name.upper())
print(name.lower())
print(name.title())


#Create a boolean variable and print its type
x = bool(10)
print(x)
print(type(x))

#Store a string and print its length
name = "MariDinesh"
print(len(name))
name1 = input("Enter you name =")
print(len(name1))


#Create variables for length and width. Find area of rectangle
length = 500
width = 300

area = length * width
print("Area of rectangular = ",area)

#Assign a number and print its square and cube
num3 = 10
square = num3 ** 2
cube = num3 ** 3
print("square =", square)
print("cube = " ,cube)

#Create variables for marks of 3 subjects and calculate average
Maths = 78
science = 98
social = 60

avg = (Maths+science+social)/3
print("avg =",avg)

#Store two strings and concatenate them
x = "Mari"
y = "Dinesh"
z = x + " " + y
print(z)

#Create a variable with a large number and convert it into float
l_num = 1500
flt = (float(l_num))
print(flt)

#Create variables for seconds and convert into minutes
sec = 180
min = sec / 60
print(min)

#Store your birth year and calculate your current age
birthyear = 1999
currentyear = 2026
age = currentyear - birthyear
print("My age is :",age)

#Create variables for base and height. Calculate area of triangle
base = 30
height = 5
areaoftriangle = 0.5 * base * height
print(areaoftriangle)


#Store a string and print first and last character
name = "Dinesh"
first = name[0]
last = name[-1]
print(first)
print(last)


