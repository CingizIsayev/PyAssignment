a =  int(input("Enter the first number: "))
b =  int(input("Enter the second number: "))
c =  int(input("Enter the third number: "))

if a < b and a < c:
    min = a
elif b < a and b < c:
    min = b
else:
    min = c

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

if a<b and a>c or a>b and a<c:
    mid = a
elif b<a and b>c or b>a and b<c:
    mid = b
else:
    mid = c

print("The numbers in ascending order are:", min, mid, max)