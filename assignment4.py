# n=int(input("enter the nimber"))
# x=lambda a:a*a
# print(x(n))

# n1=int(input("enter the 1st number:"))
# n2=int(input("enter the 2nd number:"))
# x=lambda n1,n2:n1+n2
# print(x(n1,n2))

# list1=[2,3,4,5,6]
# result=map(lambda a:a*a,list1)
# result=list(result)
# print(result)

# def check_even(number):
#     if number%2==0:
#         return True
#     else:
#         return False
# n=[1,2,3,4,5,6,7,8,9,10]
# even_num_check=filter(check_even,n)
# even_num_check=list(even_num_check)
# print(even_num_check)
# 
# a=[(1,2),(3,4),(4,6),(5,9)]
# a.sort(key=lambda x:x[1])
# print(a) 
# 
# from functools import reduce
# n=[1,2,3,4,5,6,7,8,9,10]
# product=reduce(lambda x,y:x*y,n)
# print(product)

# list1=["abhi","cat","bob"]
# upper=lambda x:x.upper()
# list2=map(upper,list1)
# list2=list(list2)
# print(list2)

# people = [
# {"name": "Alice", "age": 30},
# {"name": "Bob", "age": 25},
# {"name": "Charlie", "age": 35}
# ]
# people.sort(key=lambda x:x['age'])
# print(people)

# def make_multiplier(n):
#     return lambda x:x*n
# times2=make_multiplier(2)
# times5=make_multiplier(5)
# num=int(input("enter the number:"))
# print("the result:",times2(num))
# print("the result:",times5(num))



# words = ['apple', 'banana', 'grape', 'kiwi']
# sorted_words = sorted(words, key=lambda w: sum(letter in 'aeiou' for letter in w.lower()))
# print(sorted_words)

# words = ['madam', 'hello', 'noon', 'python']
# # result=filter(lambda x:x==x[::-1],words)
# # result=list(result)
# # print(result)

# from functools import reduce
# words = ['Hello', 'world', 'From', 'python']
# cap_words=filter(lambda x:x[0].isupper(),words)
# result=reduce(lambda a,b:a+b,cap_words)
# print(result)

# products = [
# {"name": "Laptop", "price": 900},
# {"name": "Phone", "price": 500},
# {"name": "Tablet", "price": 300},
# {"name": "Monitor", "price": 200}
# ]
# filtered_pro=list(filter(lambda x:200<=x["price"]<=800,products))
# print(filtered_pro)

# numbers = [10, 15, 22, 33, 42]
# categorize=list(map(lambda x:(x,"even"if x%2==0 else "odd"),numbers))
# print(categorize)

# emails = ['alice@example.com', 'bob@gmail.com', 'carol@yahoo.com']
# domain_ext=list(map(lambda x:x.split('@')[1],emails))
# print(domain_ext)






