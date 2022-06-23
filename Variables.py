#Here we start with 2 variables

var1 = 17          #Here variable is number type
var2 = "Akshat"    #Here variable is string type

print("var1")
print("var2")

#We can assigne different names to the variable
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#Variable Names are case sensitive

myvar = "John"
my_var = "John"
myVar = "John"
MYVAR = "John" #This is constant
myvar2 = "John"

#Values to multiple variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Instade of this we can print them in single print function with the help of comma
print(x,y,z)

#we can add them in single line using "+" operator
print(x+y+z)

#We cannot add a number variable into string variable with the above method, it will give an error

#Example of global variable and local variable
A = "awesome"   #this is global variable
#we can assign global variable using keyword "global"
def myfunc():
  A = "fantastic"   #this is local variable with the same name, so it can apply only on the loop
  print("Python is " + A)

myfunc()

print("Python is " + A)