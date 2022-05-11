from dataclasses import dataclass
from enum import Enum
from typing import List

class ComponentType(Enum):
    POWER = '電源ユニット'
    CPU = 'CPU'
    MEMORY = 'メモリ'
    MOTHERBOARD = 'マザーボード'
    STORAGE = 'ストレージ'
    CASE = 'ケース'
    OS = 'OS'
    DGPU = 'GPU'
    OTHER = 'ほか'

# ほんとはパーツごとに継承していくのがPCっぽいけど面倒なのでこれでごまかす。
@dataclass
class Component:
    type: ComponentType
    price: int
    standard: str
    description: str = '説明なし'
    shopURL: str = 'なし'

class PC:
    def __init__(self, name: str = 'mypc', discription: str = None) -> None:
        self.parts: List[Component] = []
        self.pcName = name
        self.disctiption = discription

    def assemble(self, component: Component):
        self.parts.append(component)
        
    def calc_price(self) -> int:
        sum = 0
        # NOTE: もっといい書き方ありそう
        for component in self.parts:
            sum += component.price
        return sum

    def check_bootable(self) -> None:
        # TODO: パーツ重複時に警告
        # TODO: 主要パーツが無かったら警告
        # TODO: ほかにも足りないと困るパーツあったら警告
        # 後で実装する
        pass

    def print_detail(self) -> None:
        print(f'{self.pcName}')
        print(f'{self.disctiption}')
        for p in self.parts:
            print(f'{p.type.value:<8}\t{p.price:>8,d} 円\t{p.standard:<12}\t{p.description:<24}\t{p.shopURL:<}')

        print(f'合計価格:\t{self.calc_price():>8,d} 円')


# 目的
# UE5を触りたい。
# 最高のレンダリング機能をもとめたら金がいくらあっても足りず、そもそも始められないので、あきらめる。
# なので、通常の使用に耐えうると思われるくらいで組む。

ue5pc = PC('ue5pc', 'UE5が動くくらいのPC')

# cpu
# quad-core（4コア）あればよさそう。
# ここはいろんな意見あるから責任取れない。僕はcorei3で十分だと思う。
corei3 = Component(ComponentType.CPU, 16780, 'LGA1700', 'corei3 12100 4core 8thread', 'https://kakaku.com/item/K0001413997/')
corei3f = Component(ComponentType.CPU, 13479, 'LGA1700', 'corei3 12100f 4core 8thread', 'https://kakaku.com/item/K0001413998/')
corei5 = Component(ComponentType.CPU, 25480, 'LGA1700', 'corei5 12480 6core12thread', 'https://kakaku.com/item/K0001413994/')
corei5f = Component(ComponentType.CPU, 25480, 'LGA1700', 'corei5 12480f 6core12thread', 'https://kakaku.com/item/K0001413995/')
ue5pc.assemble(corei3)

# メモリ
# 16でよさそうだけど、不安なので一応32積む。
mem16gb = Component(ComponentType.MEMORY, 6750, 'DDR4', '16GB', 'https://kakaku.com/item/K0001363420/')
mem32gb = Component(ComponentType.MEMORY, 12480, 'DDR4', '32GB', 'https://kakaku.com/item/K0001339365/')
ue5pc.assemble(mem32gb)

# マザーボード
# 一番お金をかけたくない。
mb = Component(ComponentType.MOTHERBOARD, 11980, 'microATX', 'LGA1700 DDR4 pcie4.0', 'https://kakaku.com/item/K0001416571/')
ue5pc.assemble(mb)

# 電源
# ここもお金かけたくない。いいのを買っても電気代で元取れないし、新しいパソコンが欲しくなっても壊れてくれない。
# グラボのせても750Wで余裕。
power = Component(ComponentType.POWER, 7173, 'ATX電源', '750W', 'https://kakaku.com/item/K0001026568/')
ue5pc.assemble(power)

# ストレージ
# M.2がだいぶん安くなってきた。
ssd500gb = Component(ComponentType.STORAGE, 6080, 'M.2', 'SSD 500GB', 'https://kakaku.com/item/K0001434806/')
ssd1tb = Component(ComponentType.STORAGE, 9380, 'M.2', 'SSD 1TB', 'https://kakaku.com/item/K0001431182/')
ue5pc.assemble(ssd1tb)

# ケース
# 見える部分なのでイカしたのを適当に。
case = Component(ComponentType.CASE, 2973, 'microATX', 'ミドルタワー', 'https://www.amazon.co.jp/dp/B077GFVY21/')
ue5pc.assemble(case)

# OS
# 特に理由がない限りWindows Homeでok。
os = Component(ComponentType.OS, 17136, 'Windows11 Home', '64bit', 'https://www.amazon.co.jp/dp/B09VSXCY87/')
ue5pc.assemble(os)

# グラボ
# こまった。とりあえず適当に。
# 性能よりもあるかないかの方が大事だと思うので、3060で問題ないと思う。
rtx3060 = Component(ComponentType.DGPU, 52980, 'pcie4.0', 'NVIDIA RTX3060 VRAM 12GB', 'https://kakaku.com/item/K0001363822/')
rtx3060ti = Component(ComponentType.DGPU, 69800, 'pcie4.0', 'NVIDIA RTX3060 ti VRAM 8GB', 'https://kakaku.com/item/K0001366194/')
rtx3070 = Component(ComponentType.DGPU, 84800, 'pcie4.0', 'NVIDIA RTX3070 VRAM  8GB', 'https://kakaku.com/item/K0001372327/')
ue5pc.assemble(rtx3060)

ue5pc.print_detail()


# ここから古いもの
parts = {}

# Intel
# parts['cpu'] = ('Core i7 10700', 38500)
# parts['cpu'] = ('Core i7 10700F', 37268)
parts['cpu'] = ('Core i5 10400', 20480)
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
# parts['gpu'] = ('RTX2060 SUPER VRAM 8GB', 42878) # hdmi x1, dp x3
parts['gpu'] = ('RTX2070 SUPER VRAM 8GB', 48950) # hdmi x1, dp x3
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

parts['os'] = ('Windows10 Home', 17527) # 通常版

sum = 0

# for key, val in parts.items():
#     sum += val[1]
#     print(key + ':' + val[0] + ' ' + '{:,d}'.format(val[1]) + '円')

# print('合計価格:' + '{:,d}'.format(sum) + '円')
