import game
import main

commands = ["add", "remove", "help", "retry", "quit"]

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
        if len(params) != 4:
            print("Error: 'add' requires 3 arguments <number> <row (1-9)> <col (1-9)>")
        else:
            try:
                number = int(params[1])
                row    = int(params[2])-1
                col    = int(params[3])-1
                game.add(grid, number, row, col)
                print()
                game.display(grid)
            except:
                print("Error: All values must be Integers.")

    if command == "remove":
        if len(params) != 3:
            print("Error: 'remove' requires 2 arguments <row (1-9)> <col (1-9)>")
        else:
            try:
                row    = int(params[1])-1
                col    = int(params[2])-1
                game.remove(grid, row, col)
                print()
                game.display(grid)
            except:
                print("Error: All values must be Integers")

    if command == "help":
        main.print_instructions()
        print()
        game.display(grid)

    if command == "quit":
        print("Thanks for playing")
        raise SystemExit

    if command == "retry":
        main.main()
