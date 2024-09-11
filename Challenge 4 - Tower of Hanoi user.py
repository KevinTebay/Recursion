def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from " + source + " to " + target)
    else:
        towers_of_hanoi(n - 1, source, auxiliary, target)
        print("Move disk " + str(n) + " from " + source + " to " + target)
        towers_of_hanoi(n - 1, auxiliary, target, source)

# Get the number of disks from the user
number_of_disks = int(input("Enter the number of disks: "))

source_peg = 'A'
target_peg = 'C'
auxiliary_peg = 'B'

print("\nSolving Towers of Hanoi for", number_of_disks, "disks...\n")
towers_of_hanoi(number_of_disks, source_peg, target_peg, auxiliary_peg)
