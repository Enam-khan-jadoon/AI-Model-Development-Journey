# If Condition
product_price = 800
if product_price >= 1000:
 print("Discount Available")
print("Discount Finished")

# If ELSE
product_price = 800
if product_price >=1000:
 print("Discount is available")
else:
 print("Discount is finished")


 product_price = 1500
if product_price >=1000:
 print("Discount is available")
else:
 print("Discount is finished")

marks = 45
if marks >= 50:
  print("Pass")
else:
  print("Fail")

marks = 75
if marks >= 50:
 print("Pass")
else:
 print("Fail")

#  Elif Condition
marks = 85
if marks >= 80:
 print("Grade A")
elif marks>=70:
 print("Grade B")
else:
 print("Grade C")

marks = 55
if marks >= 80:
 print("Grade A")
elif marks>=70:
 print("Grade B")
else:
 print("Grade C")

 price = 1500
 if price >= 5000:
  print("20% Discount")
 elif price>=2000:
  print("10% Discount")
 else:
  print("No Discount")

price = 6000
if price >= 5000:
 print("20% Discount")
elif price>=2000:
 print("10% Discount")
else:
 print("No Discount")

price = 2500
membership = True
if price >=1000 and membership == True:
 print("Discount approved")
else:
 print("Not approved")

 price = 2500
membership = False
if price >=1000 and membership == True:
 print("Discount approved")
else:
 print("Not approved")

price = 500
membership = True
if price >=1000 and membership == True:
  print("Discount approved")
else:
  print("Not approved")

# Or Operator
price = 1500
membership = False
if price>=1000 or membership==True:
 print("Discount approved")
else:
 print("Discount not approved")

#  Not Operator
membership= True
if not membership:
 print("Please become a member")
else:
 print("Welcome Member")