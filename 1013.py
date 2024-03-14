values = [int(i) for i in input().split()]
num_1 = values[0]
num_2 = values[1]
num_3 = values[2]

formula= (num_1+num_2+abs(num_1-num_2))/2

major= (formula+num_3+abs(formula-num_3))/2
print(f"{int(major)} eh o maior")
