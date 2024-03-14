n = int(input())
hour = n//3600
print(f"{hour}",end = ":")
n = n%3600
min = n//60
print(min,end =":")
sec = n%60
print(sec)

	