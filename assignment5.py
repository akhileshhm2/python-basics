# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"Name:{self.name}")
#         print(f"age:{self.age}")
# s1=Student("akhilesh",32)
# s1.info()
# 
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
# b1=Book("got","george")
# print(b1.title)
# print(b1.author)                   

# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"rollno:{self.rollno}")
# s1=Student("akhilesh",3)
# s1.display()
# 
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
# area1=Rectangle(8,5)
# print(area1.area())
# 
# class BankAccount:
#     def __init__(self,owner,balance=0):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"succesfully deposited{amount}")
#     def withdrawel(self,amount):
#         if amount > self.balance:
#             print(f"insufficent balance")    
#         else:
#             self.balance -= amount
#     def display_balance(self):
#         print(f"account holder:{self.owner}")
#         print(f"current balance{self.balance}")
# b1=BankAccount("owner",5000)
# print(f"initial account details")
# b1.display_balance()
# print(f"amount to be deposited")
# b1.deposit(2000)
# print(f"after the deposited")
# b1.display_balance()
# print(f"withdraw the money")
# b1.withdrawel(10000)
# print(f"withdraw the money2")
# b1.withdrawel(5000)
# print(f"final account details")
# b1.display_balance()

class Shape:
    def __init__(self,sides):
        self._sides=sides
    def setsides(self,num):
        self.num=num
    def info(self):
        print(f"the number of sides:{self._sides}")
class Triangle(Shape):
    def __init__(self):
        super().__init__(3)
T=Triangle()
T.info()        
                        
    




        




