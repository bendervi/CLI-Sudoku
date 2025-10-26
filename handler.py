import game
import main

commands = ["add", "remove", "help", "retry"]

def input(str, grid):
    str = str.lower()
    params = str.split()
    commando = params[0]
    
    if commando not in commands:
        print("invalid command, please try again\n")
    
    if commando == "add":
        number = int(params[1])
        row    = int(params[2])-1
        col    = int(params[3])-1
        game.add(grid, number, row, col)
        print()
        game.display(grid)

    if commando == "remove":
        row    = int(params[1])-1
        col    = int(params[2])-1
        game.remove(grid, row, col)
        print()
        game.display(grid)

    if commando == "help":
        game.print_instructions()
        print()
        game.display(grid)

    if commando == "retry":
        main.main()
