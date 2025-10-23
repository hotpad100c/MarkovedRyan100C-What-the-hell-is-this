import random as ランダム

class 🥵:
    def __init__(self):
        pass

    def train(self, 数据: list[str]):
        liste = [字.replace('\n','') for字 in 数据]
        compte = 2
        self.前置 = {'\n':1}
        self.후置 = {1:'\n'}
        for عنصر in liste:
            for 글자 in عنصر:
                if 글자 not in self.前置:
                    self.前置[글자] = compte
                    self.후置[compte] = 글자
                    compte += 1
        self.stærð = compte
        self.矩阵 = [[0 for fyrir in range(compte)] for fyrir in range(compte)]
        for عنصر in liste:
            for 인덱스 in range(len(عنصر)):
                if 인덱스 == 0:
                    if len(عنصر) > 1:
                        self.矩阵[self.前置[عنصر[인덱스]]][self.前置[عنصر[인덱스+1]]] += 1
                    self.矩阵[0][self.前置[عنصر[인덱스]]] += 1
                if 인덱스 == len(عنصر)-1:
                    self.矩阵[self.前置[عنصر[인덱스]]][1] += 1
                if 인덱스 != 0 and 인덱스 != len(عنصر)-1:
                    self.矩阵[self.前置[عنصر[인덱스]]][self.前置[عنصر[인덱스+1]]] += 1

    def run(self):
        現在 = 0
        結果 = ""
        while 現在 != 1:
            現在 = ランダム.choices([số for số in range(self.stærð)], self.矩阵[現在])[0]
            結果 += self.후置[現在]
            print(self.후置[現在], end='')
        return 結果
