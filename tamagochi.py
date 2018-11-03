import random

#Родительский класс питомца
class Pet():
    colors = ('white', 'black', 'black-white', 'spotty', 'brown', 'tricolor', 'gray')
    def __init__(self):                                        #Начальные харакетристики при создании питомца
        self.name = input('What is your pet name? - ')
        x = random.randint(0, 6)
        self.color = self.colors[x]
        self.hungry = 100
        self.sleep = 100
        self.mood = 70
        self.healthy = 100

    def feed(self, food):                                      #Функция кормления питомца
        if food in self.prefer_food:
            self.hungry += 20
        elif food in self.poison_food:
            self.hungry += 5
            self.healthy -= 25
        else:
            self.hungry += 10
        if self.hungry > 100:
            self.hungry = 100
            self.healthy -= 5
        self.sleep -= 10
        self.mood -= 10

    def sleeping(self):                                        #Функция сна питомца
        if self.sleep == 100:
            self.mood -= 30
        self.sleep = 100
        self.hungry -= 20
        self.mood -= 15
        if self.healthy < 100:
            self.healthy += 5

    def play(self, game):                                      #Функция игры с питомцем
        if game in self.prefer_games:
            self.mood += 20
        else:
            self.mood += 10
        if self.mood > 100:
            self.mood = 100
            self.sleep -= 25
        self.sleep -= 10
        self.hungry -= 15

    def is_pet_died(self):                                     #Функция для проверки жив ли питомец
        if self.sleep <= 0 or self.hungry <= 0 or self.healthy <= 0 or self.mood <= 0:
            return True
        else:
            return False

    def print_prefer(self):                                    #Функция печати особенностей данного вида питомца
        print('Your {} likes to eat {} and play with {}, but be careful - it can dies because of {}.'.format(
            self.name, ', '.join(self.prefer_food), ', '.join(self.prefer_games), ', '.join(self.poison_food)))

    def print_charst(self):                                    #Функция печати состояния питомца
        print('How does {} feel:\n hungry: {}\n sleep: {}\n mood: {}\n healthy: {}'.format(
            self.name, self.hungry, self.sleep, self.mood, self.healthy))

class Cat(Pet):                                                #Детёнышеский класс кошки
    prefer_food = ['fish', 'meet', 'milk']                     #У каждого подкласса есть любимая и отравляющая еда, любимые игры
    poison_food = ['chocolate', 'cabbage', 'carrot', 'candy']
    prefer_games = ['mouse', 'pointer']

class Dog(Pet):
    prefer_food = ['meet', 'bone']                             #Детёнышеский класс собаки
    poison_food = ['chocolate', 'milk', 'carrot', 'candy']
    prefer_games = ['ball', 'sneakers']

class Rabbit(Pet):                                             #Детёнышеский класс кролика
    prefer_food = ['cabbage', 'carrot']
    poison_food = ['fish', 'meet', 'candy']
    prefer_games = ['hug', 'tale']

p = ''
possible_pets = ['cat', 'dog', 'rabbit']                       #Возможные животные
actoins = ['feed', 'sleep', 'play']                            #Действия с животным
games = ['mouse', 'pointer', 'ball', 'sneakers', 'hug', 'tale']#Игры
foods = ['fish', 'meet', 'milk', 'bone', 'cabbage', 'carrot']  #Еда

while p == '' or p.lower() not in possible_pets:               #Цикл повторяется, пока пользователь не введёт корректное животное
    p = input('Which pet do you want? (cat, dog, rabbit): ')

if p.lower() == 'cat':                                         #Создание животного нужного класса
    pet = Cat()
elif p.lower() == 'dog':
    pet = Dog()
else:
    pet = Rabbit()

print('Cool! You have a {} {}! It have a color {}!:)'.format(p.lower(), pet.name, pet.color))
pet.print_prefer()

while True:
    try:
        if not pet.is_pet_died():                              #Игра продолжается, пока животное не умрёт
            #Спрашиваем, хочет ли пользователь играть дальше
            answ = int(input('Do you wanna play next?\n 1 - yes\n 2 - no\n'))
            if answ == 1:
                pet.print_charst()

                #Выбор действия
                act = int(input('Please, choose the action (you need to print just a number):\n 1 - {}\n 2 - {}\n 3 - {}\n'.format(
                    actoins[0], actoins[1], actoins[2])))

                if 1 <= act <= 3:
                    act = actoins[act - 1]
                    #Проверяем, какое именно действие выбрал пользователь
                    if act == actoins[0]:
                        food = int(input(
                            'Please, chooce the food (you need to print just a number):\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n'.format(
                                foods[0], foods[1], foods[2], foods[3], foods[4], foods[5])))

                        if 1 <= food <= 6:
                            food = foods[food - 1]
                            pet.feed(food)
                        else:
                            print('Sorry, dude, but you have to choose between 1 and 6, maybe we will eat later.;(')

                    elif act == actoins[1]:
                        pet.sleeping()

                    else:
                        game = int(input(
                            'Please, choose the game (you need to print just a number):\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n'.format(
                                games[0], games[1], games[2], games[3], games[4], games[5])))

                        if 1 <= game <= 6:
                            game = games[game - 1]
                            pet.play(game)

                        else:
                            print('Sorry, dude, but you have to choose between 1 and 6, maybe we will play later.;(')
                else:
                    print('Sorry, dude, but you have to choose between 1 and 3!')
            elif answ == 2:
                break
        else:
            print('Nooo, dude, you killed your sweetie {}!;(\n Please, never do it with real pets! '.format(pet.name))
            break

    except ValueError as err:                                  #Кидаем ошибку, если пользователь вместо числа вводит что-то другое
        print('Было введено неправильное значение!')