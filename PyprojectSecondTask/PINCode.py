PIN = "0427"
pin = input( ).replace (" ", "")
if pin == "":
	print("PIN is required")
if len(pin) == 4:
	if pin.isdecimal( ):
		if pin == PIN:
			print("PIN is correct. Acces granted.")
		else:
			print("PIN is incorrect. Acces Denied")
	else:
		print("PIN must be only digits")
else:
	print("Pin must be 4 digits")