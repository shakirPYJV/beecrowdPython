while True:
	try:
		a = input()
		if a.lower()=="exit":
			break
		a = float(a)
		pi = 3.14159
		formula = pi*a**2
		print("A=%.4f"%formula)
	except ValueError:
		print("Please enter a valid input")