#Fibonacci series
a = 0
b = 1

for i in range(10):
    print(a , end=",  ")
    c = a + b
    a = b
    b = c

print()

#Print Fibonacci numbers less than 50
a = 0
b = 1
while a < 50:
    print(a , end=", ")
    c = a + b
    a = b
    b = c


print()
#Find the sum of first 10 Fibonacci numbers
a = 0
b = 1
total = 0
for i in range(20):
    print(a , end=",  ")

    c = a + b
    a = b
    b = c
    total += a

print()
print(total)

#Check whether a number is in Fibonacci series or not
#(Example: 13 → Yes, 14 → No)
num = int(input("Enter number: "))

a = 0
b = 1

found = False

while a <= num:
    if a == num:
        found = True
        break

    c = a + b
    a = b
    b = c

if found:
    print("Yes")
else:
    print("No")