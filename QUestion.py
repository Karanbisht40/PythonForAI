#ques-write a program to read a text from a given file certificate.txt and find wheather it contains the word live

#open 
file = open("certificate.txt", "r")

# #read
containvalue=  file.read()

containvalue = containvalue.lower() #lower case

if"live" in containvalue:
    print("yes live word is present in the file")
else:
    print("not contain any live word")

 #open a file called report.txt in write mode
file = open("report.txt", "w")
file.write("this is a demo text that inserted through the code")

#ques-read only the first line of the textfile.txt
with open("textfile.txt","r") as f:
    data = f.readline()
    print("data is :", data)
    f.close()

#ques- print how many lines are present in textfile.txt
with open("textfile.txt", "r") as f:
    listsofLines = f.readlines()
    print("the total number of lines are", len(listsofLines))