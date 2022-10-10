#program -print class name
class car:
    def parts(self):
        pass
class bus:
    def route(self):
        pass
b=bus()
print(b.__class__)
b1=b.__class__
print(b1.__name__)
c=car()
print(c.__class__)
classes=c.__class__
print(classes.__name__)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Program - Encapsulation
class student:
    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project

    def show(self):
        print("Name is ",self.name, "salary = ",self.salary)

    def work(self):
        print("Name is ", self.name,",I am working at ",self.project)

s1=student("Mary",12000,"NLP")
s1.show()
s1.work()
s2 = student("Anderson" ,14000,"HIG")
s2.show()
s2.work()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program - public members
class student:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def printmethod(self):
        print("Name is ",self.name,"and my salary is ",self.salary)

g=student("Leo ", 10000)
g.printmethod()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Program-private members
class detail:
    def __init__(self,name,age,salary):
        self.name=name
        self.__age=age
        self.salary=salary

d=detail("Anamica ",34,23000)
print("Name is ",d.name,"salary ",d.salary)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Program- access private member
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def show(self):
        print("Name is ",self.name,"and my salary is ",self.__salary)

emp = employee("lara",30000)
emp.show()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#program- Name Mangling

class Employee:
     def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee('Jessa', 10000)

print('Name:', emp.name)
print('Salary:', emp._Employee__salary)

#program
print(4+3%5)

#program
class vehicle:
    def __init__(self,price):
        self.price=price
    def display(self):
        print("price = ", self.price)

class category(vehicle):
    def __init__(self,price,name):
        vehicle.__init__(self,price)
        self.name=name
    def disp_name(self):
        print("vehicle=",self.name)

obj= category(20000,'BMW')
obj.disp_name()
obj.display()

#program
print(issubclass(category,vehicle))

#Program
print(isinstance(obj,vehicle))

#program
class A:
    def display(self):
        print("This is base class")

class B(A):
    def display(self):
       print("This is derived class")

obj = B()
obj.display()

#Program -
class vehicle:
    def vehicle_info(self):
        print("Inside vehicle class")
class car(vehicle):
    def car_info(self):
        print("Inside car class")

c = car()
c.vehicle_info()
c.car_info()
