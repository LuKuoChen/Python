# 參考下列用電度數區間，設計一個計算電費的小程式。

# 電度數 0～200 度，每度 3.2 元。
# 電度數 201～ 300 度，每度 3.4 元。
# 電度數大於 300 度，每度 3.6 元。


def get_electricity():
    try:
        x = float(input("請輸入用電度數(數字):"))
        if x < 0:
            return get_electricity()
        else:
            return x
    except:
        return get_electricity()


def electricity_bill(x):
    if x <= 200:
        return x * 3.2
    elif x <= 300:
        return 200 * 3.2 + (x - 200) * 3.4
    else:
        return 200 * 3.2 + 100 * 3.4 + (x - 300) * 3.6


if __name__ == "__main__":
    x = get_electricity()
    print(f"用電 {x}度, 電費為 {str(electricity_bill(x))} 元")
