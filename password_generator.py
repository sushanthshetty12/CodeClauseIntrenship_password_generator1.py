import secrets
import string

def generate_password(length=12, use_numbers=True, use_symbols=True, use_uppercase=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password(account, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{account}: {password}\n")
    print("Password saved successfully.")

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_numbers, use_symbols, use_uppercase)
    print("Generated Password:", password)
    
    save_option = input("Do you want to save this password? (y/n): ").lower()
    if save_option == 'y':
        account = input("Enter account name: ")
        save_password(account, password)