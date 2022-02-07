def get_uniq_numbers(src: list):
    # unique_src = [el for el in src if src.count(el) == 1] - решение в лоб
    unique_src = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_src.add(el)
        else:
            unique_src.discard(el)
        tmp.add(el)
    unique_set = [el for el in src if el in unique_src]
    return unique_set


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
