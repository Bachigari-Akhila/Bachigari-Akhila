def generate_password(seed, length):
    # Define character sets for the password
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()_-+=[]{}|:;<>,.?/~"

    # Combine all character sets
    all_characters = lower_case + upper_case + digits + special_characters

    # Initialize the password with an empty string
    password = ""

    # Generate the password using the hash function and seed
    for _ in range(length):
        # Get a hash value based on the seed and current iteration
        hashed_value = hash((seed, _))
        # Convert the hash value to a positive number
        positive_value = hashed_value % len(all_characters)
        # Append the corresponding character to the password
        password += all_characters[positive_value]

    return password

if __name__ == "__main__":
    seed = 42  # You can change this seed value to get different passwords
    password_length = 12  # You can change this to set the desired password length
    generated_password = generate_password(seed, password_length)
    print("Generated Password:", generated_password)
