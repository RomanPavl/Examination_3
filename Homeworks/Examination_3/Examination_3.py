# 1. �������� �������, ������� ����� ��������� ����� ��������� ����� �
# ���������� ������ ��������� 4 �����. ��������� ����� ������ ����������
# �����������

def card_security(card):
    new_card = "*" * (len(card) - 4) + card[-4:]
    print(f"Card number: {new_card}")

card = input("Enter card number: ")
card_security(card)


# 2. �������� �������, ������� ���������: �������� �� ����� �����������

def polindrom(word):
        print("YES" if word == word[::-1] else "NO")

word = input("Enter word: ")
polindrom(word)


# 3. ������ ������
# ����� Tomato:
# 1. �������� ����� Tomato
# 2. �������� ����������� �������� states, ������� ����� ��������� ��� ������ ���������� ��������
# 3. �������� ����� __init__(), ������ �������� ����� ���������� ��� ������������ protected ��������:
# 1) _index - ���������� ���������� � 2) _state - ��������� ������ �������� �� ������� states
# 4. �������� ����� grow(), ������� ����� ���������� ����� �� ��������� ������ ����������
# 5. �������� ����� is_ripe(), ������� ����� ���������, ��� ����� ������ (������ ��������� ������ ����������)
# ����� TomatoBush
# 1. �������� ����� TomatoBush
# 2. ���������� ����� __init__(), ������� ����� ��������� � �������� ��������� ���������� �������
# � �� ��� ������ ����� ��������� ������ �������� ������ Tomato.
# ������ ������ ����� ��������� ������ ������������� �������� tomatoes.
# 3. �������� ����� grow_all(), ������� ����� ���������� ��� ������� �� ������ ������� �� ��������� ���� ����������
# 4. �������� ����� all_are_ripe(), ������� ����� ���������� True, ���� ��� ������ �� ������ ����� �������
# 5. �������� ����� give_away_all(), ������� ����� ������� ������ ������� ����� ����� ������
# ����� Gardener
# 1. �������� ����� Gardener
# 2. �������� ����� __init__(), ������ �������� ����� ���������� ��� ������������ ��������:
# 1) name - ���������� ����������, �������� ��������� � 2) _plant - ��������� ������ ������ Tomato, �������� protected
# 3. �������� ����� work(), ������� ���������� ��������� ��������, ��� ��������� �������� ����������� ����� ������
# 4. �������� ����� harvest(), ������� ���������, ��� �� ����� �������. ���� ��� -
# �������� �������� ������. ���� ��� - ����� �������� ��������������.
# 5. �������� ����������� ����� knowledge_base(), ������� ������� � ������� ������� �� �����������.

class Tomato:
    states = ["������", "������", "������� ����", "������ ����"]
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[self._index]
    def grow(self):
        if self._state != Tomato.states[-1]:
            self._index += 1
            self._state = Tomato.states[self._index]
        else:
            print("������ ����� ������, ��� ������, ������ ������ ��������")
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
        self._state = f"� ����� ������� {self.number_tomatos} ������ ���������"
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
                print(f"���� {j + 1} � ��������� {i._state}")
            else:
                print(f"�� ����� {j + 1} �������� �������, ����� �������� ������")

    def harvest(self, *args):
        self._plant = args
        for j, i in enumerate(self._plant):
            if i.all_are_ripe() == True:
                self.basket.extend(i.tomatoes)
                print(f"� ������� {len(self.basket)} ���������")
            else:
                print(f"���� {j + 1} ��� �� ������")
    @staticmethod
    def knowledge_base():
        print("""
        ������� �� �����������
1. � ������� ������ "TomatoBush" �������� ����������� ���������� ������ ���������.
2. � ������� ������ "Gardener" �������� ���������.
3. � ������ "work" ��������� ������� �� ������ ������� ��������� ���������.
4. ��� ������ ����� ������ �������, ������� � ������ ��������� "harvest" ����� � ����� ������ �������.
""")

# �����:
# 1. �������� ������� �� �����������
# 2. �������� ������� ������� TomatoBush � Gardener
# 3. ��������� ������ ������ Gardener, ������������ �� ������ � ����������
# 4. ���������� ������� ������
# 5. ���� ������ ��� �� �������, ����������� ��������� �� ����
# 6. �������� ������

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

