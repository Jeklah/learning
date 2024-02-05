import random
import sys


def launch():
    launch_prompt = (input(
        "Welcome !, this is my Rock, Paper, Scissors game would you like to play ? (Y/N)")).lower()
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


def playing():
    def choices_list():
        print(
            f"Choices were :  \n-Player  : {player_choice} \n-Pc : {pc_choice}")

    while True:
        pc_choices = ["rock", "paper", "scissors"]
        pc_choice = random.choice(pc_choices)
        player_choice = (input(
            "Chose between ('rock','paper','scissor') or type 'quit' to exit : ")).lower()
        if player_choice == "quit":
            sys.exit()
        if player_choice not in ["rock", "paper", 'scissors']:
            print("Invalid choice please chose correctly")
            continue
        elif player_choice == "rock" and pc_choice == "rock":
            print("Tie !")
            choices_list()
            play_again()
        elif player_choice == "rock" and pc_choice == "paper":
            print("You lose ! ")
            choices_list()
            play_again()
        elif player_choice == "rock" and pc_choice == "scissors":
            print("You WIN  !")
            choices_list()
            play_again()
        elif player_choice == "paper" and pc_choice == "rock":
            print("you WIN !")
            choices_list()
            play_again()
        elif player_choice == "paper" and pc_choice == "paper":
            print("Tie !")
            choices_list()
            play_again()
        elif player_choice == "paper" and pc_choice == "scissors":
            print("You lose !")
            choices_list()
            play_again()
        elif player_choice == "scissors" and pc_choice == "rock":
            print("You lose !")
            choices_list()
            play_again()
        elif player_choice == "scissors" and pc_choice == "paper":
            print("You WIN !")
            choices_list()
            play_again()
        elif player_choice == "scissors" and pc_choice == "scissors":
            print("Tie !")
            choices_list()
            play_again()


launch()
playing()
