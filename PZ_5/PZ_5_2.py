#Описать функцию AddRightDigit(D, K), добавляющуюю  к целому числу положительному
#числу К справа цифру D(D - входной параметр целого типа лежащий в диапазоне от 0 до 9, К - параметр целого типа,
# являющийся входным и выходный одновременно). С помощью функции последовательно добавиить к данному числу К справа данный цифры D1,D2,
# выводя рез-тат каждого добавления
D1= int(input("Введите цифру от 0 до 9: "))
K = int(input("Введите число К: "))

if type(D1)!=int:
  print("Введите целую цифру от 0 до 9")
  D1= int(input("Введите цифру от 0 до 9: "))

if not(0<=D1<=9):
    print("Введите число в указанном диапазоне")
    D1 = int(input("Введите цифру от 0 до 9: "))

def AddRightDigit(D2):
    print("Промежуточный результат с D1: ",K, D1, sep="")
    print("Конечный результат с D2: ",K, D1,D2,  sep="")

AddRightDigit(D2=int(input("Снова введите цифру от 0 до 9: ")))