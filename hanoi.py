def hanoi(n, source, target, auxiliary, move_counter):
    if n > 0:
        move_counter = hanoi(n - 1, source, auxiliary, target, move_counter)
        move_counter += 1
        print(f"Move {n} from rod {source} to rod {target} (Move {move_counter})")
        move_counter = hanoi(n - 1, auxiliary, target, source, move_counter)
    return move_counter

def main():
    print("Towers of Hanoi")
    tower_size = int(input("Enter the number of disks: "))
    moves = hanoi(tower_size, 'A', 'C', 'B', 0)
    print(f"Total moves: {moves}")

if __name__ == "__main__":
    main()