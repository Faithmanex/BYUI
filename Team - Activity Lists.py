numbers = []
num = -1
while num != 0:
    num = int(input("Enter number: "))
    if num != 0:
        numbers.append(num)

total = 0
for item in numbers:
    total += item

average = total / len(numbers)

maximum = max(numbers)
print(numbers)
print("The sum is:", total)
print("The average is:", average)
print("The largest number is:", maximum)
