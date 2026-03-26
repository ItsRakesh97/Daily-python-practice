num = [1,2,2,3,4,5,6]
unique = []

for i in num:
    if i not in unique:
        unique.append(i)

print(unique)