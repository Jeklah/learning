import random
import sys


def launch():
    launch_prompt = input(
        "Welcome !, this is my Rock, Paper, Scissors game would you like to play ? (Y/N)").lower()
    if launch_prompt == "n":
        sys.exit()
    elif launch_prompt == "y":
        return
    else:
        print("Invalid choice")


def play_again() -> bool:
    if (input(
            "Would you like to play again type (n) to quit and (y) to play again ? ")).lower() == "y":
        return True
    else:
        return False


def choices_list() -> str:
    pc_choices = ["rock", "paper", "scissors"]
    pc_choice = random.choice(pc_choices)
    player_choice = input(
        "Chose between ('rock','paper','scissors') or type 'quit' to exit : ").lower()
    print(f"Choices were :  \n-Player  : {player_choice} \n-Pc : {pc_choice}")
    if player_choice == "quit":
        sys.exit()
    if player_choice not in pc_choices:
        print("Invalid choice please chose correctly")
    return player_choice


def playing(player_choice: str):
    pc_choices = ["rock", "paper", "scissors"]
    pc_choice = random.choice(pc_choices)
    print(f'PC chose: {pc_choice}')
    match player_choice:
        case "rock":
            game(
                pc_choice, "Tie !", "You lose ! ", "You WIN  !"
            )
        case "paper":
            game(
                pc_choice, "you WIN !", "Tie !", "You lose !"
            )
        case "scissors":
            game(
                pc_choice, "You lose !", "You WIN !", "Tie !"
            )


def game(pc_choice: str, pc_rock: str, pc_paper: str, pc_scis: str):
    if pc_choice == "rock":
        print(pc_rock)
    elif pc_choice == "paper":
        print(pc_paper)
    else:
        print(pc_scis)


def game_loop():

    replay = True

    while replay:
        launch()
        choice = choices_list()
        playing(choice)
        replay = play_again()

    print("Thanks for playing !")
    sys.exit()


def main():
    game_loop()


if __name__ == "__main__":
    main()
