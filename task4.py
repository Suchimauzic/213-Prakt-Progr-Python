m, d = int(input('Введите месяц рождения (1-12): ')), int(input('Введите день рождения: '))
dMonth = [20, 18, 20, 20, 20, 21, 22, 23, 23, 23, 22, 21]
cMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nMonth = ['козерог', 'водолей', 'рыбы', 'овен', 'телец', 'близнецы', 'рак', 'лев', 'дева', 'весы', 'скорпион', 'стрелец']

for i in range(len(nMonth)):
    if i+1 == m:
        if i < 11:
            if 1 <= d <= dMonth[i]:
                print('Ваш знак зодиака: ' + nMonth[i])
            elif dMonth[i]+1 <= d <= cMonth[i]:
                print('Ваш знак зодиака: ' + nMonth[i+1])
        elif i+1 == 11:
            print('Ваш знак зодиака: ' + nMonth[0])