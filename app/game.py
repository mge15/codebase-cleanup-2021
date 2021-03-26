
from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    Params:
        choice1 and choice2 are strings that are one of the valid options in the game
    """
    winners = {
            "rock":{
                "rock": None,
                "paper": "paper",
                "scissors": "rock",
            },
            "paper":{
                "rock": "paper",
                "paper": None,
                "scissors": "scissors",
            },
            "scissors":{
                "rock": "rock",
                "paper": "scissors",
                "scissors": None,
            }
    }
    return winners[choice1][choice2]

if __name__ == "__main__":

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner(u, c)

    if winner == u:
        print("You Won!")
    elif winner == c:
        print("Computer Won!")
    elif winner == None:
        print("Tie!")
