#file not found

try:
    file= open("./Python-for-AI/ExceptionHandling/a_file.txt")

    a_dictionary={"key": "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file =   open("./Python-for-AI/ExceptionHandling/a_file.txt", "w")
    file.write("something")
 
except KeyError as error_message:
    print(f"that key {error_message} not exist")

else:
    content = file.read()
    print(content)

finally:
    # file.close()
    # print("file is closed")
    raise TypeError("this is the error that i made up")
