age = int(input("Enter your age: "))


if age < 3:
    print(f"Your ticket is free.")
elif 3 <= age <= 12:
    print(f"Your ticket costs $10.")
else:
    print(f"Your ticket costs $15.")