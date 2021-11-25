import random

print("Игра: Угадай Столицу")
print("Если хочешь остановиться, вместо ответа напиши Stop")
print("")
city = dict(
    Россия='Москва',
    Нидерланды='Амстердам',
    Китай='Пекин',
    Норвегия='Осло',
    Франция='Париж',
    Германия='Берлин',
    Румыния='Бухарест',
    Польша='Варшава',
    Бельгия='Бруссель',
    Ирландия='Дублин',
    Япония='Токио',
    Латвия='Рига',)
counter = 0
praviln = 0
restart = True
while restart:
    country, capital = random.choice(list(city.items()))
    print(country)
    answer = str(input("Введи Ответ "))
    if answer == capital:
        print('Супер!')
        praviln += 1
    elif answer == 'Stop':
        restart = False
        break
    else:
        print("Попробуй ещё!")
        counter += 1
    print("Правильные", "Неправильные")
    print("    ", praviln, "        ", counter)
    print("                         ")
