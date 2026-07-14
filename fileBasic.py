#opening the file
file= open("ex.txt", "r") 

#reading the file
data =file.read()
print("data is :" , data)


#if a file under many folder if terminal does not access 
# import os
# file_path = os.path.join(os.path.dirname(__file__), "ex.txt")
# with open(file_path, "r") as file:
#     data = file.read()
# print("Data is:", data)


#appending data
file= open("ex.txt", "a")
file.write("\n this new data write from append")

#create a new file (x)
file= open("exx.txt", "x")
file.write("\n create a file file")
