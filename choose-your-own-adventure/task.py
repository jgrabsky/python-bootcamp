print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child ticket price is $5.")
        ticket_price = 5
    elif age <= 18:
        print("Youth ticket price is $7.")
        ticket_price = 7
    else:
        print("Adult ticket price is $12.")
        ticket_price = 12

    want_photo = str(input("Do you want to have a photo take?  Type y for Yes and n for No"))
    if want_photo == "y":
        ticket_price += 3

    print(f"Your ticket price is ${ticket_price}")
else:
    print("You cannot ride the rollercoaster")
