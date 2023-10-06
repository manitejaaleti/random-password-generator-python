import random
import string

def generate_password(length):
    # Define a string containing all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Random Password Generator")
    print("=========================")
    length = int(input("Enter the length of the password: "))

    if length < 1:
        print("Password length should be at least 1.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
