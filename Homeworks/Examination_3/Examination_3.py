# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card_security(card):
    new_card = "*" * (len(card) - 4) + card[-4:]
    print(f"Card number: {new_card}")

card = input("Enter card number: ")
card_security(card)


# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

def polindrom(word):
        print("YES" if word == word[::-1] else "NO")

word = input("Enter word: ")
polindrom(word)


# 3. Решите задачу
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов
# и на его основе будет создавать список объектов класса Tomato.
# Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

class Tomato:
    states = ["росток", "цветок", "зеленый плод", "зрелый плод"]
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[self._index]
    def grow(self):
        if self._state != Tomato.states[-1]:
            self._index += 1
            self._state = Tomato.states[self._index]
        else:
            print("Больше расти нельзя, уже созрел, дальше только портится")
    def is_ripe(self):
        if self._state == Tomato.states[-1]:
            return True
        else:
            return False

class TomatoBush(Tomato):
    default_index = 0
    def __init__(self, number_tomatoes):
        super().__init__(TomatoBush.default_index)
        self.number_tomatos = number_tomatoes
        self.tomatoes = ["tomato" + f"{i}" for i in range(1, self.number_tomatos + 1)]
        for i in range(len(self.tomatoes)):
            self.tomatoes[i] = Tomato(TomatoBush.default_index)
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
        self.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.is_ripe():
                return True
            else:
                return False

    def give_away_all(self):
        self.tomatoes.clear()
        self._state = f"с куста собрано {self.number_tomatos} спелых помидоров"
        self.number_tomatos = 0

class Gardener:
    def __init__(self, name):
        self.name = name
        self.basket = []

    def work(self, *args):
        self._plant = args
        for j, i in enumerate(self._plant):
            if i.all_are_ripe() == False:
                i.grow_all()
                print(f"Куст {j + 1} в состоянии {i._state}")
            else:
                print(f"На кусте {j + 1} помидоры созрели, можно собирать урожай")

    def harvest(self, *args):
        self._plant = args
        for j, i in enumerate(self._plant):
            if i.all_are_ripe() == True:
                self.basket.extend(i.tomatoes)
                print(f"В корзине {len(self.basket)} помидоров")
            else:
                print(f"Куст {j + 1} еще не созрел")
    @staticmethod
    def knowledge_base():
        print("""
        Справка по садоводству
1. С помощью класса "TomatoBush" создайте необходимое количество кустов помидоров.
2. С помощью класса "Gardener" создаете садовника.
3. В методе "work" садовника укажите за какими кустами помидоров ухаживать.
4. Как только плоды станут зрелыми, укажите в методе садовника "harvest" плоды с каких кустов собрать.
""")

# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

Gardener.knowledge_base()
bush1 = TomatoBush(5)
bush2 = TomatoBush(7)
bush3 = TomatoBush(12)
roman = Gardener("Roman")
roman.work(bush1, bush2, bush3)
roman.harvest(bush1, bush2, bush3)
roman.work(bush1, bush2, bush3)
roman.work(bush1, bush2, bush3)
roman.harvest(bush1, bush2, bush3)

