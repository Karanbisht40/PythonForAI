#normal function
def add(a,b):
    print(a+b)

add(2,3)

#with help of args 
def add(*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        sum += i
    print(sum)

    #fun call 
add(2,3,5,6,8,9,3)

# normal
def mydetails(name, age):
    print(name)
    print(age)
mydetails("karan", 19)

# #with kwargs
def  mydetails(**kwargs):
    print(kwargs)
    # print(type(kwargs))
    # for key,value in kwargs.items():
    #     print(key,value)


mydetails(name="karan", age=25, edu="btech", location="hyderabad")