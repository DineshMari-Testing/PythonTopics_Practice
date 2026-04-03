#Print numbers from 1 to 10
from itertools import count

for i in range(0,11):
    print(i)

#Print your name 5 times
for i in range(5):
    print("Dinesh")

#Print numbers from 10 to 1 (reverse)
for i in range(10,1,-1):
    print(i)

#Print all even numbers from 1 to 20
for i in range (1,20):
    if i % 2 == 0:
        print("Even number :",i)


#Print all odd numbers from 1 to 20
for i in range(1,20):
    if i % 2 != 0:
        print("Odd number :",i)


#Print numbers from 1 to 50, but skip multiples of 5
for i in range(1,51):
    if i % 5 == 0:
        continue
    print("Not multiple by 5 :", i)

#Print numbers from 1 to 10, each on same line (use end=" ")
for i in range(1,10):
    print(i , end=" ")

#Find the sum of numbers from 1 to 10
num = 0
for i in range(1,11):
    num += i
    print(num)

#Find the sum of even numbers from 1 to 20
for i in range(1,20):
    if i % 2 == 0:
        i += i
        print(i)

#Find the sum of odd numbers from 1 to 20
for i in range(1,20):
    if i % 2 != 0:
        i += i
        print(i)

#Count how many numbers are there from 1 to 100
count = 0

for i in range(1,101):
    count += 1
    print(count , end=", ")

#Print multiplication table of any number (user input)
num = int(input("Enter the number for multiplication table : "))
for i in range(1,11):
    print(num,"X", i ,"=" ,num * i)

#Print multiplication table of 5
for i in range(1,11):
    print(5,"X", i ,"=" ,5 * i)

'''*
**
***
****
*****'''
for i in range(1,6):
    print("*" *i)

'''*****
****
***
**
*'''
for i in range(5,0 ,-1):
    print("*" *i)

'''1
12
123
1234
12345'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
print()



