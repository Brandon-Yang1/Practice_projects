## using all basics practice 2##

print("Welcome to my 2nd mini project")

numbers = []

total = 0

total_num = int(input("how many numbers do you want to enter?: "))

for i in range(total_num):
    number = int(input("please enter a number: "))
    numbers.append(number)

max = numbers[0]
min = numbers[0]

for number in numbers:
    total = total + number
    if number > max:
        max = number
    if number < min:
        min = number
    

avg = total / total_num

print(total)
print(round(avg , 2))
print(max)
print(min)
