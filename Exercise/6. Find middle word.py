# 找出中間的字元

# 當使用者輸入文字之後，透過 len() 的方法得到字串的長度，將長度除以二，再透過文字的取值，就能夠得到一段字串中間的字元。
# 參考：len() 取得字串長度、取得字元與字串


def get_string():
    try:
        string_check = input("請輸入字串:")
        return string_check if len(string_check) != 0 else get_string()
    except:
        get_string()


def get_middle_word(x):
    if len(x) % 2 == 0:
        return x[len(x) // 2 - 1]+ x[len(x) // 2]
    elif len(x) % 2 == 1:
        return x[len(x) // 2]

if __name__ == "__main__":
    print(f"中間的字元為: {get_middle_word(get_string())}")
