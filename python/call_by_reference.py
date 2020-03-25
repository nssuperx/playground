hoge1num = 0
hoge2num = 0
while True:
    hoge1num += 1
    hoge2num += 1
    if id(hoge1num) != id(hoge2num):
        print(hoge1num)
        break