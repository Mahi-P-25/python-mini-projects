def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose (1-4): ")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choice == "1":
    print("Answer:", add(num1, num2))
elif choice == "2":
    print("Answer:", subtract(num1, num2))
elif choice == "3":
    print("Answer:", multiply(num1, num2))
elif choice == "4":
    print("Answer:", divide(num1, num2))
else:
    print("Invalid choice.")
