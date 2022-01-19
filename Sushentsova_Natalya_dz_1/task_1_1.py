def convert_time(duration: int) -> str:
    duration_day = duration // 86400
    duration_day_remainder = duration % 86400
    duration_our = duration_day_remainder // 3600
    duration_our_remainder = duration_day_remainder % 3600
    duration_min = duration_our_remainder // 60
    duration_min_remainder = duration_our_remainder % 60
    duration_sec_remainder = duration_min_remainder % 60
    str_out = str
    if duration_day != 0:
        str_out = f"{duration_day} дн, {duration_our} час, {duration_min} мин, {duration_sec_remainder} сек"
    elif duration_day == 0 and duration_our != 0:
        str_out = f"{duration_our} час, {duration_min} мин, {duration_sec_remainder} сек"
    elif duration_day == 0 and duration_our == 0 and duration_min != 0:
        str_out = f"{duration_min} мин, {duration_sec_remainder} сек"
    elif duration_day == 0 and duration_our == 0 and duration_min == 0:
        str_out = f"{duration_sec_remainder} сек"
    return str_out


duration = 406560
result = convert_time(duration)
print(result)
