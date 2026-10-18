ID = input("Enter your ID: ")
age = input("Enter your age: ")
workshopcode = input("Enter your workshop code: ")
payment = input("Enter your payment amount: ")
if ID.isascii() and ID.isdecimal() and len(ID) == 8:
    print("Student ID is valid")
    if age.isdecimal() and int(age) >= 18 and int(age) <= 65:
        age = int(age)
        match workshopcode:
            case "PY":
                if age >= 16:
                    price = 30
                else:
                    print("You are too young to attend the workshop. REJECTED")
            case "WEB":
                if age >= 16:
                    price = 40
                else:
                    print("You are too young to attend the workshop. REJECTED")
            case "CY":
                if age >= 18:
                    price = 50
                else:
                    print("You are too young to attend the workshop. REJECTED")
        match age:
            case n if n >= 16 and n <= 18:
                discount = 0.2
            case _:
                discount = 0
        discounted_price = price * (1 - discount)
        if payment.isdecimal() and int(payment) >= discounted_price:
            print(f"Payment accepted. You have successfully registered for the {workshopcode} workshop.Your student id is {ID}. final fee is {discounted_price} AZN. THANKS FOR CHOOSING US!!!")
        else:
            print(f"Payment is insufficient. The discounted price for the {workshopcode} workshop is {discounted_price} AZN.")