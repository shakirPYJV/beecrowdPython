n = int(input())
for i  in [3600,60,1]:
	print(f"{n//i}")
	n = n%i