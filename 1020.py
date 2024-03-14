a = int(input())
years = a//365
print(f"{years} ano(s)")
a = a%365
months = a//30
print(f"{months} mes(es)")
days = a%30
print(f"{days} dia(s)")