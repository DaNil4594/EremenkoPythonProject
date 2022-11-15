# Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть
# числа, меньшие своих соседей).

from random import randint
n = int(input("Введите размер списка: "))
i=0# счетчик
b=[]# список в который будут записываться локальные минимумы
a = [randint(0, 100) for i in range(0, n)]
print("Рандомно заполненный список: ", a)
for i in a:
    if a.index(i)==0:
        if a[a.index(i)]<a[a.index(i)+1]:
            b.append(i)
    elif a.index(i)==a.index(a[-1]):
        if a[a.index(i)]<a[a.index(i)-1]:
            b.append(i)
    else:
        if a[a.index(i)]<a[a.index(i)-1] or a[a.index(i)]<a[a.index(i)+1]:
            b.append(i)

c=[]
i=0#Обнуляем счетчик
for i in b:
    c.append(i**2)
    i+=1

print("Список с локальными минимумами: ",b)
print("Результат возведения в квадрат: ", c)

