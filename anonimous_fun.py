# n=[1,2,3,4]
# def square(numbers):
#     return numbers*numbers
# x=map(square,n)
# result=list(x)
# print (result)

# x=lambda a: a+10
# print(x(5))

# x=lambda a,b:a*b
# print(x(2,3))

# def myfun(n):
#     return lambda a :a*n
# doubler=myfun(2)
# print(doubler(11))

# numbers=[1,2,3,4]
# result=map(lambda x:x*x,numbers)
# print(result)
# print(set(result))

# def check_even(numbers):
#     if numbers%2==0:
#         return True
#     else:
#         return False
# n=[1,2,3,4,5,6,7,8,9,10]
# even_number_iterator=filter(check_even,n)
# even_num=list(even_number_iterator)
# print(even_num)
# 
# from functools import reduce
# def add(x,y):
#     return x+y
# a=[1,2,3,4]
# res=reduce(add,a) 
# print(res)   


# numbers=[1,2,3,4]
# result=map(lambda x:x*x,numbers)
# x=list(result)
# print(x)

# def even_check(numbers):
#     if numbers%2==0:
#         return True
#     else:
#         return False
# n=[1,2,3,4,5,6,7,8,9,10]    
# even_number_iterator=filter(even_check,n)
# even_num=list(even_number_iterator)
# print(even_num)           

from functools import reduce
def add(x,y):
    return x+y
n=[1,2,3,4,5]
result=reduce(add,n)
print(result)

