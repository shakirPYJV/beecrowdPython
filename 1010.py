a1 = input().split()[1:]
num_1 = int(a1[0])
price_1 = float(a1[1])
sum_1 = num_1*price_1

a2 = input().split()[1:]
num_2 = int(a2[0])
price_2 = float(a2[1])
sum_2 = num_2*price_2

total = sum_1 + sum_2
print(f"VALOR A PAGAR: R$ {total:.2f}")