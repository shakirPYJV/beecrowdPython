values = [int(i) for i in input().split()]
num_1 = values[0]
num_2 = values[1]
num_3 = values[2]

formula= (num_1+num_2+abs(num_1-num_2))/2

if formula > num_3:
	print(f"{int(formula)} eh o maior")
else :
	print(f"{int(num_3)} eh o maior")
