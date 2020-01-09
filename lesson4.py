import random

list_100 = []
list_20 = ['lesha', 'masha', 'sasha', 'dasha', 'misha', 'vasya', 'vanya', 'lena', 'nastya', 'mitya', 'dima',
           'kostya', 'andrey', 'anton', 'serge', 'marina', 'lyuda', 'kolya', 'yulya', 'pasha']
# сначала сделал с randint, но не нашел куда засунуть def, и решил не стирать, потому что ответ тоже правильный
for i in range(0, 100):
    r = random.randint(0, 19)
    list_100.insert(i, list_20[r])
# потом узнал, что choices нужно было использовать
def f_1(x, y):
    return random.choices(x, k=y)
print(f_1(list_20, 100))
# ниже задаем функцию выведения самого часто-встречающегося имени из списка 100 имен
def f_2(x):
    c = list_100.count(list_20[0])
    for i in range(0, 19):
        frequency = list_100.count(list_20[i])
        if frequency >= c :
            c = frequency
            name = list_20[i]
    return (name, c)
print(f_2(list_100))
# ниже задаем функцию выведения первой буквы самого редко-встречающегося имени из списка 100 имен
litera = list(map(lambda x: x[0], list_100))
litera_unique = list(set(litera))
def f_3(x):
    c_1 = litera.count(litera_unique[0])
    for i in range(0, len(litera_unique)):
        frequency_1 = litera.count(litera_unique[i])
        if frequency_1 <= c_1:
            c_1 = frequency_1
            litera_1 = litera_unique[i]
    return (litera_1, c_1)
print(f_3(litera))
