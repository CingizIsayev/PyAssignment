TEA = 2
COFFEE = 4
JUICE = 3
Code = input("insert drink code ").replace( " " , "")
quant = int(input("Insert drink quantity "))
match Code:
	case "T" | "J" | "C" :
		match quant:
			case 0 | 1 | 2 | 3 | 4| 5 | 6 | 7 | 8 | 9 | 10 :
				match Code:
					case "T" :
						total = TEA *quant
						print (f"Tea, amount: {quant}, price : {total} , AZN")
					case "J":
						total = JUICE *quant
						print (f"Juice, amount: {quant}, price : {total}, AZN")
						
					case "C":
						total = COFFEE * quant
						print (f"Coffee, amount: {quant}, price : {total} , AZN")	
			case _:
				print("Invalid quanyity")
	case _:
		print("Invalid drink")
match total:
	case n if n>20:
		print("large drink")
	case _:
		print("regular drink")