# Set: A data structure of python which stores multiple values in one variable
numbers = {10, 20, 30, 10, 40, 20}
print(numbers)

# Add() method in set
fruits = {"Apple", "Banana", "Mango"}
fruits.add("Orange")
fruits.add("Apple")
print(fruits)

# Remove method in set
subjects = {"Maths", "English", "Science", "Computer"}
subjects.remove("Science")
print(subjects)

# Discard() method in set
colors = {"Blue", "Green", "Red"}
colors.discard("Yellow")
print(colors)

# Pop() method in set
colors = {"Red", "Blue", "Green", "Black"}
removed = colors.pop()
print("Removed color:",  removed)
print("Updated colors:", colors)

# Clear() method in set
students = {"Ali", "Usman", "Talha", "Ahmed"}
students.clear()
print(students)

# Length (len()) method in set
products = {"Laptop", "Mobile", "Keyboard", "Laptop"}
print(len(products))

# Set Membership — in and not in
students = {"Ali", "Usman", "Ahmed", "Talha"}
print("Ahmed" in students)
print("Hassan" not in students)

# Set Iteration using for Loop
countries = {"Pakistan", "USA", "UK", "Canada"}
for country in countries:
    print(country)

# Update() method in set
# It is use to add multiple values in set
students = {"Ali", "Ahmed"}
students.update(["Usman", "Talha", "Hassan"])
print(students)

# Set Union
# Means combining two or more sets to make a new set
students_class_a = {"Ali", "Ahmed", "Usman"}
students_class_b = {"Usman", "Hassan", "Talha"}
result = students_class_a.union(students_class_b)
print(result)

# Set intersection()
students_class_a = {"Ali", "Ahmed", "Usman"}
students_class_b = {"Usman", "Hassan", "Ali"}
result = students_class_a.intersection(students_class_b)
print(result)

# Set difference()
students_class_a = {"Ali", "Ahmed", "Usman"}
students_class_b = {"Usman", "Hassan", "Ali"}
result = students_class_a.difference(students_class_b)
print(result)

students_class_a = {"Ali", "Ahmed", "Usman"}
students_class_b = {"Usman", "Hassan", "Ali"}
result = students_class_b.difference(students_class_a)
print(result)

# Symmetric Difference()
# It takes common elements from both sets and excludes other elements
students_class_a = {"Ali", "Ahmed", "Usman"}
students_class_b = {"Usman", "Hassan", "Ali"}
result = students_class_a.symmetric_difference(students_class_b)
print(result)