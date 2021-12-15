"""this is our main"""


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
    pass
