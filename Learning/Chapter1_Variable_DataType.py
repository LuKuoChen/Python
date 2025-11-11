# 變數(Variable)
# 變數名稱 = 值
# 變數會把賦予的值放在一個記憶體位置，可用id()來查詢位置

# 變數命名規則
# 1. 變數名稱只能使用以下字元:
#     a-z (小寫字母)
#     A-Z (大寫字母)
#     0-9 (數字)
#     _ (底線)
# 2. 自首不能以數字開頭
# 3. 區分大小寫
# 4. 不可為保留字(Python keywords https://docs.python.org/zh-tw/3.13/reference/lexical_analysis.html#keywords)
# 5. [建議]參照PEP8風格規範
#     函式、變數和屬性使用snake_case
#     類使用CamelCase

a = 7
x1 = 7 / 3

b = a  # 此時a和b指向同一個記憶體位置
print(a, b)
print(id(a), id(b))

a = -12  # a會改變記憶體位置；b還是之前的位置
print(a, b)
print(id(a), id(b))

b = 100  # b改變記憶體位置，原本一開始a,b指向同一個的記憶體位置被釋放(Garbage Collection垃圾回收機制)
print(a, b)
print(id(a), id(b))

# 變數進階用法
# 1. 連續指定
int1 = int2 = int3 = 10

# 2. 分別賦值
x_train, y_train = 23.5, 18.9

# 3. 交換內容
x, y = y, x
