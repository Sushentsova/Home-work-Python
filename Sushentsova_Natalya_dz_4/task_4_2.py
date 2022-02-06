from requests import get, utils


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    index_code = content.find(code)
    if index_code != -1:
        index_value = content.find("<Value>", index_code)
        value = content[index_value + 7:index_value + 12]
        result_value = float(value.replace(",", "."))   ## здесь должно оказаться результирующее значение float
    else:
        return
    return result_value


print(currency_rates("USD"))
print(currency_rates("noname"))
