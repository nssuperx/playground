# -*- coding:utf-8 -*-

BOARDSIZE = 8
DIRECTION_Y = [-1, -1, -1, 0, 0, 1, 1, 1]
DIRECTION_X = [-1, 0, 1, -1, 1, -1, 0, 1]

class Stone:
    # 無効な石を配置
    def __init__(self):
        self.isused = False

    # 石を置く
    def put(self, black):
        self.isblack = black

    # 石の有効化
    def enable(self):
        self.isused = True


class Board:
    # 初期設定
    def __init__(self):
        a[3][3].enable()
        a[3][3].put(False)
        a[3][4].enable()
        a[3][4].put(True)
        a[4][3].enable()
        a[4][3].put(True)
        a[4][4].enable()
        a[4][4].put(False)

    # 石を探す
    def seek_stone(self, y, x, black, i, board_list):
        count = 0
        while True:
            count += 1
            ydir = count * DIRECTION_Y[i]
            xdir = count * DIRECTION_X[i]
            if y+ydir < 0 or BOARDSIZE-1 < y+ydir or x+xdir < 0 or BOARDSIZE-1 < x+xdir:
                count = 0
                break
            if board_list[y+ydir][x+xdir].isused == False:
                count = 0
                break
            if board_list[y+ydir][x+xdir].isblack == black:
                break
        return count

    # 置けるところを全探索
    def detect_stone(self, black):
        b = a[:]
        putlist = []
        for y in range(BOARDSIZE):
            for x in range(BOARDSIZE):
                if b[y][x].isused == True:
                    continue
                for i in range(BOARDSIZE):
                    count = self.seek_stone(y, x, black, i, b)
                    if count > 1:
                        putlist.append(y)
                        putlist.append(x)
                        break
        return putlist

    # 石を裏返す
    def inverse_stone(self, y, x, black):
        a[y][x].enable()
        a[y][x].put(black)
        for i in range(BOARDSIZE):
            count = self.seek_stone(y, x, black, i, a)
            # print(count)
            for j in range(count):
                a[y+j*DIRECTION_Y[i]][x+j*DIRECTION_X[i]].put(black)

    # 石を数える
    def count_stone(self, black):
        count = 0
        for i in range(BOARDSIZE):
            for j in range(BOARDSIZE):
                if a[i][j].isused == True:
                    if a[i][j].isblack == black:
                        count += 1
        return count

    # ボードを表示
    def print_board(self):
        print("{0:>3}".format(" "), end="")
        for i in range(BOARDSIZE):
            print("{0:>3}".format(i), end="")
        print()

        for i in range(BOARDSIZE):
            print("{0:>3}".format(i), end="")
            for j in range(BOARDSIZE):
                if a[i][j].isused == False:
                    c = 'l'
                elif a[i][j].isblack == True:
                    c = 'X'
                else:
                    c = 'O'
                print("{0:>3}".format(c), end="")
            print()


def put_stone(stone, player):

    # 置けるリストを作る
    putlist = board.detect_stone(stone)
    if len(putlist) == 0:
        print("pass")
        return 1
    canputy = putlist[0::2]
    canputx = putlist[1::2]
    print("y:" + str(canputy))
    print("x:" + str(canputx))

    # ユーザーが操作
    while True:
        detect = False
        print(player+" のターンです。")
        y = input("y:")
        x = input("x:")

        # 整数に型変換しつつ、それ以外をはじく
        try:
            y = int(y)
            x = int(x)
        except ValueError:
            print("整数値を入力してください。")
            continue

        # 強制終了できる
        if x == 9 or y == 9:
            return - 1

        # 入力値を置けるリストと照らし合わせ
        index_num = [n for n, v in enumerate(canputy) if v == y]
        for i in index_num:
            if y == canputy[i] and x == canputx[i]:
                detect = True
                break
        if detect == True:
            break
        print("そこには、置けません。")

    # 入力が正しければ石を置く
    board.inverse_stone(y, x, stone)
    board.print_board()
    return 0


a = [[Stone() for i in range(BOARDSIZE)] for i in range(BOARDSIZE)]
board = Board()
board.print_board()


while True:
    play_O = 0
    play_X = 0
    play_O = put_stone(False, "O")
    if play_O == -1:
        break
    play_X = put_stone(True, "X")
    if play_X == -1:
        break
    if play_O + play_X == 2:
        break

count_O = board.count_stone(False)
count_X = board.count_stone(True)

print("O の数は " + str(count_O))
print("X の数は " + str(count_X))

if count_O > count_X:
    print("O の勝ちです。")
elif count_O == count_X:
    print("引き分けです。")
else:
    print("X の勝ちです。")


input("終了するにはエンターキーを押してください。")
