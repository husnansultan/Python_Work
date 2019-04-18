##99 bottles of beer chalang

import time
## 99 Bottles of beer on the wall
## 99 Bottles of beer
## Take one down, pass it around
## 98 bottles of beer on the wall
bottles = 99
while bottles > 0:
    print(bottles,"bottles of beer on the wall")
    print(bottles,"bottles of beer")
    print("Take one down, pass it around")
    bottles = bottles - 1
    print(bottles,"bottles of beer on the wall")
    time.sleep(1)