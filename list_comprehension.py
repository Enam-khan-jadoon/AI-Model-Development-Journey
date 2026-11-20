numbers = [2, 4, 6, 8]
squares = [number * 2 for number in numbers]
print(squares)

numbers = [3, 5, 7]
result = [number * 3 for number in numbers]
print(result)

# List Comprehsension with if statement
ages = [12, 18, 25, 15, 30]
result = [age for age in ages if age>=18]
print(result)

# List Comprehension with if else statement
marks = [35, 75, 45, 90, 25]
result = ["Pass" if number>=50 else "Fail" for number in marks]
print(result)