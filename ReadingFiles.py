
#normal reading
file = open("ex.txt", "r")
data= file.read()
print(data)
file.close()

#with keyword
with open("ex.txt", "r") as f: 
    data= f.read()
    print("file data", data)