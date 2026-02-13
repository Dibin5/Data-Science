import string, maskpass

print("--- create new account ---")

username = input("enter the email: ")

print("(Tip: Press 'Left-Ctrl' while typing to SHOW or HIDE your password)")
new_password = maskpass.advpass(prompt="Enter New Password: ", mask="*")
repeat_password = maskpass.advpass(prompt="Re-type Password: ", mask="*")

if new_password != repeat_password:
    print("error: Password do no match! please try again.")
else:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation

    has_lower = False
    has_upper = False
    has_nums = False
    has_symbols = False

    for char in new_password:
        if char in lower:
            has_lower = True
        if char in upper:
            has_upper = True
        if char in nums:
            has_nums = True
        if char in symbols:
            has_symbols = True

    is_long = len(new_password) >= 8

    if has_lower and has_upper and has_nums and has_symbols and is_long:
        print(f"\nSignup SUCCESS! New Account created for: {username}")
    else:
        print("\nWeak Password! Please include Upper, Lower, Numbers, and Symbols.")
