import string


# Function to normalise player input

def normalise_input(user_input, white_list):
    # Step 1: Remove leading and trailing spaces and make it lowercase
    user_input = user_input.strip()
    user_input = user_input.lower()

    # Step 2: Remove punctuation
    for char in string.punctuation:
        user_input = user_input.replace(char, '')

    # Step 3: Split the input into words
    words = user_input.split()

    # Step 4: Keep only words in the whitelist
    normalised_words = []
    for word in words:
        if word in white_list:
            normalised_words.append(word)

    return normalised_words


whitelist = ["go", "take", "drop", "inspect", "check", "score", "i", "inventory", "room", "north", "east", "west", "south"]

# Example usage:
"""
user_input = "Go north and take the key!"
normalised_input = normalise_input(user_input, whitelist)
"""
