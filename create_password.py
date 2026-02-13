import random, string

my_word = input("enter the password: ")
length = int(input("enter the length of the password: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = " ".join(random.choice(chars) for i in range(length))

generated_password = my_word + password
print(f"suggested password: {generated_password}")

print("\n--- confirm new password ---")
pass1 = input("type the password: ")
pass2 = input("repeat the password: ")

if pass1 == pass2:
    print("success! password match.")
else:
    print("error! password do not match.")
