def repeats(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    sum_once = 0
    for num, count in count_dict.items():
        if count == 1:
            sum_once += num
    return sum_once