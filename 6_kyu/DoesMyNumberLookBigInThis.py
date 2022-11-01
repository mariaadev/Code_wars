def narcissistic(value):

    lst_nums = [int(x) for x in str(value)]
    len_v = len(lst_nums)
    accum = 0
    for i in lst_nums:
        accum += (i**len_v)
    
    return accum == value

