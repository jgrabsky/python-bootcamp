from os import system

def find_highest_bidder(bid_dictionary):
    highest_bidder = ""
    highest_bid = 0

    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


print("Welcome to the secret auction program!")

bids = {}

more_bidders = "y"
while more_bidders == "y":

    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    more_bidders = input("More bidders? (y/n) ").lower()
    
    system("cls")

find_highest_bidder(bids)

