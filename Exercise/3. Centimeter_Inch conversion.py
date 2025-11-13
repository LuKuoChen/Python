# 長度換算公式
# 世界上常用的長度單位有公制和英制，公制就是公釐、公分、公尺、公里...等，英制則是碼、英尺、英吋...等，單位之間可以透過下方的公式互相轉換。

# 1 公尺 = 100 公分 = 1000 公釐
# 1 碼 = 3 英尺 = 36 英吋
# 1 公尺 = 1.0936 碼 = 3.281 英尺
# 1 公分 = 0.394 英吋


def get_setting():
    try:
        setting = int(input("請輸入 1)公分 2)英吋:"))
        return setting if setting in [1, 2] else get_setting()
    except:
        get_setting()


def get_length():
    try:
        return float(input("請輸入長度(數字):"))
    except:
        get_length()


def centimeter_inch_conversion(setting, length):
    centimeter, inch, yard = 0, 0, 0
    if setting == 1:
        centimeter = length
        inch = length * 0.394
        yard = length * 0.394 / 36
        return centimeter, inch, yard
    else:
        centimeter = length / 0.394
        inch = length
        yard = length / 36
        return centimeter, inch, yard


if __name__ == "__main__":
    setting=get_setting()
    length=get_length()
    if setting == 1:
        print(
            f"{length} 公分等於 {centimeter_inch_conversion(setting=setting,length=length)[1]} 英吋({centimeter_inch_conversion(setting=setting,length=length)[2]} 碼)"
        )
    else:
        print(
            f"{length} 英吋等於 {centimeter_inch_conversion(setting=setting,length=length)[0]} 公分({centimeter_inch_conversion(setting=setting,length=length)[2]} 碼)"
        )
