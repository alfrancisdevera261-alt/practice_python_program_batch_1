odd_numbers = 0
for i in range(10):
    numbers = int(input("Enter a number: "))
    if numbers % 2 == 1:
        odd_numbers += 1
print(odd_numbers)