import random
import sys

def draw_card(deck):
    return random.choice(deck)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to Blackjack")

play_blackjack = "y"
while play_blackjack == "y":

    my_cards = []
    my_cards.append(draw_card(cards))
    my_cards.append(draw_card(cards))
    print(f"Your cards: {my_cards}")

    dealer_cards = []
    dealer_cards.append(draw_card(cards))
    dealer_cards.append(draw_card(cards))
    print(f"Computer's first card: [{dealer_cards[0]}, X]")

    hit_me = "y"
    player_over_twenty_one = sum(my_cards) > 21
    while hit_me == "y" and not player_over_twenty_one:
        hit_me = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        my_cards.append(draw_card(cards))
        print(f"Your cards: {my_cards}")
        player_over_twenty_one = sum(my_cards) > 21
        if player_over_twenty_one:
            print("You bust!")

    if not player_over_twenty_one:
        print(f"Computer's cards: {dealer_cards}")
        game_over = False
        while not game_over:
            if sum(dealer_cards) > 21:
                print("Dealer busts, you win!")
                game_over = True
            elif sum(dealer_cards) == sum(my_cards):
                print("Tie")
                game_over = True
            elif sum(dealer_cards) > sum(my_cards):
                print("Dealer wins")
                game_over = True
            else:
                dealer_cards.append(draw_card(cards))

    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
