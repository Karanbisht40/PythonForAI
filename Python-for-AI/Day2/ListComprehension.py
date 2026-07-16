l=[]
for a in range(1,101):
    l.append(a)    #list method
print(l)

#list comprehension
n=[m for m in range(1,101)]
print(n)

n=[m for m in range(1,101) if m%2==0]
print(n)
