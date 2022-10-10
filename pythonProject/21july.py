# program-1  while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+= 1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# program-2  while loop
j = 1
while j < 8:
    print(j)
    print("Welcome to python world")
    if j == 7 :
        break
    j+=1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -3  while loop
k = 0
while k < 5:
    k += 1
    if k == 3:
        continue
    print(k)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -4
c = 1
while c < 5:
    print(c)
    c += 1
else:
    print("c is no longer than 6")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -5 for loop
fruits = ["grapes","banana","Mango","Apple"]
for x in fruits:
      print("Given Element:  ",x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program-6 for loop(strings)
for x in "banana":
    print("Result: ",x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program-7
city = ["chennai","Banglore","mumbai","Kolkatta","goa"]
for y in city:
    print("cities list: ",y)
    if y == "Kolkatta":
        break
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program-8
city = ["chennai","Banglore","mumbai","Kolkatta","goa"]
for y in city:
    if y == "Kolkatta":
        break
    print("Result after break statement:  ",y)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program_9 for & continue statement
city = ["chennai","Banglore","mumbai","Kolkatta","goa"]
for c in city:
    if c == "mumbai":
        continue
    print ("list after if checking:  ",c)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program-10 range
for x in range(6):
    print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program_11
for x in range(2,6):
    print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - 12
for x in range(1,6,1):
    print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program - 13
for x in range(6):
    print(x)
else:
    print("finally finished")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program-14
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program-15
x = [1,3,5,7,9]
y = [2,4,6,8]
for h in x:
    for k in y:
        print(h,k)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - 15- function
def my_function():
    print("Hello from a function")

my_function()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - 16 - function
def family(name):
    print(name+ "jones")

family("amenda ")
family("emili ")
family("margrette ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program- 17
def func1(sname,hname):
    print(sname+" "+hname)

func1("Geetha","Latha")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -18
def joy(*name):
    print("The youngest child is  "+name[2])

joy("Latha","Geetha","uma","Rama","Ruba")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -19

def my_family(child1,child2,child3):
    print("The youngest child is:  "+child2)

my_family("Ruban","Altaf","Ram")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program - 20
def my_function(**kid ):
    print("His last name is  "+kid["lname"])

my_function(fname="Guru",lname="muthu")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program - 21 -Assignment
def fact(x):
        print("The factor of ", x ,"are: ")
        for i in range(1,x+1):
            if x % i == 0:
                print(i)

j=420
fact(j)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -22 -Assignment to print 10 even numbers
print("Natural numbers are ")
for i in range(0,11):
    print(i)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -23 Assignment
for i in range(1,24):
    if i % 2 == 0:
        print("Even numbers are ",i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program-24 Assignment
for i in range(1,24):
    if i % 2 != 0:
        print("Odd numbers are ",i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -25 Assignment
for i in range(1,11):
  print("Whole numbers are ",i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -26 Assignment -loop statement to print the following series:
#10, 20, 30 … … 300
print("Multipels of  10 numbers ",x)
for i in range(10,301):
    if i % 10 == 0:
        print (i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -27 Assignment - print first 10 integers and their squares
for i in range(1,11):
    print (i, " ",i * i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - 28 Multipels of 7

for i in reversed(range (7,106)):
    if i % 7 == 0:
        print ("multipels of 7",i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#rprogram-29 to display all even numbers that falls between two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
for i in range(a+1,b):
    if i % 2 ==0:
      print ("List of even numbers are:  ",i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -30 to find the sum of the digits of a number accepted from the user.
num=int(input("enter a number:"))
sum=0
for i in str(num):
    sum=sum+int(i)
print(sum)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -31 using function
def sum():
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    c = a + b
    print("Result: ",c)

sum()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -32 using function
def mult(a,b):
    c = a * b
    print("Result of multiplication is:  ",c)

mult(6,9)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program - 33 using arbitary arguments
def play(*name):
    print("The youngest child is ",name[3])

play("guru","Ram","siva","vishnu")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program -34 using function default parameter value
def country(name="Norway"):
    print("My country name is  ",name)

country("USA")
country("Europe")
country("Brazil")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program-35 passing list as an argument
def myfamily(member):
    for x in member:
        print ("Members list are  ",x)

list1=["Anuj","Uma","Raja","Rama","Akash"]
myfamily(list1)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - 36 function using return statement
def myfunc(x):
    return 3 * x
print("The answer is")
print(myfunc(2))
print(myfunc(5))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -37 function to find maximum of 3 numbers
def max():
    a=int(input("Enter the 1 number "))
    b=int(input("Enter the 2 number "))
    c=int(input("Enter the 3 number "))
    if a > b and a > c:
        print("Biggest number is  ",a)
    elif b > c:
        print("Bigest number is  ",b)
    else:
        print("Biggest number is  ",c)

max()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - 38 function  to sum all the numbers in a list
def display(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    print(sum)

list2 = [8,2,3,0,7]
print("Result of the addition is  ")
display(list2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - 39 function to multiply all the numbers in a list
def display(list1):
    sum = 1
    for i in list1:
        sum = sum * i
    print(sum)

list2 = [8, 2, 3, -1, 7]
print("Result  of the multiplication process is  ")
display(list2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -40
a = "1234abcd"
print("Reversed string is  ", a[-1:])













