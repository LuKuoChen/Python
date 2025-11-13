# 大樂透電腦選號
# 設計出大樂透電腦選號的程式 ( 從 1～49 個數字中，選出六個不重複的數字 )。

# 方法一、串列判斷
# 先建立一個空串列，接著不斷將 1～49 的隨機數放入串列中，放入時進行判斷，如果串列中已經有該數字就不放入，直到串列的長度等於 6 為止。
# 參考：while 迴圈、random.randint、if 判斷式

import random


def lottery1():
    lottery = []
    while len(lottery) < 6:
        num = random.randint(1, 49)
        if num not in lottery:
            lottery.append(num)
    return lottery


# 方法二、搭配集合 set
# 因為 Python 的集合有著「項目不會重複」的特性，所以只要將 1～49 的隨機數字不斷放到一個集合裡，直到集合的項目到達六個，就完成選號不重複的動作。
# 參考：集合


def lottery2():
    lottery = set()
    while len(lottery) < 6:
        lottery.add(random.randint(1, 49))
    return lottery


# 方法三、使用 random.sample
# 因為 Python random 模組裡的 random.sample 具有取出不重複項目的特性，所以只要使用 random.sample 就能輕鬆的取得串列中的六個不重複數字。
# 參考：random.sample(seq, k)、range(start, stop, step)

def lottery3():
    return random.sample(range(1, 50), 6)


if __name__ == "__main__":
    print(lottery1())
    print(lottery2())
    print(lottery3())
