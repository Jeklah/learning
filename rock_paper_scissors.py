import random
import sys

PC_CHOICES = ["rock", "paper", "scissors"]


def launch():
    launch_prompt = input(
        "Welcome !, this is my Rock, Paper, Scissors game push enter to play or q to exit.").lower()
    if launch_prompt == "q":
        sys.exit()
    elif launch_prompt == "":
        return
    else:
        print("Invalid choice")


def play_again():
    return (
        input(
            "Would you like to play again type (n) to quit and (y) to play again ? "
        )
    ).lower() == "y"


def choices_list(PC_CHOICES: list) -> str:
    player_choice = str
    while player_choice not in ['rock', 'paper', 'scissors', 'quit']:
        player_choice = input(
            "Chose between ('rock','paper','scissors') or type 'quit' to exit : ").lower()
        if player_choice == "quit":
            sys.exit()
        if player_choice not in PC_CHOICES:
            print("Invalid choice please chose correctly")
    return player_choice


def playing(player_choice: str, PC_CHOICES: list):
    pc_choice = random.choice(PC_CHOICES)
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
        choice = choices_list(PC_CHOICES)
        playing(choice, PC_CHOICES)
        replay = play_again()

    print("Thanks for playing !")
    sys.exit()


def main():
    game_loop()


if __name__ == "__main__":
    main()
