#Print numbers from 1 to 10
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



