"""費波那契數列（Fibonacci Sequence）通常是透過迭代（迴圈）或遞迴方式，從 0 和 1 開始，後續數字為前兩數之和
（0, 1, 1, 2, 3, 5, 8...），最簡單的方法是使用 while 或 for 迴圈不斷計算並儲存數值，但遞迴方法雖然簡潔但效率
較差，迭代法（使用列表或變數）在效率上更佳。"""


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Top-Down DP
def fib_td(n: int) -> int:
    fibs: list[int] = [0, 1]
    if n < 2:
        return fibs[n]

    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]


# Buttom-Up DP
def fib_bu(n: int) -> int:
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]


# Rolling DP
def fib_rd(n: int) -> int:
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


print(fib(10))
print(fib_td(10))
print(fib_bu(10))
print(fib_rd(10))
