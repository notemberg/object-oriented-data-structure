# Explanation:
# The tower_of_hanoi function solves the problem by moving n-1 disks to an auxiliary peg, then moving the nth disk to the target, and finally moving the n-1 disks from the auxiliary peg to the target.
# The base case is when there's only one disk to move, which is directly moved from the source to the target.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

# Example usage:
tower_of_hanoi(3, 'A', 'C', 'B')