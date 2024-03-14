import math

values = [float(i) for i  in input().split()]
a = values[0]
b = values[1]
c = values[2]
pi = 3.14159

area_triangle = 0.5*a*c 
area_circle = pi*math.pow(c,2)
area_trapezium = 0.5*(a+b)*c
area_square = math.pow(b,2)
area_rectangle = a*b

print(f"TRIANGULO : {area_triangle:.3f}")
print(f"CIRCULO : {area_circle:.3f}") 
print(f"TRAPEZIO : {area_trapezium:.3f}")
print(f"QUADRADO : {area_square:.3f}")
print(f"RETANGULO : {area_rectangle:.3f}")
