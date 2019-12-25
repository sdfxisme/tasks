print('task1')
u=int()
for u in range(1,6):
    print(u,0)


print('task2')
n = input('input 10-digit number')
n = int(n)
if n < 1000000000: print('incorrect number')
if n > 9999999999: print('incorrect number')
i=0
while n > 0 :
    if n%10==5 : i=i+1
    n = n//10
print(i)

print('task3')
sum=0
for i in range(1,101):
    sum+=i
print(sum)

print('task4')
m=1
for i in range(1,10):
    i = i + 1
    m = m * i
print(m)

print ('task5')





