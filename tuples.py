# We cannot update tuples

cities = ("Islamabad", "Abbottabad", "Haripur", "Lahore")
print(cities)

cities = ("Islamabad", "Abbottabad", "Haripur", "Lahore")
print(cities[0])

cities = ("Islamabad", "Abbottabad", "Haripur", "Lahore")
print(cities[-1])

# Why tuples are immutable
# colors = ("Blue", "Green", "Red")
# colors[1] = "Black"
# print(colors)

# Tuple length

subjects = ("Maths", "English", "Science", "Computer", "Biology")
print(len(subjects))

# Tuple Count Method
fruits = ("Apple", "Mango", "Banana", "Apple", "Orange", "Apple")
print(fruits.count("Apple"))

# Tuple index
cities = ("Islamabad", "Lahore", "Karachi", "Peshawar", "Lahore")
print(cities.index("Lahore"))

# Tuple iteration using for loop
subjects = ("Maths", "English", "Science", "Computer", "Biology")
for subject in subjects:
    print(subject)

# Tuple Membership (in and not in)
products = ("Laptop", "Mobile", "Keyboard", "Mouse")
print("Keyboard" in products)

products = ("Laptop", "Mobile", "Keyboard", "Mouse")
print("Tablet" not in products)
