score = int(input())
if score < 0 or score > 100:
	print("Score is invalid.")
else:
	print("Pass") if score > 50 else print("Fail")