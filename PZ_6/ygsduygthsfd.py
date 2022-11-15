import random
def PrintList(d):
    i = 0
    while i < 100:
        if (i % 10 != 0) or (i == 0):
            print(d[i], end=' ')
        else:
            print()
            print(d[i], end=' ')
        i += 1
    print()

ListAppend = []
t = 0
while t < 100:
    ListAppend.append(round(random.random(), 2))
    t += 1
print('Исходный список', sep='\n')
PrintList(ListAppend)
ListAppend.sort()
print('Отсортированный список', sep='\n')
PrintList(ListAppend)