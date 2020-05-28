parts = {}
parts['motherboard'] = ('AMD B450', 8236)
parts['cpu'] = ('AMD Ryzen 7 3700X', 38995)
parts['main_mamory'] = ('DDR4 PC4-21300 16GB', 6990)
parts['gpu'] = ('RTX 2070', 48810)
parts['power'] = ('650W', 6710)
parts['case'] = ('ATX', 3850)
parts['ssd'] = ('240GB TLC', 4290)
parts['hdd'] = ('3TB 7200rpm', 7098)
parts['sata_cable'] = ('sataケーブル3本セット', 1000)
parts['os'] = ('Windows10 Home', 17527)

sum = 0

for key, val in parts.items():
    sum += val[1]
    print(key + ':' + val[0] + ' ' + '{:,d}'.format(val[1]) + '円')

print('合計価格:' + '{:,d}'.format(sum) + '円')
