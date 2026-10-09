monthlyelecusage = int(input("Enter your monthly electricity usage in kWh: "))
if monthlyelecusage < 0:
    print("Invalid input. Please enter a positive value.")
elif monthlyelecusage <= 100:
    bill = monthlyelecusage * 0.8
elif monthlyelecusage <= 300:
    bill = 100 * 0.8 + (monthlyelecusage - 100) * 1.2
else:
    bill = 100 * 0.8 + 200 * 1.2 + (monthlyelecusage - 300) * 1.5
print("Your electricity bill is: AZN", bill)
print("starting fee is 0.8 AZN for the first 100 kWh, 1.2 AZN for the next 200 kWh, and 1.5 AZN for any usage above 300 kWh.")