# 元組(Tuple)
# 元組的資料型態是不可變的
# (,)一個元組的資料型態是tuple
# 資料有順序但不能修改
T0 = ()
T1 = "python"
T2 = (0, 1e3, "tuple", True)
T3 = (0, (1, 3), (2, 4))
T4 = tuple("123")
print(T0)
print(T1)
print(T2)
print(T3)
print(T4)

# 元組常用函式
print(len(T2))
print(T2.index(True))
print(T2.count("tuple"))


# 串列(List)
# 串列的資料型態是list
# [,]一個串列的資料型態是list
# 資料有順序且可修改
L0 = []
L1 = [True]
L2 = [1, 2.0, "3", (4, 5), [6, 7]]
L3 = list((1, 2, 3))
print(L0)
print(L1)
print(L2)
print(L3)
print(L1 + L2)

# 串列常用函式
print(len(L2))
print(L2.index("3"))
print(L2.count([6, 7]))
L2.append("8")
print(L2)
L2.insert(1, "9")
print(L2)
L2.remove("9")
print(L2)
L2.pop()
print(L2)
L2.pop(1)
print(L2)
print(L2.clear())

# 集合(Set)
# 集合的資料型態是set
# {,}一個集合的資料型態是set
# 資料無順序且不可重複，但可以修改
# 因無順序，故無法使用[]來讀取元素
S0 = {12, 21, 12}
S1 = set("letters")
S2 = set([5, 2, 1, 1])
print(S0)
print(S1)
print(S2)

# 集合常用函式
print(len(S2))
print(S2.add(3))
print(S2)
print(S2.remove(1))
print(S2)
print(S2.pop())
print(S2)
print(S2.clear())

# 集合特性(交集、聯集、差集、互斥)
S3 = {1, 2, 3}
S4 = {3, 4, 5}
S3.intersection(S4)
print(S3 & S4)
S3.union(S4)
print(S3 | S4)
S3.difference(S4)
print(S3 - S4)
S3.symmetric_difference(S4)
print(S3 ^ S4)
S3.issubset(S4)
print(S3 <= S4)

# 字典(Dictionary)
# 字典的資料型態是dict
# {Key:Value,}一個字典的資料型態是dict
# 資料無順序且可重複，但可修改
# 雖然無順序但可以透過索引(Key)來讀取元素，索引必須獨一無二
D0 = {}
D1 = {"cat": "貓", "dog": "狗", "mouse": "老鼠"}
D2 = dict(cat="貓", dog="狗", mouse="老鼠")
D3 = dict([["a", 100], ["b", 200]])
print(D0)
print(D1)
print(D2)
print(D3)

# 字典常用函式
print(len(D1))
print(D1["cat"])
print(D1.get("cat"))
print(D1.keys())
print(D1.values())
print(D1.items())
print(D1.pop("cat"))
print(D1)
print(D1.popitem())
print(D1)
print(D1.clear())
