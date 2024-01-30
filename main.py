"""Rock Paper Scissors Game"""

from random import choice, seed
from rich import print


def computer_choice():
    """Randomly chooses between rock, paper, or scissors"""
    seed()
    choices = ["rock", "paper", "scissors"]
    return choice(choices)


def player_choice():
    choices = ["rock", "paper", "scissors"]
    return choices[int(input("Choose 1 for rock, 2 for paper, or 3 for scissors: "))-1]


def check_winner(p_choice,c_choice):
    match (p_choice, c_choice):
        case "rock", "scissors":
            return "Player"
        case "paper", "rock":
            return "Player"
        case "scissors", "paper":
            return "Player"
        case "rock", "paper":
            return "Computer"
        case "paper", "scissors":
            return "Computer"
        case "scissors", "rock":
            return "Computer"
        case _:
            return "Tie"
    

def round_number():
    return int(input("How many rounds would you like to play? "))


def display_choices():
    print("0: Rock")
    print("1: Paper")
    print("2: Scissors")


def display_all_choices(p_choice, c_choice):
    print(f"[green]Player: {p_choice}[/green] | [red]Computer: {c_choice}[/red]")


def display_winner(winner):
    print(f"[bold blue]{winner} wins![/bold blue]")


def display_final_winner(player_wins, computer_wins):
    if player_wins > computer_wins:
        print(f"[bold blue]Player win the game![/bold blue] Score: {player_wins} - {computer_wins}")
    elif player_wins == computer_wins:
        print(f"[bold blue]Tie game![/bold blue] Score: {player_wins} - {computer_wins}")
    else:
        print(f"[bold blue]Computer win the game![/bold blue] Score: {player_wins} - {computer_wins}")


def main():
    rounds = round_number()
    player_wins = 0
    computer_wins = 0
    for _ in range(rounds):
        player = player_choice()
        computer = computer_choice()
        display_all_choices(player, computer)
        winner = check_winner(player, computer)
        if winner == "Tie":
            print("[bold blue]Tie![/bold blue]")
        else:
            if winner == "Player":
                player_wins += 1
            else:
                computer_wins += 1
            display_winner(winner)
    display_final_winner(player_wins, computer_wins)
    

if __name__ == "__main__":
    main()