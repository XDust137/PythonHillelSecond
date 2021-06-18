import random


class Player:
    list_of_frame = []

    def __init__(self, name: str = "Unnamed"):
        self.name = name

    @property
    def score(self):
        res = []
        for item in self.list_of_frame: res.extend(item)
        for item in res:
            if item == ['X']: res[len(res)] = 10
            elif item == ['/']: res[len(res)] = 0
        print(res)
        return str(name + "'s score: " + str(sum(res)))


# Определение кол-ва игроков
count: int
while True:
    inputcount = input("Enter player number (1-6): ")
    if inputcount.isdigit() and 0 < int(inputcount) < 7: break
    else: print('Input data is not a number or out of range')
count = int(inputcount)

# Даём имена игрокам
players = []
for i in range(count):
    name = input("Enter name of " + str(i+1) + " player: ")
    players.append(Player(name))

left = players.copy()
playing = True


# я решил всё же что лучше будет эту функцию оставить в основном коде, т.к. она изначально служила лишь
# для приёма вводных данных и их проверки, и в итоге просто возвращала подходящее значение, остальная логика
# выполнялась далее, а datainput() это просто адаптированная под боулинг функция input() с проверками
def datainput(isSecond: bool = False):
    if isSecond: print("How much is knocked at the second time?")
    else: print("How much is knocked?")
    while True:
        res = input(">> ")
        if res.isdigit() and 0 <= int(res) <= 10:
            break
        else: print('Error input data. I think, you should input only number 0-10.')
    return int(res)


# Запуск игры
print('Game begins!')
for i in range(9):
    for j in range(count):
        # выбор игрока
        turn = random.choice(left)
        throws = []
        print(turn.name + "'s turn!")
        # запрос на кол-во сбитых кеглей
        knocked = datainput()
        # обработка запроса и проверка на страйк
        if knocked == 10:
            print('Strike!')
            throws = ['X']
            knocked2 = 0
        # если не страйк то
        else:
            print(str(knocked) + ' pins knocked down. Try again!')
            knocked2 = datainput(True)
            # если сбиты все или каким-то чудом более то
            if knocked + knocked2 >= 10:
                print('Spare')
                throws = [knocked, '/']
            # если не все то
            else: throws = [knocked, knocked2]
        # добавляем новый фрейм в общий список и объявляем для удобства переменную предыдущего
        turn.list_of_frame.append(throws)
        previous = turn.list_of_frame[len(turn.list_of_frame) - 1]
        # в зависимости от предыдущего фрейма...
        if previous == ['X']: turn.list_of_frame[len(turn.list_of_frame) - 1] = [knocked + knocked2 + 10]
        elif previous == [int, '/']: turn.list_of_frame[len(turn.list_of_frame) - 1] = [knocked + 10]


for i in range(count): print(players[i].score)
