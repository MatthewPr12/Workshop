"""
this is our main

ship is a tuple: ((x,y), length, h(for horizontal)/v(for vertical))
"""

def help():
    print('This is a battleship game for two players on 10 on 10 field')
    print('Wait for your turn and then enter coordinates and the direction (v for vertical, h for horizontal')
    print('Write just (x,y) for shot')
    print('Example for ship: "b4 v"')

def read_placement():
    """
    Reads and checks user input

    Returns: a coordinate and v/h
    Example: ('b4',v)
    """
    return input().split()

def shot(board):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", ]
    print("Choose coordinate")
    for line in board:
        print(line)
    coordinate = input(">>>")
    while True:
        if coordinate[0] in letters:
            column = letters.index(coordinate[0]) + 1
            break
        else:
            print("Your coordinate is not exist")
    while True:
        if 0 <= int(coordinate[1]) <= 9:
            row = letters.index(coordinate[0]) + 1
            break
        else:
            print("Your coordinate is not exist")
    if board[row][column] == "*":
        print("You hit")
        board[row][column] = "X"
    elif board[row][column] == "X" or board[row][column] == ".":
        print("You already shot there")
    else:
        print("You missed")
        board[row][column] = "."
    return board


if __name__ == "__main__":
    field1,field2 = [([0] for i in range(11)) for i in range(11)], [([0] for i in range(11)) for i in range(11)]
    ships1,ships2 = ['*', '**', '***'], ['*', '**', '***']

    help()
    for ship in ships1:
        print(f'Next ship is {ship}')
        coordinates = read_placement()
        # field1 = place(field1, coordinates)
        # print(field_visual(field1))
    for ship in ships2:
        print(f'Next ship is {ship}')
        coordinates = read_placement()
        print(read_placement())
        # field1 = place(field1, coordinates)
        # print(field_visual(field2))
