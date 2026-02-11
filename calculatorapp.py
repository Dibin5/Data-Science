a = float(input("enter the number: "))
operator = input("enter the operator (+, -, *, /): ")
b = float(input("enter the number: "))
result = None

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        print(f"error: the number is not divisible by zero")
else:
    print("invalid operator! use +, -, *, /")
print(f"result:{result:.2f}")
