# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p=Person("akhilesh",22)
# print(p.name)  
# print(p.age) 
# 
# protected...................
# 
# class Person:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
# class student(Person):
#     def get_name(self):
#         return self._name
#     def get_age(self):
#         return self._age
# s=student("Bob",24)
# print(s.get_name())
# print(s.get_age())  
# 
# 2nd ex of protected......................
# 
# class Employee:
#     def __init__(self):
#         self._salary=50000
# class Outsider:
#     def reveal_salary(self,emp):
#         print(emp._salary)
# e=Employee()
# o=Outsider()
# o.reveal_salary(e) 
# 
# private.......................................
# 
# class Person:
#     def __init__(self,name):
#         self.__name=name
#     def dis_name(self):
#         return self.__name
# p=Person("charlie")
# print(p.dis_name())             

#pgm with pub,pro,pri.................
# 
class Bank:
    def __init__(self,acc_holder,balance,pin):
        self.acc_holder=acc_holder
        self._balance=balance
        self.__pin=pin
    def show_details(self):
        print(f"Account holder name:{self.acc_holder}")
        print(f"Account balance:{self._balance}")
    def withdrawal(self,amount,entered_pin):
        if entered_pin != self.__pin:
            print("incorrect pin")
        elif amount > self._balance:
            print(f"insufficient balance current balance is {self._balance}")
        else:
            self._balance -= amount
            print(f"withdrawal of {amount} is succesful")
            print(f"current balance is :{self._balance}")
b1=Bank("Akhilesh",5000,1234)
print("initial account details")
b1.show_details()
print("withdrawal attempt 1")
amt1=int(input("enter the withdrawel amount"))
pin1=int(input("enter the pin"))
b1.withdrawal(amt1,pin1)
print("withdrawal attempt 2")
amt2=int(input("enter the withdrawel amount"))
pin2=int(input("enter the pin"))
b1.withdrawal(amt2,pin2)
print("withdrawal attempt 3")
amt3=int(input("enter the withdrawel amount"))
pin3=int(input("enter the pin"))
b1.withdrawal(amt3,pin3)

# print("withdrwal attempt 2")
# b1.withdrawal(5000,1234)  
# print("withdrawal attempt:3")
# b1.withdrawal(500,1243) 
# print("final details")
b1.show_details()             

             