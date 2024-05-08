def squares_dictionary(n):
    dic = {}
    for i in range(1, n + 1):
        new = [(i, i*i)]
        dic.update(new)
    return dic

print(squares_dictionary(8))
