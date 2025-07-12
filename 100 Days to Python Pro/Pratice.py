# 定義元組
t = ('駱昊', 38, True, '四川成都')
print(t)
# 獲取元組中的元素
print(t[0])
print(t[3])
# 遍歷元組中的值
for member in t:
    print(member)
# 重新給元組賦值
# t[0] = '王大錘'  # TypeError
# 變數t重新引用了新的元組原來的元組將被垃圾回收
t = ('王大錘', 20, True, '雲南昆明')
print(t)
# 將元組轉換成列表
person = list(t)
print(person)