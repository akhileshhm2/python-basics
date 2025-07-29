# squares=(x*x for x in range(1,6))
# for squares in squares:
#     print(squares)

# def generate_squares(limit):
#     for x in range(1,limit+1):
#         yield x*x
# squares=generate_squares(5)
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares)) 

# def outer(func):
#     def inner():
#         print("i got decorator")
#         func()
#     return inner
# @outer
# def ordinary():
#     print("i am ordinary")
# ordinary()   
# 
                









def orginal(func):
    def mini():
        print("hello")
        func()
    return mini
@orginal
def mix():
    print("world")
mix()    

    