import random

board_size = 20

board = [' '] * board_size

ships = {
    "Small Ship": 1,
    "Medium Ship": 2,
    "Large Ship": 3
}

player_fleet = {}
for ship_name, ship_size in ships.items():
    while True:
        try:
            pozicia = int(input(f"Enter the starting position (0-{board_size - 1}) for {ship_name}: "))
            if pozicia < 0 or pozicia >= board_size:
                print("Invalid position. Try again.")
                continue

            for i in range(pozicia, pozicia + ship_size):
                if board[i] != ' ':
                    print("Ships overlap. Try again.")
                    break
            else:
                for i in range(pozicia, pozicia + ship_size):
                    board[i] = 'O'
                player_fleet[ship_name] = list(range(pozicia, pozicia + ship_size))
                break
        except ValueError:
            print("Invalid input. Try again.")

computer_fleet_options = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  
]

computer_fleet = random.choice(computer_fleet_options)

while True:
    print("\nPlayer Board:")
    print(" ".join(board))
    print("\nComputer Board:")

    computer_attack = random.randint(0, board_size - 1)
    if computer_attack in player_fleet.values():
        for ship_name, ship_positions in player_fleet.items():
            if computer_attack in ship_positions:
                print(f"Computer hit your {ship_name} at position {computer_attack}.")
                player_fleet[ship_name].remove(computer_attack)
                if not player_fleet[ship_name]:
                    print(f"Your {ship_name} has been sunk!")
                break
        board[computer_attack] = 'X'
    else:
        print(f"Computer missed at position {computer_attack}.")
        board[computer_attack] = 'M'

    if all(len(ships_pozicia) == 0 for ships_pozicia in player_fleet.values()):
        print("\nComputer wins! Your entire fleet has been sunk.")
        break

    try:
        player_attack = int(input("\nEnter your attack position (0-19): "))
        if player_attack < 0 or player_attack >= board_size:
            print("Invalid attack position. Try again.")
        elif board[player_attack] == 'X' or board[player_attack] == 'M':
            print("You've already attacked that position. Try again.")
        else:
            if player_attack in computer_fleet:
                print("Congratulations! You hit the computer's ship.")
                computer_fleet.remove(player_attack)
                board[player_attack] = 'X'
            else:
                print("You missed the computer's ship.")
                board[player_attack] = 'M'

        if len(computer_fleet) == 0:
            print("\nCongratulations! You win! You've sunk the entire computer fleet.")
            break

    except ValueError:
        print("Invalid input. Try again.")
