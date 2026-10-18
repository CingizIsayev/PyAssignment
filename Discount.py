totalpurcahase = float(input("Enter the total purchase amount: "))

if totalpurcahase < 100:
    discount = 0
elif totalpurcahase < 300:
    discount = 0.1
elif totalpurcahase < 500:
    discount = 0.15
else:
    discount = 0.2  

discount_amount = totalpurcahase * discount
final_amount = totalpurcahase - discount_amount 
print("Total purchase amount: $", totalpurcahase)
print("Discount amount: $", discount_amount)
print("Final amount after discount: $", final_amount)
print("Alisverise gore oprem brat")