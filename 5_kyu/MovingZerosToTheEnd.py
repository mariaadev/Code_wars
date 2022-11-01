def move_zeros1(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
        
    return lst

