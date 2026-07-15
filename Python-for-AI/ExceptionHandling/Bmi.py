# heigth = float(input("Height:"))
# weight = float(input("weight is:"))

# if heigth >3 :
#     raise ValueError("human weight is not more than 3 meter")

# Bmi= weight /heigth**2
# print(Bmi)

#example
def fun1():
  try:
    l =[2,3,5,7]
    i = int(input("enter the index :"))
    print(l[i])
    return 1

  except:
    print("some error occurred")
    return 0

#   finally:
#     print("i am always executed")
      
      # This line executes only if no return statement is executed before it.
    print("i am always executed") 


x = fun1()
print(x)