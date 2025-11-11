# 資料型態(Data Type)
# 1. 基本
#     整數(int; integer): Python3無上限; 運算子
#     浮點數(float): 科學記號(e or E)表示10的次方
#     字串(str; string): Slice的應用; 常用函式
#     布林(bool; boolen): 0(False)以外都是True
#     型態轉換: int() float() str() bool()
# 2. 複合
#     元祖(tuple)
#     串列(list)
#     集合(set)
#     字典(dict)

# 算術運算子
# +, -, *, /, %, //, **

# 比較運算子
# ==, !=, >, <, >=, <=, is, in

# 邏輯運算子
# and, or

# 延續符號的用法
# 若當行程式碼過長，可在行末使用\來分多行
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet = "abcd" + \
    "efgh" + \
    "ijkl" + \
    "mnop" + \
    "qrst" + \
    "uvwxyz"

# Slice的應用
# 變數名稱[start:end:step]; 預測開始值為0
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[:])
print(alphabet[2:])
print(alphabet[:12])
print(alphabet[-8:-3])
print(alphabet[5:20])
print(alphabet[::2])
print(alphabet[::-1])  # 反轉字串

# 常用函式
# len(變數名稱)取得字串長度
print(len(alphabet))

# .split(符號)將字串切割成串列
x = "cat,dog,bird"
print(x.split(","))

# 符號.join(變數)將串列合併成字串
y = x.split(",")
z = "&".join(y)
print(z)

# 變數名聲.find(欲尋找字串) . rfind(欲尋找字串)搜尋字串第一次出現位置
x = "cat,dog,cat,bird"
print(x.find("cat"))
print(x.rfind("cat"))

# .count(變數名稱)計算字串出現次數
print(x.count("cat"))

# .replace(old,new,count)將字串替換
print(x.replace("cat", "mouse", 1))
print(x.replace("cat", "mouse"))
