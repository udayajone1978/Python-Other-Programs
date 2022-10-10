#program- accessing private members from public method
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def show(self):
        print("Name- ",self.name,",Salary- ",self.__salary)

emp=employee("Mary",20000)
emp.show()

#program- Name Mangling
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

emp=employee("Ram",30000)
print("Name- ",emp.name)
print("Salary- ",emp._employee__salary)

#Program-Protected Member
class company():
    def __init__(self):
        self._project="NLC"
class employee(company):
    def __init__(self,name):
        self.name=name
        company.__init__(self)

    def show(self):
        print("Employee name : ",self.name)
        print("Working on project : ",self._project)

emp=employee("Amenda")
emp.show()

#Program-getters and setters
class student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age

stud = student("Gourav",12)
print("Name- ",stud.name,",Age- ",stud.get_age())
print("After setting age")
stud.set_age(15)
print("Name- ",stud.name,",Age- ",stud.get_age())

#Program-Information Hiding and conditional logic for setting an object attributes
class student:
    def __init__(self,name,rollno,age):
        self.name=name
        self.__rollno=rollno
        self.__age=age
    def show(self):
        print("Name- ",self.name,",Roll.no- ",self.__rollno,",Age- ",self.__age)
    def get_rollno(self):
        return self.__rollno
    def set_rollno(self,number):
        if number >50:
            print("Please enter correct roll number")
        else:
            self.__rollno=number

s1=student("Mary",123,15)
s1.show()
print("After modify")
s1.set_rollno(23)
s1.show()

#Program- classes and objects
class vehicle():
    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage

v=vehicle(140,120)
print("maxspeed ",v.maxspeed,"mileage ",v.mileage)

#Program- Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(Vehicle):
    pass

volvo=bus("School volvo",130,150)
print("Bus name-",volvo.name,",Speed-",volvo.max_speed,",Mileage-",volvo.mileage)


#Program
x=int(input("Enter the value to be checked as odd or even - "))
def check():
    if x & 1:
        return 'odd'
    else:
        return 'even'

# print("Result is ",check())

#Program
class Mystore:
    __prod_code=[]
    __prod_name=[]
    __prod_price=[]
    __prod_quant=[]

    def getdata(self):
        self.p=int(input("Enter no.of products you need to store: "))
        for x in range(self.p):
            self.__prod_code.append(int(input("Enter product code: ")))
            self.__prod_name.append(input("Enter product name: "))
            self.__prod_price.append(int(input("Enter cost price: ")))

    def display(self):
        print("        Stock in stores")
        print("____________________________________________")
        print("Product code\t Product name\tCost price")
        print("__________________________________________")

        for x in range(self.p):
            print(self.__prod_code[x], "\t\t\t",self.__prod_name[x],"\t\t\t",self.__prod_price[x])
            print("_________________________________________")
    def print_bill(self):
        total_price=0
        for x in range(self.p):
             print("Enter the Quantity of product code")
             q=int(input(self.__prod_code[x] ))
             self.__prod_quant.append(q)
             total_price=total_price+self.__prod_price[x]*self.__prod_quant[x]
        print("        INVOICE RECEIPT        ")
        print("_______________________________________________________________________________________")
        print("Product code\t\tProduct name\t\tCost price\t\tQuantity\t\tTotal Amount")
        for x in range(self.p):
                print(self.__prod_code[x],"\t\t\t\t",self.__prod_name[x],"\t\t\t\t",self.__prod_price[x],"\t\t\t\t", self.__prod_quant[x],"\t\t\t\t",self.__prod_quant[x]*self.__prod_price[x])
                print("_____________________________________________________________________________________")
        print("                                 Total Amount=", total_price)
        Amount=int(input("Enter the amount given by consumer  "))
        Total= Amount -total_price
        print("Balance amount= ",Total)

s=Mystore()
s.getdata()
s.display()
s.print_bill()


#Program -Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f" The Seating Capacity of a {self.name} is  {capacity}"

class bus(Vehicle):
    def seating_capacity(self,capacity=50):
     return super().seating_capacity(capacity=50)

b = bus("Omni",150,250)
print(b.seating_capacity())

#program-Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    color = "white"

class Car(Vehicle):
    color = "white"

c= Car("SWift ",170,280)
print("Name- ",c.name,",Max-speed- ",c.max_speed,",Mileage- ",c.mileage)
c1= Bus("Volvo" , 180,230)
print("Name- ",c1.name,",Max-speed- ",c1.max_speed,",Mileage- ",c1.mileage)

#Program - Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class vehicle():
    def __init__(self,name,maxspeed,mileage,capacity):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.capacity=capacity
    def fare(self):
        print("Name- ",self.name,"Maxspeed- ",self.maxspeed,"Mileage- ",self.mileage,"Seating capacity- ",self.capacity)
        return self.capacity*100
class bus(vehicle):
    pass
schoolbus= bus("Omni",120,260,50)
print("Amount= ",schoolbus.fare())

#program- Write a program to determine which class a given Bus object belongs to.
class vehicle():
    def __init__(self,name,maxspeed,mileage,capacity):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.capacity=capacity
class bus(vehicle):
    pass

schoolbus = bus("Maruthi",150,250,30)
print("Name- ",schoolbus.name,",Maxspeed- ",schoolbus.maxspeed,",Mileage- ",schoolbus.mileage,",Seating capacity- ",schoolbus.capacity)
print(type(schoolbus))

