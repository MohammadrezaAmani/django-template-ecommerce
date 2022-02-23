from . import jalali

def persian_numbers_converter(str):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for i, p in numbers.items():
        str = str.replace(i, p)
    return str

def jalali_converter(time):
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    out = jalali.Gregorian(time_to_str).persian_tuple()

    out_new = "{}/{}/{},ساعت{}:{}".format(out[0], out[1], out[2], time.hour, time.minute)
    return persian_numbers_converter(out_new)