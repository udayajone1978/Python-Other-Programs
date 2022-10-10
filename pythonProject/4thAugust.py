#Program - SWap
a=int(input("Enter the first value "))
b=int(input("Enter the second value "))
print("Original value of a and b is :",a,"",b)
a = a+b
b = a-b
a = a-b
print(" After swapping a is :",a,"b is :" ,b)

#Program - occurrences of each character
str1="Hello world"
print("occurrences of H :", str1.count("H"))
print("occurrences of e :", str1.count("e"))
print("occurrences of l :", str1.count("l"))
print("occurrences of o :", str1.count("o"))
print("occurrences of w :", str1.count("w"))
print("occurrences of r :", str1.count("r"))
print("occurrences of d :", str1.count("d"))

#program- Anagram strings
b=("LisTen AcT")
b1=b.lower()
a=("SiLeNt CAT")
a1 = a.lower()
a1 = [a1[i] for i in range(0,len(a1))]
a1.sort()
b1 = [b1[i] for i in range(0,len(b1))]
b1.sort()
if a1 == b1:
    print("Given strings are Anagram")
else:
    print("Given strings are not Anagram")


#program -4.	Write a python program to reverse each word of a given string
def sentence(s1):
    words=s1.split(" ")
    newwords=[word[::-1] for word in words]
    newsentence=" ".join(newwords)
    return newsentence

s1="Python Concept Of The Day"
print(sentence(s1))

#program-substring


def substr(str1,n):
    for i in range(n):
        temp= " "
        for j in range(i,n):
            temp += str1[j]
            print(temp)
str1="test"
substr(str1,len(str1))
print(str1)

#rpogram -print pattern
for i in range(1,6):
    for j in range(5,0,-1):
        if(i ==j):
            print("*",end="")
        else:
            print(j,end="")
    print()

#Program for diamond pattern
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
