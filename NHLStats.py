from Player import Player
import tkinter as tk

enter_name = input("\nEnter a player name: ")


def handle_lowercase(name):
    for i in range(0, len(name)):
        if name[i].isspace():
            name = name[0].upper() + name[1:i] + " " + name[i+1].upper() + name[i+2:]
    return name


def get_player(name):
    name = handle_lowercase(name)
    try:
        player = Player(name)
        while True:
            again = input("Would you like to see stats for another player? Enter 'y/n': ")
            if again == 'y':
                new_player = input("Enter a player name: ")
                get_player(new_player)
            elif again == 'n':
                break
            else:
                print("\nInvalid entry. Try again.\n")
                continue

    except KeyError:
        new_input = input("Name invalid. Enter 'Exit' to exit, or try another player: ")
        if new_input == "Exit" or new_input == "exit":
            return
        else:
            get_player(new_input)


get_player(enter_name)
