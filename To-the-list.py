a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operation (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error")
else:
    print("Invalid")