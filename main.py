"""
this is our main

ship is a tuple: ((x,y), length, h(for horizontal)/v(for vertical))
"""

def help():
    print('This is a battleship game for two players on 10 on 10 field')
    print('Wait for your turn and then enter coordinates (x,y) and the direction (v for vertical, h for horizontal')
    print('Write just (x,y) for shot')
    print('Example for ship: "b 4 v"')

def read_placement():
    """
    Reads and checks user input
    """
    user_input = input().split()
    return user_input


if __name__ == "__main__":
    field1,field2 = [([0] for i in range(11)) for i in range(11)], [([0] for i in range(11)) for i in range(11)]
    ships1,ships2 = ['*', '**', '***'], ['*', '**', '***']

    help()
    # placement_over = False
    # for ship in ships1:
    #     print(f'Next ship is {ship}')
    #     coordinates = read_placement()
    #     # field1 = place(field1, coordinates)
    # for ship in ships2:
    #     print(f'Next ship is {ship}')
    #     coordinates = read_placement()
    #     # field1 = place(field1, coordinates)
