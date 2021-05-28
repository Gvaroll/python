def ters(x):
    x.reverse()
    for i in x:
        i.reverse()
    return x
print(ters([[1, 2], [3, 4], [5, 6, 7]]))