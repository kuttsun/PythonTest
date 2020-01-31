import numpy as np
from enum import IntEnum, auto
from collections import deque

# lots = [0.0104, 0.0105,0.0099,0.0095]

# for lot in lots:
#     print(f'{lot} => {round(lot, 3)}')
#     print(f'{-lot} => {round(-lot, 3)}')
#     print(f'{lot:.3f}')
#     print(f'{-lot:.3f}')

# x = [0,1,2,3,4,5,6,7,8,9,10,11]
# split = 3
# area = len(x) // split
# print(split,area)
# for i in range(area):
#     print(i)
#     x2 = x[i * area:(i+1)*area]
#     if len(x2) > 0:
#         print(x2[0], x2[-1])
#         print(np.mean(x2))

# person = { 'name': 'Taro', 'age': 20 }
# print(person)

# print('country' in person)
# person['country'] = 'Japan'
# print('country' in person)

hoge = [1, 2, 1, 9, 10, 3, 2, 6, 7]
print(hoge[:-3:])
print(hoge[3::])
print(np.argmax(hoge))

# x = np.array([
#     [1, 2, 1, 9, 10, 3, 2, 6, 7],
#     [2, 1, 8, 3, 7, 5, 10, 7, 2],
#     [3, 6, 7, 1, 9, 3,  5, 7, 0]
#     ])
# ret = np.corrcoef(x)[0][1::] # 相関関数行列を求める。
# print(ret)

# class Exchange(IntEnum):
#     BITFLYER = 0
#     BINANCE = auto()
#     BITMEX = auto()
#     OKEX = auto()

# print(int(Exchange.BITFLYER))  # 1
# print(int(Exchange.BINANCE))  # 2
# print(int(Exchange.BITMEX))  # 3
# print(int(Exchange.OKEX))  # 3

# https://qiita.com/TTsujiGIT/items/a3fb7112baa94527dc52
# x = deque([0,1,2])
# y = deque([2,3,4])
# z = deque([4,5,6])

# myarray = np.array([x,y,z])
# print(myarray)

# ret = np.corrcoef(myarray) # 相関関数行列を求める。
# print(ret)

# myDict = {0: {0: 0, 1: 548, 2: 776, 3: 696, 4: 582},
#           1: {0: 548, 1: 0, 2: 684, 3: 308, 4: 194},
#           2: {0: 776, 1: 684, 2: 0, 3: 992, 4: 878},
#           3: {0: 696, 1: 308, 2: 992, 3: 0, 4: 114},
#           4: {0: 582, 1: 194, 2: 878, 3: 114, 4: 0}}

# for i,v in enumerate(myDict.items()):
#     print(i,v)

# orderedNames = myDict.keys()
# dataMatrix = np.array([myDict[i] for i in orderedNames])
# print(dataMatrix)


