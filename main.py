import random
import os


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    randNum = random.randint(0, len(cards)-1)
    return cards[randNum]


def calculate_score(cards):
    score = sum(cards)
    for card in cards:
        if card == 11:
            if score > 21:
                cards.remove(card)
                cards.append(1)
                score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0

    else:
        return score

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9
# need to be repeated until the game ends.


# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep
# drawing cards as long as it has a score less than 17.


def compare(user_score, computer_score):
    if (user_score == 0 or computer_score > 21):
        print("User has won")
        return True

    elif (computer_score == 0 or user_score > 21):
        print("Computer has won")
        return True
    else:
        return False



def playGame():
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

    user_cards.append(deal_card())
    computer_cards.append(deal_card())

    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    status = compare(user_score,computer_score)
    if(status == True):
        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {computer_cards}")

    while(not status):
        deal = input("Do you want to draw another card, 'y' for yes and 'n' for no")
        if (deal == 'y'):
            user_cards.append(deal_card())
            print("Dealing card to User...")
            print(f"Your cards: {user_cards}")
            user_score = calculate_score(user_cards)
            if computer_score < 17:
                computer_cards.append(deal_card())
                print("Dealing card to Computer...")
                computer_score = calculate_score(computer_cards)
            status = compare(user_score, computer_score)
        elif(deal == "n"):
            print(f"Your final hand: {user_cards}")
            print(f"Computer's final hand: {computer_cards}")
            if (computer_score == user_score):
                print("It's a draw!")
                status = True
            elif (user_score > computer_score):
                print("User has won!")
                status = True
            elif (computer_score > user_score):
                print("Computer has won")
                status = True
        else:
            print("Invalid Input")

playGame()
playAgain = input("Do you want to play again, 'y' for yes and 'n' for no")
if(playAgain == 'y'):
    playGame()

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start
# a new game of blackjack and show the logo from art.py.
