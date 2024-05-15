# Data types, Numbers, Operations, Type Conventions, f-Strings
#Primitive data type 

# integer boolean float

# mystery = 734_529.678 => Float

# len is not working with integers

# print("Hello"[0])

# type()

#type conversion or casting

# -------------------------------------------------------

# 2**3 => 2*2*2

#Order => PEMDAS => () ** * / + -

# * /  => equaly important
#+ -  => equaly important

# 8 // 3 divide and convert to int

# calculation goes left to right 
# print(3 * 3 + 3 /3 -3) => 7
# round(a, b) 
# -=  +=
# f-strings 
# print(f"")

# Price Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_split = input("How many people to split the bill? ")
total_bill_float = float(total_bill)
tip_percentage_float = float(tip_percentage)
people_split_float = float(people_split)

tip_percentage_float_final = tip_percentage_float / 100
total_bill_with_tip = total_bill_float * (1 + tip_percentage_float_final)

total_bill_with_tip_float = float(total_bill_with_tip)

each_person_pays = total_bill_with_tip_float / people_split_float
# each_person_pays_rounded = round(each_person_pays, 2)
each_person_pays_rounded = "{:.2f}".format(each_person_pays)
print(f"Each person should pay: ${each_person_pays_rounded}")