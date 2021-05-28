def reverse_list(x):
    x.reverse()
    for i in x:
        i.reverse_list()
    return x
print(ters([[1, 2], [3, 4], [5, 6, 7]]))
