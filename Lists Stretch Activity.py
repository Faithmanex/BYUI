numbers = []
num = -1
print('Enter a list of numbers, type 0 when finished.')
while num != 0:
    num = int(input("Enter number: "))
    if num != 0:
        numbers.append(num)

total = 0
smallest_positive = None
positive_numbers = []

for item in numbers:
    total += item
    if item > 0:
        positive_numbers.append(item)
        if smallest_positive == None or item < smallest_positive:
            smallest_positive = item

average = total / len(numbers)
maximum = max(numbers)

sorted_numbers = sorted(numbers)

print("The sum is:", total)
print(f"The average is:, {average:.3f}")
print("The largest number is:", maximum)
print("The smallest positive number is:", smallest_positive)
print("The sorted list is:")
for num in sorted_numbers:
    print(num)
