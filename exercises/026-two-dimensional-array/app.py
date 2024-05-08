def two_dimensional_list(x,y):
    m = []
    for i in range(x):
        r = []
        for j in range(y):
            r.append(i*j)
        m.append(r)
    return m

print(two_dimensional_list(1,10))