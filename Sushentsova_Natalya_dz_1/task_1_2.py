def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    list_of_sum = []
    sum_of_num = 0
    for num_3deg in dataset:
        sum_of_num = sum_of_num + num_3deg % 10
        if sum_of_num % 7 == 0:
            list_of_sum.append(sum_of_num)

    sum_1 = 0
    for sum_of_num in list_of_sum:
        sum_1 += sum_of_num
    return sum_1  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    new_list_of_num = []
    for num in dataset:
        new_num = num + 17
        new_list_of_num.append(new_num)

    new_list_of_sum = []
    new_sum_of_num = 0
    for new_num in new_list_of_num:
        new_sum_of_num = new_sum_of_num + new_num % 10
        if new_sum_of_num % 7 == 0:
            new_list_of_sum.append(new_sum_of_num)

    sum_2 = 0
    for new_sum_of_num in new_list_of_sum:
        sum_2 += new_sum_of_num
    return sum_2  # Верните значение полученной суммы


my_list = []
number = 1
while number <= 1000:
    if number % 2 != 0:
        my_list.append(number ** 3)
    number += 1

print(my_list)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
