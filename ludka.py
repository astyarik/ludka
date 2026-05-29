import random
import time

house = True
balance = 500
inv = 0
ch = 0
lu = 0

while balance >= 0:
    x = random.randint(1, 100)

    if x <= 50:
        x = "Common"
        cost = random.randint(10, 40)
    elif x <= 75:
        x = "Rare"
        cost = random.randint(40, 100)
    elif x <= 90:
        x = "Epic"
        cost = random.randint(90, 160)
    elif x <= 99:
        x = "Mythic"
        cost = random.randint(120, 200)
    else:
        x = "Legendary"
        cost = random.randint(500, 1000)
    
    print(f"Баланс: {balance}")
    while ch < 5:
        try:
            if house == True:
                ch = int(input("Выбери от 1 до \n1. Депнуть хату (+1000 рублей)\n2. Крутить кейс (100 рублей)\n3. Выйти\n4. Инвентарь\n>>> "))
            else:
                ch = int(input("Выбери от 1 до \n1. Вернуть хату (-2000 рублей)\n2. Крутить кейс (100 рублей)\n3. Выйти\n4. Инвентарь\n>>> "))
        except:
            print("Неверный вариант")
        if ch > 4:
            print("Ты это, введи цифру существующего варианта!")
        else:
            break

    if ch == 1 and house == True:
        house = False
        balance += 1000
        print(f"Вуаля! Вы бездобный, за то на балансе теперь {balance} рублей!")
        continue

    elif ch == 1 and house == False:
        if balance >= 2000 <= 2100:
            print("А на что лудоманить будешь?")
        elif balance <= 2000:
            print("Какой тебе дом? Накопи сначала! Вот сорви с дерева яблоко, да поешь.")
        else:
            print("Куплено! Приходите ещё)")
            balance -= 2000
            house = True
        continue
    
    elif ch == 3:
        print("Бай-бай, меллстройность!")
        break
    
    elif ch == 4:
        print(f"В вашем инвентаре {inv} вещей")

    elif ch == 2:
        balance -= 100
        print("Крутим...")
        time.sleep(1)
        print("Бэм, бэм бэм бэм...")
        time.sleep(1)
        print("Ух-ты!")
        time.sleep(1)
        print(f"\nИ тебе выпал скин {x}")

        while lu <= 3:
            try:
                lu = int(input(f"1. Сохранишь       или\n2. продашь за {cost}?\n>>> "))
            except:
                print("число введи нужное")
            if lu >= 3:
                print("Введи цифру существующего варианта!")
        if lu == 1:
            print("И зачем...")
            print(f"Количетсво вещей в инвентаре: {inv}")
        if lu == 2:
            balance += cost
            if cost <= 100:
                print("Бли-и-ин, ещё раз?")
            else:
                print("ДА, ДА, ОКУП!")
        break
