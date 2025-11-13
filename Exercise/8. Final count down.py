# 最後倒數

# 在 Python 可以透過 print 印出結果，如果在印出的文字前方加上「\r」的命令，每次印出時會將游標移動到最前方，搭配 end 不換行的設定，就能做出類似「畫面更新」的效果，下面的程式執行後，畫面上會顯示倒數秒數。
# 參考：time.sleep、print

import time


def get_integer():
    try:
        x = int(input("請輸入倒數秒數:"))
        return x if x > 0 else get_integer()
    except:
        get_integer()


def final_count_down(x):
    for i in range(x + 1):
        print(f"\r倒數:{x-i}", end="")
        time.sleep(1)


# 下載進度條
def progress_bar(x):
    for i in range(x + 1):
        print(f'\r[{"█"*i}{" "*(x-i)}] {i*100/x}%', end="")
        time.sleep(0.5)


def snow_count():
    n = 100
    icon = "⋮⋰⋯⋱"  # 特殊符號 - 點點: https://www.oxxostudio.tw/project/special-characters/#a16
    for i in range(n + 1):
        print(f"\r{icon[i%4]} {i*100/n}%", end="")
        time.sleep(0.1)


if __name__ == "__main__":
    # final_count_down(get_integer())
    # progress_bar(get_integer())
    snow_count()
