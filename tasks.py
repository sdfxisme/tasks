print('task1')
u = int()
for u in range(1, 6):
    print(u, 0)

print('task2')
n = input('input 10-digit number')
n = int(n)
if n < 1000000000:
    print('incorrect number')
if n > 9999999999:
    print('incorrect number')
i = 0
while n > 0:
    if n % 10 == 5:
        i = i + 1
    n = n // 10
print(i)

print('task3')
summa = 0
for i in range(1, 101):
    summa += i
print(summa)

print('task4')
m = 1
for i in range(1, 10):
    i = i + 1
    m = m * i
print(m)

print('task5')
n = input('your number to digit per line')
n = int(n)
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10

print('task6')
num = input('your number to sum digits')
num = int(num)
sum_of_digits = 0
while num > 0:
    sum_of_digits = sum_of_digits + num % 10
    num = num // 10
print(sum_of_digits)

print('task7')
number = input('your number to multiply digits')
number = int(number)
mult_of_digits = 1
while number > 1:
    mult_of_digits = mult_of_digits * (number % 10)
    number = number // 10
print(mult_of_digits)

print('task8')
