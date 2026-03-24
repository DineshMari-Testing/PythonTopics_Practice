#variable  & Casting
x = 5
y = 7
print(str(x) + str(y))
print(float(x), float(y))


#variable name types
myVariableName = "Dinesh"  #Camel Case
MyVariableName = "Mari"   #Pascal Case
my_variable_name = "s"  #Snake Case
print(MyVariableName , myVariableName, my_variable_name)


#Variable - Assign Multiple Values
x,y,z = 1,2,3
print(x,y,z)


#One value to Multiple Variable
a=b=c = "Maridinesh S"
print(a)


#Unpack collection
fruits = ["Apple","Banana","Cherry"]
x,y,z = fruits
print(x,y,z)


#Python Output variable
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

#Output variable with using + operator ( Notice the space after the words Python and is - if using + Operator )
x = "Python "
y = "is "
z = "awesome"
print(x+y+z)

#Global Variable
x = "awesome"

def myfunc():
    print(x)

myfunc()

#Global variable and local variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print(x)

myfunc()
print(x)

#Global keyword Using
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print(x)

myfunc()
print(x)


#Global variable to change the inside as function ( function not called so the variable taken teh global variable of awesome )
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print(x)

print(x)



