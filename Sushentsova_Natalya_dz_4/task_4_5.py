from requests import get, utils


def main(argv) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    program, code = argv
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    index_code = content.find(code)
    if index_code != -1:
        index_value = content.find("<Value>", index_code)
        value = content[index_value + 7:index_value + 12]
        result_value = float(value.replace(",", "."))   ## здесь должно оказаться результирующее значение float
    else:
        result_value = "Проверьте корректность ввода кода валюты"
    return result_value


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))

"""
Результат запуска с терминала:
PS C:\Users\User\PycharmProjects\Home-work-Python\Sushentsova_Natalya_dz_4> python task_4_5.py USD
76.65
PS C:\Users\User\PycharmProjects\Home-work-Python\Sushentsova_Natalya_dz_4> python task_4_5.py dfdd
Проверьте корректность ввода кода валюты
PS C:\Users\User\PycharmProjects\Home-work-Python\Sushentsova_Natalya_dz_4> python task_4_5.py AZN
45.11

"""