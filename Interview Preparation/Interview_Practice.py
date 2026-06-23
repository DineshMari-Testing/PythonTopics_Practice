#Reverse string
s = "Python"
print(s[::-1])

s = "Balasubramanian"
rev = ""

for c in s:
    rev = c + rev

print(rev)

#Palindrome string
str = "madam"

if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#Largest number in array
arr = [1,2,3,4,5,10]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print(largest)

#smallest number in array
arr = [1,2,3,4,5,10]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i
print(smallest)


#Second largest number
arr = [10,20,30,40,50]
arr.sort()
print(arr[-2])


#Sort array
arr = [5,3,2,4,1]
arr.sort() #Ascending
print(arr)

#Descending
arr = [5,3,2,1,4]
arr.sort(reverse=True)
print(arr)


#Sort array without sort keyword   ---- Need to learn
arr = [5, 3, 1, 4, 2]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)



#Count Vowels
s = "python programming"
count = 0
for c in s.lower():
    if c in "aeiou":
        count += 1

print(count)


#Prime number check
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not prime number")
            break
    else:
        print("Prime number")

