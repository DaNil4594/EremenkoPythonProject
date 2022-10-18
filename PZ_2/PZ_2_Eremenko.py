m = input('Введите массу(в кг):')
while type(m) !=int:
    try:
        m = int(m)
        try:
            col_vo_tonn = m // 1000
            if col_vo_tonn < 1:
                print("Количество полных тонн - 0")
            elif col_vo_tonn >= 1:
                print(f"Количество полных тонн - {col_vo_tonn}")
        except:
            if type(m) == float or type(m) == str or type(m) == bool:
                print("Введите корректное значение! Целое число!")
    except ValueError:
        print("Ошибка!Введите целое число.")
    break