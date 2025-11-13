# 判斷平年與閏年
# 在公曆裡有 365 天和 366 天的差異，也就衍伸有了平年和閏年的定義，這篇文章將會介紹如何透過 Python 的 if 邏輯判斷式，判斷某一年是平年還是閏年。

# 什麼是平年？什麼是閏年？
# 平年和閏年按照下方的規範來定義，只要滿足下方的規範，就是閏年，否則就是平年，閏年的二月有 29 天，平年的二月則是 28 天。

# 1. 除以 4 能整除，且除以 100 不能整除
# 2. 如果剛好是 100 的倍數，且除以 400 能整除
# 3. 舉例來說 2000 年是 100 的倍數且除以 400 能整除，所以是 2000 年是閏年，例如 2100 年雖然是 4 的倍數，但除以 100 能整除，所以 2100 年是平年。

def get_year():
    year = int(input("請輸入年份:"))
    try:
        return year if  len(str(year)) == 4 else get_year()
    except:
        return get_year()

def leap_year_detector(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    year = get_year()
    print(f"{year} 是{'閏年' if leap_year_detector(year) else '平年'}")
