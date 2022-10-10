# #program
# var=3
#
# var1=0
#
# var2=var1+1
#
# while(var<7):
#
#     var2=var2+var1
#
#     if(var1%2==0):
#
#             var=var+1
#             var1=var1+1
#
#     else:
#             var2=var2*var1
#             var1=var1+3
#
# print("value v1",var1)
# print("Value v2",var2)
import django
print(django)

#Program - Python function that takes a sequence of numbers and
# determines whether all the numbers are different from each other
def test_distinct(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False;

print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))

# Python3 program explaining work
# of randint() function

# import random module
import random

r1 = random.randint(5, 15)
print("Random number between 5 and 15 is " ,(r1))

r2 = random.randint(-10, -2)
print("Random number between -10 and -2 is " ,(r2))

#program-program to demonstrate the use of choice() method
import random
list1=[1,2,3,4,5,6]
print(random.choice(list1))
string = "Geeks"
print(random.choice(string))
tuple1=(2,4,6,8,10)
print(random.choice(tuple1))

#Program-

