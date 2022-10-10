 #program
def even(list1):
     list2=[]
     for i in list1:
       if i % 2 == 0:
        list2.append(i)
     return list2

list2 = even([1,5,7,4,6,8,10,12])
print("Even numbers are" ,list2)

#program
def add(*numbers):
     total=0
     for n in numbers:
         total=total+n
     print("Sum is ",total)

add()
add(4,5,6,7)
add(20,30,40,50)

# #Program
def fact(n):
     if n ==0:
         return 1
     else:
         return n*fact(n-1)
print("factorial of a number ",fact(7))

 #Program -lambda function
l=[2,5,6,10,12,14,18]
even_no= list(filter(lambda x: x % 2 ==0,l))
print("Even numbers are ",even_no)

#program - ATM program
amount1=100000
while True:
    print("1 Deposit")
    print("2 Withdrawal")
    print("3 Balance")
    a = input("Enter the option")
    if a =="1":
        s=int(input("Enter the Deposit amount"))
        amount1 = amount1+s
        print("total balance",amount1)
    elif a =="2":
         f = int(input("Enter the Withdrawal amount"))
         amount1 = amount1 - f
         print("Total balance ",amount1)
    elif a =="3":
         print("Existing balance", amount1)

    b=input("Do you want to continue ?(yes/no)")
    if b == "no":
        print("Thank you")
        break
    elif b =="yes":
        continue



