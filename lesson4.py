import random
list_100 = []
list_20 = ['lesha', 'masha', 'sasha', 'dasha', 'misha', 'vasya', 'vanya', 'lena', 'nastya', 'mitya', 'dima',
               'kostya', 'andrey', 'anton', 'serge', 'marina', 'lyuda', 'kolya', 'yulya', 'pasha']
# сначала сделал с randint, не не нашел куда засунуть def, решил не стирать
for i in range(0,99):
    r = random.randint(0, 19)
    list_100.insert(i,list_20[r])
print(list_100)
# потом узнал, что choices нужно было использовать
def f(x,y):
    return random.choices(x,k = y)
print(f(list_20, 100))
