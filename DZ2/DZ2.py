import random


class Player:
    list_of_frame = []

    def __init__(self, name: str = "Unnamed"):
        self.name = name

    @property
    def score(self):
        res = []
        for item in self.list_of_frame: res.extend(item)
        for i in range(len(res)):
            if res[i] == 'X':
                res[i] = 10
            elif res[i] == '/':
                res[i] = 0
        print(res)
        return str(self.name + "'s score: " + str(sum(res)))


# Определение кол-ва игроков
count: int
while True:
    inputcount = input("Enter player number (1-6): ")
    if inputcount.isdigit() and 0 < int(inputcount) < 7:
        break
    else:
        print('Input data is not a number or out of range')
count = int(inputcount)

# Даём имена игрокам
players = [Player(input(f"Enter name of {i + 1} player: ")) for i in range(count)]
left = players.copy()
playing = True


def datainput(isSecond: bool = False):
    if isSecond: print("How much is knocked at the second time?")
    else: print("How much is knocked?")
    while True:
        res = input(">> ")
        if res.isdigit() and 0 <= int(res) <= 10: break
        else: print('Error input data. I think, you should input only number 0-10.')
    return int(res)


def pre_check(chplayer, chthrow, chthrow2=None):
    if chthrow2 is None:
        if len(chplayer.list_of_frame) > 1:
            if chplayer.list_of_frame[-2][-1] == "X":
                chplayer.list_of_frame[-2][-1] = 20 + chthrow
        elif chplayer.list_of_frame[-1][-1] == "/":
            chplayer.list_of_frame[-1][-1] = 10 + chthrow
    else:
        if chplayer.list_of_frame[-1][-1] == "X": chplayer.list_of_frame[-1][-1] = 10 + chthrow + chthrow2


def throw_check(FUNplayer, FUNthrow: int, FUNthrow2=None):
    """Return int type or string type"""
    if FUNthrow2 is None:
        if FUNthrow >= 10:
            if FUNplayer.list_of_frame: pre_check(FUNplayer, FUNthrow)
            FUNplayer.list_of_frame += [["X"]]
            return "X"
        if FUNplayer.list_of_frame: pre_check(FUNplayer, FUNthrow)
        return FUNthrow
    else:
        if FUNthrow == 'X': FUNthrow = 10
        if FUNthrow2 >= (10 - FUNthrow):
            if FUNplayer.list_of_frame: pre_check(FUNplayer, FUNthrow, FUNthrow2)
            FUNplayer.list_of_frame += [["/"]]
            return "/"
        if FUNplayer.list_of_frame: pre_check(FUNplayer, FUNthrow, FUNthrow2)
        FUNplayer.list_of_frame += [[FUNthrow, FUNthrow2]]
        return FUNplayer.list_of_frame[-1]


# Запуск игры
random.shuffle(players)
print('Game begins!')
for i in range(9):
    for player in players:
        throw1 = throw_check(player, int(input("Write your hited keglse: ")))
        if throw1 == "X": print("STRIKE")
        if throw1 == "/": print("SPARE")
        throw2 = throw_check(player, throw1, int(input("Write your next hited keglse: ")))
        if throw2 == "X": print("STRIKE")
        else: print("SPARE")
        # Скорее всего эта строчка и вовсе не нужна но пускай будет наверное? Не уверен
        # res = player.list_of_frame[-1]
else: pass

for player in players:
    print(player.list_of_frame)
    print(player.score)
