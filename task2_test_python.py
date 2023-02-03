# Задание на стоимость звонка

t_h, t_m = int(input("Введите час: ")), int(input("Введите минуты: "))
dt = int(input("Время длительности разговора (в минутах): "))
s = int(input("Стоимость минуты разговора: "))
d = int(input("День недели (1-7): "))

t = t_h * 60 + t_m              # Время начала разговора
price = 0

for i in range(t, t + dt + 1):
    if d == 6 or d == 7:
        if 0 <= i < 480 or 1320 <= i <= 1439:
            price += s - s * (0.1 + 0.2)
        else:
            price += s - s * 0.1
    else:
        if 0 <= i < 480 or 1320 <= i <= 1380:
            price += s - s * 0.2

    if i - t >= 1440:
        d += 1
        t = i-t
    if d >= 8:
        d = 1

print(price)