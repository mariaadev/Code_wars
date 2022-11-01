
def find_outlier(integers):
    odd = []
    even = []
    result = 0
    for i in integers:
        if i % 2 != 0:
            odd.append(i)
        elif i% 2 == 0:
            even.append(i)
    if len(odd) < len(even):
        result = odd[0]
    else:
        result = even[0]
    
    return result


