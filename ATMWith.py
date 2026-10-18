Balance = 1000
withdraw = int(input("Enter amount to withdraw: "))
if withdraw < 0:
    print("Invalid amount. Please enter a positive value.")

elif withdraw > Balance:
    print("Insufficient balance.")

else:
    Balance -= withdraw
    print("Withdrawal successful. Remaining balance:", Balance)