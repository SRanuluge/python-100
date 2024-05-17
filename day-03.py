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


# -----------------------------------------------------

print("Welcome to the rollercoaster!")
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
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


# ------------------------------
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

def count_letters(name, letters):
    count = 0
    for letter in letters:
        count += name.lower().count(letter)
    return count

def love_true_score(name1, name2):
    combined_name = name1 + name2
    
    # Count occurrences of 'TRUE'
    true_count = count_letters(combined_name, 'true')
    
    # Count occurrences of 'LOVE'
    love_count = count_letters(combined_name, 'love')
    
    # Combine counts to form a two-digit number
    score = int(f"{true_count}{love_count}")
    
    return score
score = love_true_score(name1, name2)
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else :
  print(f"Your score is {score}.")


# -----------------------------
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")