import math
p1 = [float(i) for i in input().split()]
x1,y1 = p1[0],p1[1]  

p2 = [float(i) for i in input().split()]
x2,y2 = p2[0],p2[1]  

distance = math.sqrt(math.pow((x2-x1),2)+(math.pow((y2-y1),2)))