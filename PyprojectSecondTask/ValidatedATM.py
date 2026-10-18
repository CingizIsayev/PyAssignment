BALANCE = 1000
PIN = "0427"
Pin = input().replace(" ", "")
Withdrawal = input().replace(" ", "")

if len(Pin) == 4:
    if Pin == PIN:
        if Withdrawal.isascii() and Withdrawal.isdecimal():
            Withdrawal = int(Withdrawal)
            if Withdrawal > 9 and Withdrawal < 501 and Withdrawal % 10 == 0:
                match Withdrawal:
                    case n if n < 201:
                        fee = 0
                    case n if n > 200:
                        fee = 2

                if Withdrawal + fee > BALANCE:
                    print("Not enough balance")
                else:
                    print(f"You withdrwed {Withdrawal} AZN, the fee is {fee} AZN, remaining balance {BALANCE - (Withdrawal + fee)} AZN")
            else:
                print("Withdrawal amount must be divisible by 10 and must be in range of 10 - 500")
        else:
            print("withdrawal is invalid")
    else:
        print("Pin is incorrect")
else:
    print("Pin must be 4 digits")