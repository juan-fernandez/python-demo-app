def my_mean(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return (list[0] + list[1]) / 2

    return sum(list) / len(list)
