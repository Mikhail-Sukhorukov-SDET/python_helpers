def flatten(l, res=None):
    if res == None:
        res = []
    for i in l:
        if isinstance(i, list):
            flatten(i, res)
        else:
            res.append(i)
    return res

flatten([1, [2, 3, [4]], 5]) # вернет [1,2,3,4,5]
flatten([1, [2,3], [[2], 5], 6]) # вернет [1,2,3,2,5,6]
flatten([[[[9]]], [1,2], [[8]]]) # вернет [9,1,2,8]