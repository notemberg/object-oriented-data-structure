# Explanation:
# The main function generate_permutations checks if index has reached the end of the list. If so, it prints the current permutation.
# Instead of using a for loop, a helper function swap_and_generate is defined inside the main function. This helper function recursively swaps the current element with others starting from the current index.
# After swapping, the function makes a recursive call to generate permutations for the next index.
# The swap is undone (backtracking) before moving to the next element to ensure that the function explores all possible permutations.

def generate_permutations(elements, index=0):
    if index == len(elements):
        print(elements)
        return
    
    # Recursive step: swap elements and generate permutations
    def swap_and_generate(i):
        if i >= len(elements):
            return
        elements[index], elements[i] = elements[i], elements[index]  # swap
        generate_permutations(elements, index + 1)
        elements[index], elements[i] = elements[i], elements[index]  # backtrack
        swap_and_generate(i + 1)  # move to the next element for swapping
    
    swap_and_generate(index)

# Example usage:
generate_permutations([1, 2, 3,4,5,6,7])