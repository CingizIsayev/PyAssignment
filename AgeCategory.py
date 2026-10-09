enterurage = int(input("Enter your age: "))

if enterurage < 0:
    print("Age cannot be negative.")
elif enterurage < 13:
    print("You are a child.")

elif enterurage < 18:
    print("You are a teenager.")
elif enterurage < 65:
    print("You are an adult.")
else:
    print("You are a senior.")