#Написать программу, которая:
#- Создаёт список из 6 строк (*строки определяются в коде, на ваш вкус*).
#- Подсчитывает количество строк, содержащих букву `д`.
#- Использует циклы для подсчета.
list=["привет", "как", "chjd", "добрый","обедддд","трамп"]
count=0
for i in list:
    if "д" in i:
        count+=1
print(count)            