import game
import handler

def get_difficulty():
    print("Select your difficulty: easy/medium/hard")
    while True:
        input_difficulty = input().strip().lower()
        match input_difficulty:
            case "easy":
                return 0
            case "medium":
                return 1
            case "hard":
                return 2
            case _:
                print("Invalid input, please try again:")

def print_instructions():
    print("How to play:\n")
    print("    add    <number> <row (1-9)> <col (1-9)>")
    print("    remove          <row (1-9)> <col (1-9)>")
    print("    retry")
    print("    help")
    print("    quit\n")

def main():
    print("Hello, let's play a game of Sudoku.\n")

    difficulty = get_difficulty()
    print("\nGenerating game...\n")

    grid = game.generate_sudoku()
    grid = game.assign_difficulty(grid, difficulty)
    game.display(grid)

    print("Game generated!\n")
    print_instructions()

    printed_warning = False
    while not game.is_solved(grid):
        if game.is_filled(grid) and not printed_warning:
            print("hmm... something is not right")
            print("Perhaps track back or retry? ")
            printed_warning = True

        print(">>> ", end="")
        handler.input(input().lower(), grid)

    print("\nYou solved it, good job!!!")

if __name__ == "__main__":
    main()
