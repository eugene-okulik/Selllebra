words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def multiple_print(**kwargs):
    for word, count in kwargs.items():
        print(word * count)


multiple_print(**words)
