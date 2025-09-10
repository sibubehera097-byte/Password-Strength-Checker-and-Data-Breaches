import requests
import hashlib
import string
import random

# Password strength check
def check_strength(password):
    length = len(password) >= 12
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    score = sum([length, upper, lower, digit, special])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

# Check password against HaveIBeenPwned API (k-Anonymity model)
def check_breach(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if suffix in res.text:
        return True
    return False

# Generate a strong password
def suggest_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


# ---- MAIN PROGRAM ----
pwd = input("Enter a password to check: ")

print(f"\nStrength: {check_strength(pwd)}")

if check_breach(pwd):
    print("⚠️ This password has been leaked in data breaches!")
    print(f"Try this instead: {suggest_password()}")
else:
    print("✅ This password was not found in known breaches.")

