parts = {}

# Intel
parts['cpu'] = ('Core i7 10700', 38500)
# parts['cpu'] = ('Core i7 10700F', 37268)
# parts['cpu'] = ('Core i5 10400', 20480)
# parts['cpu'] = ('Core i5 10400F', 18675)
# i7 8core 16thread LGA1200
# i5 6core 12thread LGA1200
# 内蔵gpu付きです。
# なぜそうしたかは、2000円くらいしか変わらんから、普通に性能がいいから。です。
# でも、基本はbiosでとめます。いざというときに使います。
# 型番に「F」がついてるのは内蔵gpuなしです。
# 正直、ターボブーストでクロックはめちゃ上がるからi5でもいい気がする。
# でもいろんなスコアは低い。たぶん普通に使う分ではそんな影響ないかと。


# AMD
# parts['cpu'] = ('AMD Ryzen 7 3700X', 39280)
# parts['cpu'] = ('AMD Ryzen 5 5600X', 39380)
# Ryzen 7 3700X 8core 16thread SocketAM4
# Ryzen 5 5600X 6core 12thread SocketAM4
# 下のが最新。6core12thread。ryzen7の最新のは高すぎる。
# コスパだけで考えると、正直intelのでもよかった気がする。そんなに変わらん。


# Intel
parts['motherboard'] = ('ATX Intel H470 LGA1200', 12882)
# どちらのcpuでもこれ
# M.2付き

# AMD
# parts['motherboard'] = ('ATX AMD B450 SocketAM4', 7980)
# parts['motherboard'] = ('ATX AMD B550 SocketAM4', 11861)
# SocketAM4 B450 最安
# Ryzen 5 5600Xにするならおそらくbiosアップデートがいる。
# Ryzen 5 5600X : SocketAM4 B550

parts['main_memory'] = ('DDR4 PC4-21300 16GB x2', 10980)

# parts['gpu'] = ('RTX2060 SUPER VRAM 8GB', 39800) # dvi x1, hdmi x1, dp x1
parts['gpu'] = ('RTX2060 SUPER VRAM 8GB', 42878) # hdmi x1, dp x3
# もう3000円くらいかければDisplayPort端子数が増える。

parts['power'] = ('750W', 7238)

parts['case'] = ('ATX', 3938)

parts['ssd'] = ('none', 0)
# M.2がついてるマザーを選んだ。というか普通に最安のでもついてた。

# parts['hdd'] = ('3TB 7200rpm', 7177) # 東芝製
# parts['hdd'] = ('4TB 5400rpm', 7380) # 東芝製
parts['hdd'] = ('5TB 7200rpm', 8800) # 東芝製
# 4TBにしても値段1000円くらいしか変わらん。
# 一応高回転数なのにした。
# 4TB 7200rpmで安いのが見つからなかった

parts['sata_cable'] = ('sataケーブル3本セット', 1000)

# parts['os'] = ('Windows10 Home', 17527)
parts['os'] = ('Windows10 Home', 12345) # 古い、usbインストーラーついてくる
# 古いのを買ったら安くなる。欲しいのはライセンスキーなので関係なし。

sum = 0

for key, val in parts.items():
    sum += val[1]
    print(key + ':' + val[0] + ' ' + '{:,d}'.format(val[1]) + '円')

print('合計価格:' + '{:,d}'.format(sum) + '円')
