# Conditional statements, logical operators, code blocks and scope

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

#-----------------------------------------------------------

# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if (number % 2) == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

  print("Welcome to the rollercoaster!")


# -------------------------------------------------------------------
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


# --------------------------------------------

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else :
  bill += 25
  
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else :
    bill += 3
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")