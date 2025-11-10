import game
import main

commands = ["add", "remove", "help", "retry"]

def input(str, grid):
    # Handle empty input
    if not str:
        return
    str = str.lower()
    params = str.split()
    command = params[0]
    
    if command not in commands:
        print("invalid command, please try again\n")
    
    if command == "add":
        number = int(params[1])
        row    = int(params[2])-1
        col    = int(params[3])-1
        game.add(grid, number, row, col)
        print()
        game.display(grid)

    if command == "remove":
        row    = int(params[1])-1
        col    = int(params[2])-1
        game.remove(grid, row, col)
        print()
        game.display(grid)

    if command == "help":
        main.print_instructions()
        print()
        game.display(grid)

    if command == "retry":
        main.main()
