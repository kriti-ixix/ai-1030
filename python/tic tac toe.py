# Importing the Libraries

# Global Variables
board = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

# User defined classes and functions
def print_board():
    print(board['7'] + "|" + board['8'] + "|" + board['9'])
    print("-----")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-----")
    print(board['1'] + "|" + board['2'] + "|" + board['3'])

# Main function
def main():
    print_board()

main()