import random
import string

length = int(input("enter the length of the password: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = " ".join(random.choice(chars) for i in range(length))
print("print your password is:", password)
