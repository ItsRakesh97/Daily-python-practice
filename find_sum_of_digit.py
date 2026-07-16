num = int(input("enter the number : "))

total = 0
while num > 0:
    total += num % 10
    num = num // 10

print(total)