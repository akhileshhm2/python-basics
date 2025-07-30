# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"Name:{self.name},Age:{self.age}")
# s1=student("akhilesh",22)
# s1.display() 

# class dog:
#     def __init__(self,breed,color):
#         self.breed=breed
#         self.color=color
# d1=dog("rottwheeler","black")
# print(d1.breed)
# print(d1.color)

class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def info(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Price:{self.price}")
b1=book("got","Jason",500)
b1.info()            


                   
        