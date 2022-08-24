def upper_decor(fu):
    def wrap():
        result = fu()   #hello
        return result.upper()
    return wrap
@upper_decor
def hello_name():
    return "hello"

# print(upper_decor(hello_name)())
print(hello_name())
# # --------------------------------

# def upper_decor(fu):
#     def wrap(name):
#         result = fu(name)   #hello
#         return result.upper()
#     return wrap
# @upper_decor

# def hello_name(name):
#     return "hello "+name

# name=input("enter a name")

# # print(upper_decor(hello_name)())
# print(hello_name(name))
#------------------------------------------
# def decor(fun):
#     def wrapper(n):
#         any_list=fun(n)
#         return[item * 3 for item in any_list]
#     return wrapper


# @decor 
# def upper(l):
#     return[item.upper() for item in l]


# print(upper(['a','b','c']))