def find_nb(m): 
    n = 1 
    volume = 0
    while volume < m:
        volume = volume + n**3 
        if volume == m: 
            return n 
        n =  n + 1 
    return -1 
