# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    food_in_fridge = 50
    money_in_nightstand = 100
    dirt = 0    
    cat_food = 30

    def __init__(self):
        pass

    def __str__(self) -> str:
        return 'Еды доме {}, денег в доме {}, грязи в доме {}, кошачьей еды в доме {}'.format(
            self.food_in_fridge, self.money_in_nightstand, self.dirt, self.cat_food)

class Human:

    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullness = 30

    def __str__(self) -> str:
        return '{} сытость {}, настроение {}'.format(self.name, self.fullness, self.mood)


class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name=name,house=house)
        self.mood = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        self.house.dirt += 5        
        if self.mood < 10:
            return cprint('Муж умер от депресии!', color='red')
        dice = randint(1, 5)
        if self.fullness <= 0:
            return cprint('Муж умер от голода!', color='red')
        if self.fullness < 30:
            self.eat()
        if self.house.dirt > 90:
            self.mood -= 10
        elif self.house.money_in_nightstand < 110:
            self.work            
        if dice == 1:
            self.work()
        if dice == 2:
            self.eat()
        if dice == 3:
            self.pet_cat()
        else:
            self.gaming()

    def pet_cat(self):
        print('Муж погладил кота')
        self.fullness -= 10
        self.mood += 10


    def eat(self):
        if self.house.food_in_fridge < 19:
            self.fullness -= 10
        else:
            self.fullness += 20
            self.house.food_in_fridge -= 20
            print('Муж поел')
            print('В холодильнике осталось {} еды'.format(self.house.food_in_fridge))

    def work(self):
        print('Муж пошел на работу')
        self.fullness -= 10
        self.house.money_in_nightstand += 150

    def gaming(self):
        print('Муж играет в Танки!')
        self.fullness -= 10
        self.mood += 20
class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name=name,house=house)
        self.mood = 100        

    def __str__(self):
        return super().__str__()

    def act(self):
        self.house.dirt += 5
        if self.mood < 10:
            return cprint('Жена умерла от депресии!', color='red')
        if self.fullness <= 0:
            return cprint('Жена умерла от голода!', color='red')
        if self.fullness < 30:
            self.eat()            
        if self.house.dirt > 90:
            self.mood -= 10
        elif self.house.food_in_fridge < 60 or self.house.cat_food < 20:
            self.shopping()
        elif self.house.dirt > 50:
            self.clean_house()
        elif self.mood < 16:
            dice = randint(1, 3)
            if dice == 1:
                self.buy_fur_coat()
            else:
                self.pet_cat()


    def pet_cat(self):
        print('Жена погладила кота')
        self.fullness -= 10
        self.mood += 10


    def eat(self):
        if self.house.food_in_fridge < 19:
            self.fullness -= 10
        else:
            self.fullness += 20
            self.house.food_in_fridge -= 20
            print('Жена поела!')
            print('В холодильнике осталось {} еды'.format(self.house.food_in_fridge))        

    def shopping(self):
        if self.house.money_in_nightstand < 100:
            print('Денег нет!')
        elif self.house.money_in_nightstand > 199:
            self.house.money_in_nightstand -= 200
            self.house.food_in_fridge += 200
            print('Жена сходила в магазин! ')
            self.fullness -= 10
        elif self.house.money_in_nightstand > 99:
            self.house.money_in_nightstand -= 100
            self.house.food_in_fridge += 100
            print('Жена сходила в магазин! ')
            self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money_in_nightstand >= 350:
            self.mood += 60
            print('Жена купила шубу')
            self.house.money_in_nightstand -= 350
            self.fullness -= 10            
        else:
            self.mood = self.mood
            print('Жена не купила шубу')

    def clean_house(self):
        print('Жена убралась в доме!')
        if self.house.dirt < 90:
            self.house.dirt -= self.house.dirt
            self.fullness -= 10          
        else:
            self.house.dirt -= 90
            self.fullness -= 10
class Cat(Husband):

    def __init__(self, name,house):
        self.house = house
        self.name = name
        self.fullness = 30
    
    def __str__(self):
        return '{} сытость {}'.format(self.name, self.fullness)


    def act(self):
        if self.fullness == 0:
            return cprint('Котик умер!', color='red')
        if self.fullness < 30:
            self.eat()
        dict = randint(1,3)
        if dict == 1:
            self.soil()

    def eat(self):
        if self.house.cat_food < 10:
            self.fullness -= 10
            print('Мурзик не поел!')
        else:
            self.fullness += 10
            self.house.cat_food -= 5
            print('Мурзик поел!')

    def soil(self):
        print('{} дерет обои!'.format(self.name))
        self.fullness -= 10
        self.house.dirt += 5


    def sleep(self):
        print('{} спит'.format(self.name))
        self.fullness -= 10
class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name,house=house)
        self.mood = 100        

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness == 0:
            print('Ребенок умер!(')
        if self.fullness < 30:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food_in_fridge > 10:
            self.fullness += 10
            self.house.food_in_fridge -= 10
            print('Детенышь поел!')
        else:
            print('Ребенку нечего есть!')

    def sleep(self):
        self.fullness -= 10
        print('Ребенок спит! Всем тихо!')


home = House()
serge = Husband(name='Сережа',house=home)
masha = Wife(name='Маша', house=home)
murzik = Cat(name='Мурзик', house=home)
kolya = Child(name='Коля', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murzik.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murzik, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')



######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов





######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)




# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')

# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

