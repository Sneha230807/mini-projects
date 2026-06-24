import string
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    has_upper = any(char in string.ascii_uppercase for char in password)
    if has_upper:
        score += 1
    has_lower = any(char in string.ascii_lowercase for char in password)
    if has_lower:
        score += 1
    has_digit = any(char in string.digits for char in password)
    if has_digit:
        score += 1
    has_special = any(char in string.punctuation for char in password)
    if has_special:
        score += 1
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"
user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print(f"Password Strength: {result}")
