import random
import string

def generate_password(name, surname, birth_date):
    # Create a strong password using the first letter of name, last letter of surname, and birth date
    first_letter = name[0]
    last_letter = surname[-1]
    birth_year = birth_date[:4]
    
    # Generate a random portion of the password
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
    
    # Combine the elements to create the final password
    password = f"{first_letter}{last_letter}{birth_year}{random_chars}"
    
    return password

def check_password_strength(password):
    # Check the strength of a password
    # You can add your own password strength criteria here
    if len(password) >= 8:
        return "Strong"
    elif len(password) >= 6:
        return "Moderate"
    else:
        return "Weak"

while True:
    print("Choose an option:")
    print("1) Password Generator")
    print("2) Password Checker")
    print("3) Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        birth_date = input("Enter your birth date (e.g., YYYYMMDD): ")
        generated_password = generate_password(name, surname, birth_date)
        print("Generated Password:", generated_password)
    elif choice == '2':
        password_to_check = input("Enter the password to check: ")
        strength = check_password_strength(password_to_check)
        print("Password Strength:", strength)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
