# Еденицы массы пронумерованы следующим образом:  1- колограмм,
# 2 - миллиграмм, 3 - грамм, 4 - тонна, 5 - центнер. Дан номе еденицы длинны (1- 5)
# и масса  тела в этих еденицах. Найти длинну отрезка в метрах


while True:
    try:
        print("Введите единицу измерения массы от 1 до 5")
        print("1-килограмм")
        print("2-миллиграмм")
        print("3-грамм")
        print("4-тонна")
        print("5-центнер")
        ed_mass = input("Еденица измерения массы:")
        massa = input("Введите значение массы(вещественное число):")

        while type(ed_mass) != int:
            try:
                ed_mass = int(ed_mass)
            except:
                ed_mass = input("Введите число от 1 до 5!:")

        while type(massa) != float:
            try:
                massa = float(massa)
            except:
                massa = float(input("Ведите вещественное число:"))

        if ed_mass == 1:
            print("Масса тела  в килограммах:", massa)
        elif ed_mass == 2:
            print("Масса тела  в килограммах:", massa / 1000000)
        elif ed_mass == 3:
            print("Масса тела  в килограммах:", massa / 1000)
        elif ed_mass == 4:
            print("Масса тела  в килограммах:", massa * 1000)
        else:
            print("Масса тела  в килограммах:", massa * 10)
        break
    except ValueError:
        print("Введите пожалуйста корректные данные")
