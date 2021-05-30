def flatten(x):
    for i in x:
        if type(i)==list:
            flatten(i)
        else:
            list1.append(i)
            x.remove(i)
            flatten(x)
    return list1
list1=[]
data=[[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(data))
