
str=input("Enter the string  ")
n=int(input("Enter the number of characters "))
b = []
b=str.split(" ")
for x in str:
    if len(x) > n:
        b.append(x)
print(b)


#program
# samplelist=[0,1,True]
# print("All values"  , all(samplelist))
nestedlist = [[2,4,6,8,10],[1,3,5,7,9]]
for i in nestedlist:
    print(i)
    for j in i:
        print(j)

#program
list1=[1,2,3,4,5]
list2 = list1.reverse()
print(list1)

#program
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=[i+j for i,j in zip(list1,list2)]
print(list3)

#programs
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newlist = [x+y for x in list1 for y in list2]
print(newlist)

#programs
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

#program
list1=["george","","shyam","madan","kumar",""]
#res = []
res = list(filter(None,list1))
print(res)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# program
tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
print(tuple1[-1])

#program
tuple1= ('P', 'Y', 'T', 'H', 'O', 'N')
print(tuple1[-3])

#program
tuple1 = (0,1,2,3,4,5)
print("Existing list ",tuple1)
list1 = list(tuple1)
list1.remove(2)
tuple1 = tuple(list1)
print("changed list ",tuple1)

#program
nested_tuple = ((20, 40, 60), (10, 30, 50), "Python")
print(nested_tuple[2][0])
for i in nested_tuple:
    print("tuple",i,"Elements")
    for j in i:
        print(j ,end=",")
        print("\n")

# program
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

#program
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

#program
tuple1=tuple("hello",)
print(tuple1)
tuple3 = tuple(50,)
print(tuple3)

#program
tuple1=(10,20,30,40)
a,b,c,d = tuple1
print("value of a ",a)
print("value of b ",b)
print("value of c ",c)
print("value of d ",d)

#program
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple3=tuple2
tuple2=tuple1
tuple1=tuple3
print("tuple1 ",tuple1)
print("tuple2 ",tuple2)

#program-Copy specific elements from one tuple to a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
print(tuple1[3:-1])

#program-Modify the tuple
tuple1 = (11, [22, 33], 44, 55)
print("Given list ",tuple1)
tuple1[1][0]=222
print("After modification ",tuple1)

#Program-Counts the number of occurrences of item 50 from a tuple
tuple1=(1,4,3,2,4,50,6,4,7,9)
print("No.of appearances of 4: ",tuple1.count(4))

#Program-Check if all items in the tuple are the same
tuple1=(34,34,34,34)
list1=list(tuple1)
print(len(list1))

#program- List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
      newlist.append(x)
print(newlist)

#program-list Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist= [x for x in fruits if"a" in x]
print(newlist)

#Program- list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#program- print any one of the color,get input from user
colors=("Red","Green","Violet","blue")
print("List of color: ",colors)
value=(input("Enter any one of the color: "))
for i in colors:
    if value in i:
      print("Color existed")
    else:
      print("Not existed")
      break

#program- Dictionary
person = {"Name": "james", "age": 25, "salary": 20000}
print(person)

person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(person)
print(person.keys())
for key in person:
    print(key ,":",person[key])
print("Length of the dict: ",len(person))
