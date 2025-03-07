import math

a = float(input())
b = float(input())
c = float(input())


if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  
    area = round(area,2) 
    print(area)
else:
    print("Invalid Triangle")  
