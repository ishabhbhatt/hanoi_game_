
def display_towers(towers):
    print("\n" + "=" * 40)
    print("       TOWER OF HANOI GAME")
    print("=" * 40)

    for name, disks in towers.items():
        print(f"Tower {name}: {disks}")

    print("=" * 40)


def move_disk(towers, source, destination):
    if not towers[source]:
        print("Error: Source tower is empty!")
        return False

    disk = towers[source][-1]

    if towers[destination] and towers[destination][-1] < disk:
        print("Invalid move! Bigger disk cannot go on smaller disk.")
        return False

    towers[source].pop()
    towers[destination].append(disk)

    return True


def play_game():
    print("Welcome to Tower of Hanoi!")

    try:
        n = int(input("Enter number of disks: "))

        if n <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Please enter a valid integer.")
        return

    towers = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": []
    }

    moves = 0
    minimum_moves = 2 ** n - 1

    while len(towers["C"]) != n:
        display_towers(towers)

        print("Enter your move (Example: A C)")
        print("Enter Q to quit.")

        choice = input("Move: ").upper().split()

        if choice == ["Q"]:
            print("Game stopped.")
            return

        if len(choice) != 2:
            print("Please enter source and destination.")
            continue

        source, destination = choice

        if source not in towers or destination not in towers:
            print("Invalid tower! Choose A, B or C.")
            continue

        if source == destination:
            print("Choose two different towers.")
            continue

        if move_disk(towers, source, destination):
            moves += 1
            print("Move successful!")

    display_towers(towers)

    print("\nCONGRATULATIONS!")
    print("You completed Tower of Hanoi!")
    print("Total moves:", moves)
    print("Minimum possible moves:", minimum_moves)


if __name__ == "__main__":
    play_game()
