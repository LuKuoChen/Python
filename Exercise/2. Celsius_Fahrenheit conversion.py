# 攝氏/華氏轉換公式

# 華氏溫標的定義是：「標準大氣壓下，冰的熔點為 32°F，水的沸點為 212°F」，
# 1970 年以前，英國及其前殖民地國家多使用華氏溫標，20世紀後期，
# 全球絕大多數國家開始向國際單位制轉換，使用攝氏溫標替代了華氏溫標，
# 而攝氏溫標的定義為：「標準大氣壓下，冰的熔點為 0°C，水的沸點為 100°C」


def get_setting():
    try:
        setting = int(input("請輸入 1)攝氏 2)華氏:"))
        if setting not in [1, 2]:
            raise
        else:
            return setting
    except:
        get_setting()


def get_tempreture():
    try:
        return float(input("請輸入溫度(數字):"))
    except:
        get_tempreture()


def tempreture_conversion(setting, tempreture):
    if setting == 1:
        return tempreture * 1.8 + 32
    else:
        return (tempreture - 32) / 1.8


if __name__ == "__main__":
    setting = get_setting()
    tempreture = get_tempreture()
    print(
        f"{'攝氏' if setting==1 else '華氏'} {tempreture} 度, {'華氏' if setting==1 else '攝氏'}為 {tempreture_conversion(setting=setting,tempreture=tempreture):.2f} 度"
    )
