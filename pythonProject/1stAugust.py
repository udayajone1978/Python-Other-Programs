# #program - functions
# def demo(name,age):
#     print(name,age)
#
# demo("Mary",20)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #program
# def funct1(v1,v2,v3):
#     print("\n",v1,"\n",v2,"\n",v3)
#
# funct1(20,40,60)
# def funct1(v1,v2):
#     print("\n", v1, "\n", v2, "\n")
# funct1(30,20)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #Program-
# def calculation(a,b):
#     add=a+b
#     sub=a-b
#     return add,sub
# print("Additon and Subtraction values are")
# res=calculation(50,20)
# print(res)
#
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# #program
# def calculate(a,b):
#     return a+b,a-b
#
# add,sub= calculate(50,30)
# print("addition -",add, "Subtraction -",sub)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #program
# def show_emp(a,b=9000):
#   #  b=9000
#     print("Name: ",a,"," "Salary: ",b)
# show_emp("Ben", 12000)
# show_emp("mary")
#
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #Program
# def my_function(food):
#     for x in food:
#         print("List of items - ",x)
#
# fruits=["apple","banana","mango","cherry"]
# my_function(fruits)
#
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# #Program
# def check(s):
#     return s*5
# print("First result" , check(4))
# print("Second result" ,check(5))
# print("Third result" , check(9))
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #program
# def even(list1):
#     list2=[]
#     for i in list1:
#       if i % 2 ==0:
#          list2.append(i)
#     return list2
# list2= even([1,2,3,4,5,6,7])
# print("Even numbers: ",list2)
#
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# #program
# def arithmetic(a,b):
#     add = a+b
#     sub = a-b
#     multiply= a*b
#     division=a/b
#     return add,sub,multiply,division
# a,b,c,d = arithmetic(21,18)
# print("Addition ",a)
# print("Subtraction ",b)
# print("Multiply ",c)
# print("Division ",d)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #program
# def function1():
#    localvariable="use only inside the function"
#    print("local variable- ",localvariable)
# function1()
# globalvariable = "we can use it anywhere"
# print("globalvariable-",globalvariable)
#
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #program
# globalvar= 777
# def function1():
#      print("Value is ",globalvar)
# def function2():
#     print("value is ",globalvar)
#
# function1()
# function2()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #program-global variable
# x=5
# def function1():
#     print("value of x is ",x)
# def function2():
#     global x
#     x =7
#     print("Value of x,after changing it's value- ",x)
# def function3():
#     print("value of x in function3- ",x)
#
# function1()
# function2()
# function3()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program- Non local variable
def outer_func():
    x=77

    def inner_func():
        nonlocal x
        x = 90
        print("value in inner_function ",x)

    inner_func()
    print("Value of x ", x)

outer_func()

#program-Keyword arguments
def message(fname,sname):
    print("Hello ",fname,sname)

message(fname="mary",sname='Moses')
message(fname="lara", sname="Moses")

#program-Variable length arguments
def addition(*number):
    total = 0
    for i in number:
       total=total+i
    print("sum is ",total)

addition()
addition(20,30,40)
addition(50,60,80,90)



























































