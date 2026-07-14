

import os
file_path = os.path.join(os.path.dirname(__file__), "mydata.txt")
with open(file_path, "r") as file:
    data =  file.read()
print("data is:", data)