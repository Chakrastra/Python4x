#Permutations using recursion


def generate_permutations(string):
    # Base case: if the string is empty return a list with an empty string
    if len(string) == 0:
        return [""]

    # List to store permutations
    permutations = []

    # Iterate through the string and generate permutations
    for i in range(len(string)):
        # Get the current character
        current_char = string[i]

        # Form the remaining string after removing the current character
        remaining_string = string[:i] + string[i+1:]

        # Recursively generate all permutations of the remaining string
        for permutation in generate_permutations(remaining_string):
            # Concatenate the current character with each permutation of the remaining string
            permutations.append(current_char + permutation)

    return permutations

# Example usage
string = "CODE"
all_permutations = generate_permutations(string)
for perm in all_permutations:
    print(perm)
