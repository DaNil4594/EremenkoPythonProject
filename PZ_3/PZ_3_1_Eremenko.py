a,b,c= input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")
# Даны 3 целых числа: А, В, С. Проверить истинность высказывания: " Число В находиться между числами А и С"

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели первое число!")
        a = input("Введите первое число: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели  второе число!")
        b = input("Введите второе число: ")

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели третье число!")
        c = input("Введите третье число: ")

if a<b<c or a>b>c:
    print("Высказывание верно!")
else:
    print("Высказывание ложь.")