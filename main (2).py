number = 1
while number <=3:
 print(number)
 number= number + 1

number = 1
while number <= 5:
    print(number)
    number = number + 2

numbers = 10
while numbers>=2:
   print(numbers)
   numbers = numbers -2

num = 5
while num>=1:
   print(num)
   num = num - 1

attempt = 1
while attempt<=5:
   print("Enter your pin")
   attempt = attempt + 1
print("maximum attempts limit reached")

# city = input("Enter your city:")2
# print("Your city is", city)

# Combination of input with while loop
# attempts = 1
# while attempts<=2:
#    pin = input("Enter your pin:")
#    print("Your entered pin is", pin)
#    attempts = attempts + 1
# print("Maximum attempts reached")

# If statement inside while loop
# correct_pin = "2468"
# pin = input("Enter your pin: ")
# if pin == correct_pin:
#    print("Correct pin")
# else:
#    print("Incorrect pin")

# attempts = 1
# correct_pin = "1234"
# while attempts<=3:
#    pin = input("Enter your pin: ")
#    if pin == correct_pin:
#       print("Correct pin")
#       break
#    else:
#       print("Incorrect pin")
#       attempts = attempts + 1
#    print("Program ended")

# Break
number = 1
# while number<=10:
#    print(number)
#    if number == 3:
#     break
#    number = number + 1
# print("Loop stopped")

correct_pin = "1389"
attempt = 4
while attempt>=1:
   pin = input("Enter your pin: ")
   if pin == correct_pin:
      print("Correct Pin")
      break
   else:
      print("Incorrect Pin")
      attempt = attempt - 1
if attempt<1:
   print("Maximum limit reached")



numbers = 10
while numbers>=1:
   print (numbers)
   numbers= numbers -1 