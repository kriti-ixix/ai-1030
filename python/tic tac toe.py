# Importing the Libraries
import random

# Global Variables
board = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

# User defined classes and functions
def print_board():
    print()
    print(board['7'] + "|" + board['8'] + "|" + board['9'])
    print("-----")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-----")
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print()


def play_game():
    turn = "X"
    moves = 0

    while True:
        print_board()

        if moves == 9:
            print("Game over")
            break

        choice = input(f"Make your move {turn}: ")

        if board[choice] == " ":
            board[choice] = turn
            moves += 1

            winner = check_winner(turn)

            if winner != "":
                print_board()
                print(f"The winner is {winner}!")
                break

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

        else:
            print("This place is already filled")


def check_winner(current_turn):
    winner = ""

    row_combinations = [board['7']==board['8']==board['9']==current_turn,
                        board['4']==board['5']==board['6']==current_turn,
                        board['1']==board['2']==board['3']==current_turn]

    column_combinations = [board['7']==board['4']==board['1']==current_turn,
                        board['8']==board['5']==board['2']==current_turn,
                        board['9']==board['6']==board['3']==current_turn]

    diagonal_combinations = [board['7']==board['5']==board['3']==current_turn,
                        board['9']==board['5']==board['1']==current_turn]

    if any(row_combinations) or any(column_combinations) or any(diagonal_combinations):
        winner = current_turn

    return winner


# Main function
def main():
    play_game()

main()