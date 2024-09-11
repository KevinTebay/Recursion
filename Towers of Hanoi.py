def towers_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        towers_of_hanoi(n - 1, source, auxiliary, target)
        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")
        # Move the n-1 disks from auxiliary peg to target peg
        towers_of_hanoi(n - 1, auxiliary, target, source)

towers_of_hanoi(3, 'A', 'C', 'B')
