print('Узнайте, является ли год високосным')
year = int(input('Введите год: '))
era = int(input('Введите эру\n1 - До нашей эры\n2 - Наша эра\n'))

if era == 1:
    era = 'до нашей эры'
elif era == 2:
    era = 'нашей эры'
else:
    print('Эра указана неверно')
    exit()

if year % 4 == 0 or year % 100 == 0:
    print(str(year) + ' год ' + era + ' - високосный')
else:
    print(str(year) + ' год ' + era + ' - не високосный')