#  Mininum coins taken to give an specific amount tp grocery by greedy algorithm ...

import math
def mincount(arr,amount):
    res = 0
    for x in range(len(arr)):
        if arr[x] <= amount:
            c = math.floor(amount/arr[x])
            res = res+c
            amount = amount - c*arr[x]
        if amount == 0:
            break
    return res


print(mincount([10,5,2,1],52))
