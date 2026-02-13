import random, string

my_word = input("enter the password: ")
length = int(input("enter the length of the password: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = " ".join(random.choice(chars) for i in range(length))

generated_password = my_word + password
print(f"suggested password: {generated_password}")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = string.digits
symbols = string.punctuation

has_lower = False
has_upper = False
has_nums = False
has_symbols = False

for chars in password:
    if chars in lower:
        has_lower = True
    if chars in upper:
        has_upper = True
    if chars in nums:
        has_nums = True
    if chars in symbols:
        has_symbols = True

if has_lower and has_upper and has_nums and has_symbols:
    print("\nStrong Password!")
    print("\n--- confirm new password ---")
    pass1 = input("type the password again: ")

    if pass1 == password:
        print("success! password match.")
    else:
        print("error! password do not match.")
else:
    print("\nWeak Password! Your Password is not Strong Enough!")
    if not has_lower:
        print("-missing lowercase")
    if not has_upper:
        print("-missing uppercase")
    if not has_nums:
        print("-missing numbers")
    if not has_symbols:
        print("-missing symbols")
