# 檢查重複字元

# 判斷字元是否重複的方法，就是判斷每個字元在字串中出現的次數，如果出現的次數大於 1 表示有重複，就用 repeat 串列紀錄，如果出現次數等於 1 表示沒有重複，就用 not_repeat 串列記錄，如此一來就能夠篩選出重複與不重複的字元。
# 參考：str.count()、in 檢查內容是否存在、for 迴圈


def get_string():
    try:
        string_check = input("請輸入字串:")
        return string_check if len(string_check) != 0 else get_string()
    except:
        get_string()


def duplicate_check(x):
    repeat = []
    not_repeat = []
    for i in x:
        if x.count(i) > 1 and i not in repeat:
            repeat.append(i)
        elif x.count(i) <= 1 and i not in not_repeat:
            not_repeat.append(i)
    return sorted(repeat), sorted(not_repeat)


if __name__ == "__main__":
    repeat, not_repeat = duplicate_check(get_string())
    print(f"重複字元為:{repeat}")
    print(f"不重複字元為:{not_repeat}")
