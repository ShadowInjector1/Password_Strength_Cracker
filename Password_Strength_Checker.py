import re 

def check_password_strength(password):
    if len(password) < 8:
        return "Weak Password: Less than 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Weak Password: No uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak Password: No lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak Password: No number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak Password: No special character"
    return "Strong Password"

user_pass = input("Enter your password")
result = check_password_strength(user_pass)
print(result)