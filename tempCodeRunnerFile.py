#reading entire file
# #normal reading
# file = open("ex.txt", "r")
# data= file.read()
# print(data)
# file.close()

# #with keyword
# with open("ex.txt", "r") as f: 
#     data= f.read()
#     print("file data", data)

# #reading line by line   
# with open("textfile.txt", "r") as f:
#      line1= f.readline()
#      line2= f.readline()
#      line3= f.readline()
#      line4= f.readline()
#      line5= f.readline()
#      line6= f.readline()
#      data = f.read()
#      print("line 1", line1)
#      print("line 2", line2)
#      print("line 3", line5)
#      print("line 6", line6)
#      print("data is", data)

# #read all Lines 
# with open("textfile.txt", "r") as f:
#  lines = f.readlines()
#  print(lines)

#  #RENAME FILES
#  import os
#  os.rename("ex.txt", "xe.txt")

#  #delete files
# os.remove("xe.txt")
