def towers_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        towers_of_hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target peg
        print("Move disk %d from %s to %s" % (n, source, target))

        # Move the n-1 disks from auxiliary peg to target peg
        towers_of_hanoi(n - 1, auxiliary, target, source)

def main():
    print("Towers of Hanoi Simulation\n")
    num_disks = int(input("Enter the number of disks: "))

    if num_disks < 1:
        print("Please enter a valid number of disks (greater than 0).")
        return

    source_peg = 'A'
    target_peg = 'C'
    auxiliary_peg = 'B'

    print("\nInitial State: %d disks on %s peg\n" % (num_disks, source_peg))

    # Call the recursive function to solve the Towers of Hanoi problem
    towers_of_hanoi(num_disks, source_peg, target_peg, auxiliary_peg)

    print("\nFinal State: %d disks on %s peg" % (num_disks, target_peg))

if __name__ == "__main__":
    main()
