
a = int(input("enter any value btw 5 and 9 :"))
      
if(a<5 or a<9):
    raise ValueError("value should be btw 5 and 9")



age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Age:", age)