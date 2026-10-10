# function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    elif not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    elif not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        return "Weak: Password must contain at least one special character."
    else:
        return "Strong: Your password is strong."

# test the function
if __name__ == "__main__":
    test_passwords = [
        "password",
        "Password1",
        "Password!",
        "Pass1!",
        "StrongPass1!"
    ]

    for pwd in test_passwords:
        print(f"Password: {pwd} - Strength: {check_password_strength(pwd)}")