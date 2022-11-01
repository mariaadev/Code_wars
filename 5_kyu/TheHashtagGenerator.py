def generate_hashtag(s): 
    return  "#" + "".join(i.capitalize() for i in s.split()) if s and len(s) <= 140 else False


