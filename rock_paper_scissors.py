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
        launch()


def play_again():
    replay_question = input(
        "Would you like to play again type (n) to quit and (y) to play again ? ")
    if replay_question.lower() == "n":
        sys.exit
    elif replay_question.lower() == "y":
        return
    else:
        print("Please type a correct response (Y/N)")
        play_again()


def choices_list(player_choice):
    pc_choices = ["rock", "paper", "scissors"]
    pc_choice = random.choice(pc_choices)
    print(f"Choices were :  \n-Player  : {player_choice} \n-Pc : {pc_choice}")
    player_choice = input(
        "Chose between ('rock','paper','scissors') or type 'quit' to exit : ").lower()
    if player_choice == "quit":
        sys.exit()
    if player_choice not in pc_choices:
        print("Invalid choice please chose correctly")


def playing(player_choice):
    pc_choices = ["rock", "paper", "scissors"]
    pc_choice = random.choice(pc_choices)
    print(f'PC chose: {pc_choice}')
    match player_choice:
        case "rock":
            if pc_choice == "rock":
                print("Tie !")
            elif pc_choice == "paper":
                print("You lose ! ")
            else:
                print("You WIN  !")
            choices_list(player_choice)
            play_again()
        case "paper":
            if pc_choice == "rock":
                print("you WIN !")
            elif pc_choice == "paper":
                print("Tie !")
            else:
                print("You lose !")
            choices_list(player_choice)
            play_again()
        case "scissors":
            if pc_choice == "rock":
                print("You lose !")
            elif pc_choice == "paper":
                print("You WIN !")
            else:
                print("Tie !")

            choices_list(player_choice)
            play_again()


if __name__ == "__main__":
    launch()
    playing(player_choice, pc_choice)
