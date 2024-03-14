a = input()
print("NOTAS:")
b = int(float(a))
for i in [100,50,20,10,5,2]:
	print(f"{b//i} nota(s) de R$ {i}")
	b = b%i
print("MOEDAS:")
print(f"{b%2} moeda(s) de R$ 1")
# print(f"{b//1}moeda(s) de R$ 1")
c = abs(float(a))
# c = c - b
for i in [0.50,0.25,0.10,0.05,0.01]:
	print(f"{(c//i):.0f} moeda(s) de R$ {i}")
	c = c%i 
	
