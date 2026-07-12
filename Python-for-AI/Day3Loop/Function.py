def greet():
    print("hello")

greet()

#function with parameter

def hello(name):
    print(f"my name is {name}")
hello("karan")

#function with more than one parameter
def myfun(a,b):
    print(a+b)

myfun(2,3)

#function with keywords arguments
def hello(a, b,c):
    print(a+b+c)

hello(a=2, b=3, c=4)