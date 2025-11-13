# 星號金字塔

# 星號字塔的基本型會按照「1、3、5、7...」奇數排列的方式，將星號「＊」堆疊出金字塔的形狀 ( 也可以是 1、5、9、13...之類的奇數組合 )。


def get_integer():
    try:
        x = int(input("請輸入幾層:"))
        return x if x > 0 else get_integer()
    except:
        get_integer()


def pyramid1(n):
    for i in range(1, n + 1):
        print(((i * 2 - 1) * "*"))


def pyramid2(n):
    for i in range(1, n + 1):
        print((((n * 2 - 1) - (i * 2 - 1)) // 2 * " ") + ((i * 2 - 1) * "*"))


def pyramid3(n):
    for i in range(1, n + 1):
        print((((n * 2 - 1) - (i * 2 - 1)) * " ") + ((i * 2 - 1) * "*"))


if __name__ == "__main__":
    x = get_integer()
    pyramid1(x)  # 靠左
    pyramid2(x)  # 置中
    pyramid3(x)  # 靠右
