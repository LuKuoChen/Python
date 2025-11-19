# 數字金字塔

# 數字金字塔會按照「一定的規則」，產生一連串的數字，堆疊出金字塔的形狀，規則可能是等比級數、等差級數...等之類的數列，通常將數字大的放在下方，數字小的放在上方。


def get_integer():
    try:
        x = int(input("請輸入幾層:"))
        return x if x > 0 else get_integer()
    except:
        get_integer()


def pyramid1(n):
    for i in range(1, n + 1):
        if i == 1:
            print(i)
        else:
            for j in range(1, i + 1):
                print(j, end=" ")
            for j in range(i - 1, 0, -1):
                print(j, end=" ")
            print()


def pyramid2(n):
    for i in range(1, n + 1):
        print(" " * ((n + 1 - i) * 2 - 2), end="")
        if i == 1:
            print(i)
        else:
            for j in range(1, i + 1):
                print(j, end=" ")
            for j in range(i - 1, 0, -1):
                print(j, end=" ")
            print()


def pyramid3(n):
    for i in range(1, n + 1):
        print(" " * ((n + 1 - i) * 2 + 6 - ((i - 1) * 2)), end="")
        if i == 1:
            print(i)
        else:
            for j in range(1, i + 1):
                print(j, end=" ")
            for j in range(i - 1, 0, -1):
                print(j, end=" ")
            print()


def pyramid4(n):
    for i in range(1, n + 1):
        if i == 1:
            print(i)
        else:
            for j in range(1, i + 1):
                k = j**2
                print(k, end=" ")
            for j in range(i - 1, 0, -1):
                k = j**2
                print(k, end=" ")
            print()


if __name__ == "__main__":
    x = get_integer()
    pyramid1(x)
    pyramid2(x)
    pyramid3(x)
    pyramid4(x)
