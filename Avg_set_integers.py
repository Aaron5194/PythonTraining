n = int(input())

total = 0

for i in range(n):
    num = int(input())
    total += num

average = total / n
print(f"The average is: {average:.2f}") 
