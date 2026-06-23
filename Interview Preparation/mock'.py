name= "chandrakala"
rev = ""

for ch in name:
    rev = ch + rev
print(rev)

a = 45
b = 8
a , b = b, a

print("Swapped from b:" ,a , " Swapped from a :",b)

n = int(input("Enter number : "))
a = 0
b = 1

found = False

while a <=n:
    if a == n:
        found = True
        break
    c = a + b
    a = b
    b = c
if found:
    print("Yes")
else:
    print("No")


a = 0
b = 1

for i in range(6):
    print (a , end =", ")
    c = a + b
    a = b
    b = c
print()


n = int(input("Enter number : "))

if n<=1:
    print("Not prime")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not prime")
            break
        else:
            print("Prime")


