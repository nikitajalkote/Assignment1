import re

def check_password_strength(password):
    # length check
    length_check = len(password) >= 8
    
    # case check
    case_check = any(c.isupper() for c in password) and any(c.islower() for c in password)
    
    # Digit check
    digit_check = any(c.isdigit() for c in password)
    
    # Special character check
    special_char_check = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # All criteria met
    return length_check and case_check and digit_check and special_char_check

# user input
user_password = input("Enter your password: ")

# Check password strength
if check_password_strength(user_password):
    print("Password is strong.")
else:
    print("Password is weak.Please strenthen your password.")
