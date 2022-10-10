#next program
h=list(range(30,100,10))
print("given Range  ", h)
j=list(range(10))
print("Arrived range =  ", j)
print("After slicing-1",  j[2:6:2])
a=list(range(10))
print("Arrived range =  ", a)
print("After slicing-2 ",  a[0:8:3])
a=list(range(10))
print("After slicing-3 ",  a[:-2])
a=list(range(10))
print("The  Element are  ", a)
print("After slicing-4 ", a[:-2:2])
a=list(range(10))
print("The  Element are  ", a)
print("After slicing-5 ", a[::4])
a=list(range(10))
print("The  Element are  ", a)
print("After slicing-6 ", a[2:-2])
a="Stuttgart"
print("Given String:  ",a)
print("After slicing -7 " , a[2:-2])
a="Stuttgart"
print("Given String:  ",a)
print("After slicing-8 " , a[-2:])
a=list(range(10))
print("The  Element are  ", a)
print("After slicing-9 ", a[2:3])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program -40
a = "1234abcd"
b=a[::-1]
print("Reversed string is  ",b)


#Program -42
for i in range(6):
    for j in range(i):
      print("*",end=" ")
    print(" ")
print("~~~~~~~~~~~~~~~~~~~")
for i in range(5,0,-1):
  for j in range(i):
    print("*", end=" ")
  print(" ")

#program for using loop comprehension
fruits = ["Banana","Mango","Apple","Avakoda"]
newlist=[]
for x in fruits:
    if "a" in x:
      newlist.append(x)
print(newlist)


#program to sum all items in the list
x = [10,11,12,13]
print("The item to be added", x)
result = sum(x)
print("The sum of all items are" , result)

#program- test
x=50
def fun1():
    x=25
    print(x)
fun1()
print(x)

#program -test
x=75
def myfunc():
 x = x+1
 print(x)
myfunc()
print(x)

#program - test
print(bool(0),bool(3.14159),bool(-3),bool(1.0+1j))

# program - test
def func1():
    x=50
    return x
func1()
print(x)

#Program -test
a=[10,20]
b=a
b+=[30,40]
print(a)
print(b)

#program - test
x=10
y=50
if x**2<100 and y<100:
    print(x,y)


#program -strings
a = " Rithika ,sen "
print("length before strip method",len(a))
x= a.strip(" ")
print(x)
print("length after strip method",len(x))
print("splitting method ")
c=a.split(",")
print(c)
print(list("Rithika sen"))
c="python"
print(list(c))
for i in c:
    print(i)

#program -strings
c="  WELCOME TO PYTHON WORLD "
print(len(c))
#print(c.strip("Welcome "))
d = c.strip(" ")
print(len(d))
e="welcome to python world"
print(e.capitalize())
print(c.casefold())
print(c.center(60))
print(e.count("e"))
print(e.count("o"))
print(e.format())

# program -strings
name="kumar"
age = 26
print ("My name is ",name + "    ","Age =",format(age))
x="My name is varshaa"
print(x.encode())
# program
x="H\te\tl\tl\to"
print(x.expandtabs(2))
print(x.find("e"))


#program -16-assignment
"""a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30 (both included)."""
def values():
    l = list()
    for i in range(1,30):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
values()


#program-17 -assignment
"""a Python program to generate and print a list except for the first 5 elements, 
where the values are square of numbers between 1 and 30 (both included)"""
def printvalues():
    l = list()
    for i in range(1,30):
        l.append(i**2)
    print(l[5:15])
printvalues()

#program-18
#Write a Python program to sum all the items in a list
newlist=[]
k=int(input("enter the number of elements in list"))
for i in range(1,k):
    newlist1= int(input("enter the elements one by one"))
    newlist.append(newlist1)
print(sum(newlist))

#program-19
# Write a Python program to get the largest number from a list.
newlist=[]
k=int(input("enter the number of elements in list"))
for i in range(0,k):
    newlist1= int(input("enter the elements one by one"))
    newlist.append(newlist1)
print("given elements" ,newlist)
print(max(newlist))

#program_20
#Write a Python program to get the smallest number from a list

newlist=[]
k=int(input("enter the number of elements in list"))
for i in range(0,k):
    newlist1= int(input("enter the elements one by one"))
    newlist.append(newlist1)
print("given elements" ,newlist)
print("Smallest element in the list" ,min(newlist))

#program=21
# a Python program to count the number of strings
# where the string length is 2 or more and the first and last character are same from a given list of strings
"""a Python program to count the number of strings
where the string length is 2 or more and the first and last character are same from a given
list of strings"""
str=input("enter a string  ")
k=len(str)
print("length of the string", k)
for i in range(1,k):
    if (k >=2 and str[0]==str[k-1]):
        break
print("string is ", str)

#progrma -22
"""a Python program to get a list, sorted in increasing order by the 
last element in each tuple from a given list of non-empty tuples"""

newlist = [(2,1),(3,3),(1,2),(2,4)]
print("GIven list ", newlist)
def printitem(n):return n[-1]
tuple1= newlist
print("sorted list" , sorted(tuple1,key=printitem))

#Write a Python program to remove duplicates from a list.
newlist = [1,3,3,7,74,5,1,9,9]
print("Given list", newlist)
newset=set()
list2=list()
for x in newlist:
    if x not in newset:
        newlist.append(x)
        newset.add(x)
print("List without duplicates", newset)

#Write a Python program to check a list is empty or not
x=input("Enter the elements separated by comma:  ")

if x:
 print("list is full")
else:
    print("empty")

#Write  a Python program to clone or copy a list.
list1=[1,2,3,4,5]
list2=[list1]
print("original list", list1)
print("cloning list",list2)

#Write a Python program to find the list of words that are
# longer than n from a given list of words.
str=input("Enter the string  ")
n=int(input("Enter the number of characters "))
a = []
b=str.split(" ")
for x in b:
    if (len(x) > n):
        a.append(x)
print(a)

