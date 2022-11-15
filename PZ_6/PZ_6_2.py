#Дан список размера N найти минимальный из его локальных максимумов

from random import randint
n = int(input("Введите размер списка: "))
i=0# счетсик 2
b=[]# список в который будут записываться локальные максимумы
a = [randint(0, 100) for i in range(0, n)]
print("Рандомно заполненный список: "a)
for i in a:
    if a.index(i)==0:
        if a[a.index(i)]>a[a.index(i)+1]:
            b.append(i)
    elif a.index(i)==a.index(a[-1]):
        if a[a.index(i)]>a[a.index(i)-1]:
            b.append(i)
    else:
        if a[a.index(i)]>a[a.index(i)-1] or a[a.index(i)]>a[a.index(i)+1]:
            b.append(i)
print("Список с локальными максимумами: "b)
print("Минимальный из локальных максимумов: ", min(b))
