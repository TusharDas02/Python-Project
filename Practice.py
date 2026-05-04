height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("Enter your age: "))

    if age <= 12:
        print("Child tickets are 50")
        bill = 50
    
    elif age >12 and age <= 18:
        print("Youth tickets are 70")    
        bill = 70   
    
    elif 45 <= age <=55:
        print("You have a free ride!")

    else:
        print("Adult tickets are 120")
        bill = 120

    photo =input("Do you want a photo taken? Y or N:  ")

    if photo == "Y":
        bill += 30

    print(f"Your total bill is {bill}")


else:
    print("Sorry, you cannot ride the roller coaster.")

# print("Welcome to Pizzaria!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ") 

# bill = 0

# if size == "S":
#     bill += 150
# elif size == "M":
#     bill += 200
# elif size == "L":
#     bill += 300

# if pepperoni == "Y":
#     if size == "S":
#         bill += 50
#     else:
#         bill += 100

# if extra_cheese == "Y":
#     bill += 50

# print(f"Your final bill is {bill}")

