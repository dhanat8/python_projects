from itertools import filterfalse
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list: list[int]) -> int:
    """Take a list of cards and return the score calculated from the cards"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0 # if the first round anybody gets 0, the game ends

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game_algorithm():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1 #if set to 0, the game will end.
    is_game_over = False

    for _ in range(2): #deal the first two cards for the user and the computer
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: #or while is_game_over == False:
        # under this while loop, it checks whether there is a winner.
        # If not, the user can keep dealing cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            #this while loop will stop once the user's score exceeds 21
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        # we don't want the computer to keep dealing the card once the score exceeds 17.
        # this is why this while loop is not under the while not is_game_over
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # these will be printed once the game is over

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# this is the actual part the runs the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    game_algorithm()
