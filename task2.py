n = int(input('Введите число копеек 1-99: '))

if 11 <= n <= 14:
    print(str(n) + ' копеек')
elif n % 10 == 1:
    print(str(n) + ' копейка')
elif 2 <= n % 10 <= 4:
    print(str(n) + ' копейки')
elif 5 <= n % 10 <= 9 or n % 10 == 0:
    print(str(n) + ' копеек')