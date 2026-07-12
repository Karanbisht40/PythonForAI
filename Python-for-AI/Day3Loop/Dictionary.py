students ={
    "name": "karan",
    "age": 25,
    "city": "up"
}
print(type(students))
print(students["name"])#accessing value
print(students)

#update
students["city"]="hyderbad"
print(students)

#add new value key-value
students["favsub"]= "Math"
print(students)

#removing items
students.pop("city")
print(students)

print(students.keys())
print(students.values())
print(students.items())
print(students.get("name"))
