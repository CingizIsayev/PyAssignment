fee = 2
distance = float(input("Enter the distance traveled in kilometers: "))
if distance <= 5:
    fare = distance * 0.7 + fee
elif distance <= 15:
    fare = 5 * 0.7 + (distance - 5) * 0.6 + fee
else:
    fare = 5 * 0.7 + 10 * 0.6 + (distance - 15) * 0.5 + fee
print("Your taxi fare is: $", fare)
print("Starting fee is $2, $0.7 per km for the first 5 km, $0.6 per km for the next 10 km, and $0.5 per km for any distance above 15 km.")
print("Boltdu aa zordu bes ulduz verersen bratt")