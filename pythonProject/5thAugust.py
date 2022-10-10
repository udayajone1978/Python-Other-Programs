#Program - print pattern E
for row in range(7):
    for col in range(5):
        if col ==0 or ((row==0 or row ==3 or row ==6 and col>0)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print("\n")
print("\n")
#program - print pattern O
for row in range(7):
    for col in range(5):
        if ((col ==0 or col ==4) and (row!=0 and row!=6))or ((row ==0 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
print("\n")
#program -print pattern F
for row in range(7):
    for col in range(5):
        if (col ==0) or ((row ==0 or row ==3) and col>0):
            print("*",end="")
        else:
            print(end = " ")
    print()
print("\n")
print("\n")

#program - pattern triangle
rows=int(input("Enter number of rows: "))
k=0
count=0
count1=0
for i in range(1,rows+1):
     for j in range(1,(rows-i)+1):
         print("  ",end="")
         count+= 1
     while k!=((2*i)-1):
           if count<=rows-1:
             print(i+k,end=" ")
             count+=1
           else:
             count1+=1
             print(i+k-(2*count1),end=" ")
           k+=1

     count1=count=k= 0
     print()
print("\n")
print("\n")

#program
a=int((input("Enter the first number")))
b=(int(input("Enter the second number")))
def add(a,b):
   print("addition value - ", a+b)
def sub(a,b):
   print("subtraction value -  ", a-b)
def mul(a,b):
    print("Multiplied value - ",a*b)
def div(a,b):
    print(" Divided value -  " , a/b)
def pow(a,b):
    print("power of a is -  " , a**b)

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
pow(a,b)
