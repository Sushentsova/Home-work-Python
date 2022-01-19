def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    digit = number % 10
    if digit == 1 and number != 11:  # все цифры оканчивающиеся на 1
        return f"{number} процент"
    elif 2 <= digit <= 4:  # все цифры оканчивающиеся на 2, 3, 4
        return f"{number} процента"
    else:
        return f"{number} процентов"


for n in range(1, 101):
    print(transform_string(n))
