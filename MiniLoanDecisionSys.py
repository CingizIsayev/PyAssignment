age = int(input("Enter your age: "))
montlysalary = float(input("Enter your monthly salary: "))
requestedloan=float(input("Enter the requested loan amount: "))
if age < 18:
    print("You are not eligible for a loan due to age restrictions. REJECTED")
elif age >= 18:
    if montlysalary < 500``:
        print("You are not eligible for a loan due to low salary. REJECTED")
    elif montlysalary >= 500:
        if requestedloan > monthlysalary * 10:
            print("You are not eligible for a loan due to high requested amount. REJECTED")
        elif requestedloan <= monthlysalary * 10:
            print("Congratulations! Your loan application is APPROVED.")