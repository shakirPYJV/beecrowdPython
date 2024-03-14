values = [int(i) for i in input().split()]
num_1 = values[0]
num_2 = values[1]
num_3 = values[2]

if num_1>num_2 and  num_1>num_3:
	print(f"{num_1} eh o maior" )
elif num_2 > num_1 and num_2>num_3:
	print(f"{num_2} eh o maior")
else:
	print(f"{num_3} eh o maior")
	

