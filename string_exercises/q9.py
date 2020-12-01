str1 = "English = 78 Science = 83 Math = 68 History = 65"

splitted = str1.split()
digits = []
for i in splitted:
    if i.isdigit():
        i = int(i)
        digits.append(i)

print("Sum is ", sum(digits))
print("Average is ", sum(digits) / len(digits))
print(len(digits))

