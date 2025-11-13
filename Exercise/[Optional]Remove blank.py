# 去除中英文夾雜的空白 (進階)

# 在一些中英文夾雜的寫作規範裡，往往會強調中文英文和標點符號的寫作規範，這篇教學所採用的規範如下：
# 1. 中文字和英文字中間要有空白。
# 2. 除了括號外，其他標點符號使用「全形標點符號」。
# 3. 括號左右需要有空白，括號和括號之間不留空白。
# 4. 全形標點符號左右不留空白。

# 參考：使用正規表達式 re、合併串列

import re

# 要轉換的字串
text = """請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
"""

# 取得中文字和英文單字的正規表達式
# [a-zA-Z0-9]+ 表示開頭是英文字母後面連接一串字母或數字
regex = re.compile(r"[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+")

arr = re.findall(regex, text)

print(arr)

# def get_string():
#     try:
#         string_check = input("請輸入字串:")
#         return string_check if len(string_check) != 0 else get_string()
#     except:
#         get_string()

# def remove_blank(x):
#     return x.replace(" ", "")

# if __name__ == "__main__":
#     print(remove_blank(get_string()))
