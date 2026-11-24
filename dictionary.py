# Dictionary: A data structure of python which stores information in the form of key-value pair
employee = {
    "name" : "Ahmed",
    "age" : 25,
    "department": "IT",
    "salary": 45000
}
print(employee)

# Accessing values through dictionary
employee = {
    "name" : "Ahmed",
    "age" : 25,
    "department": "IT",
    "salary": 45000
}
print(employee["department"])
print(employee["salary"])
print(employee["name"])

# Adding new data in dictionary
student = {
    "name": "Ali",
    "age": 22
}
student["city"] = "Peshawar"
student["course"] = "Python"
print(student)

# Updating existing value in dictionary
student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}
student["age"] = 23
student["course"] = "Artificial Intelligence"
print(student)

# Deleting a specific element from dictionary del()
employee = {
    "name": "Ahmed",
    "age": 25,
    "department": "IT",
    "salary": 45000
}
del employee["salary"]
print(employee)

# pop() method: It removes specific key-value pair from the dictionary and also return its value
student = {
    "name": "Ali",
    "age": 23,
    "course": "Python"
}
removed_course = student.pop("course")
print(removed_course)
print(student)

# clear() method: It removes all the key-value pairs in dictionary, but still variable dictionary exists
student = {
    "name": "Ali",
    "age": 23,
    "course": "Python"
}
student.clear()
print(student)

# len() method: It counts total key-value pairs in dictionary
student = {
    "name": "Ali",
    "age": 23,
    "course": "Python",
    "city": "Peshawar",
    "marks": 85
}
print(len(student))

# key() method: It returns all the keys in dictionary
student = {
    "name": "Ali",
    "age": 23,
    "course": "Python",
    "city": "Peshawar"
}
print(student.keys())

# values() method: It returns all the values in dictionary
student = {
    "name": "Ali",
    "age": 23,
    "course": "Python",
    "city": "Peshawar"
}
print(student.values())

# items() method: It gives correspondence value of key and value
employee = {
    "name": "Ahmed",
    "age": 25,
    "department": "IT",
    "salary": 45000
}
print(employee.items())

# get() method: It is used to get the value of key 
employee = {
    "name": "Ahmed",
    "age": 25,
    "department": "IT"
}
print(employee.get("department"))
print(employee.get("Salary"))

# Dictionary with for Loop
student = {
    "name": "Ahmed",
    "age": 24,
    "course": "Python",
    "city": "Abbottabad"
}
for key in student:
    print(key)

# printing dictionary value using for loop
student = {
    "name": "Ahmed",
    "age": 24,
    "course": "Python",
    "city": "Abbottabad"
}
for value in student.values():
    print(value)

# Accessing keys and values together using for loop items()
student = {
    "name": "Ahmed",
    "age": 24,
    "course": "Python",
    "city": "Abbottabad"
}
for key, value in student.items():
    print(key, value)