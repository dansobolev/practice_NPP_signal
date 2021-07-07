
def flatten(lst):
    flatted_lst = []
    for i in lst:
        if str(i).isdigit():
            flatted_lst.append(i)
        else:
            flatted_lst.extend(flatten(i))
    return flatted_lst


# Преобразование списка потомков в список предков
def to_ancestors_list(desc_list):
    anc_list = []
    n = max(flatten(desc_list)) + 1
    for i in range(n):
        try:
            anc_list.append(list(map(lambda x: i in x, desc_list)).index(1))
        except ValueError:
            anc_list.append(-1)
    return anc_list


# Преобразование списка предков в список потомков
def to_descendants_list(anc_list):
    ancs_list = anc_list.copy()
    desc_list = []
    n = len(ancs_list) + 1
    for i in range(n):
        n_descs = sum(map(lambda x: x == i, ancs_list))
        i_descs = []
        for _ in range(n_descs):
            indx = ancs_list.index(i)
            ancs_list[indx] = -1
            i_descs.append(indx)
        desc_list.append(i_descs)
    return desc_list


'''
# список непосредственных потомков
descendants_list = [[1, 2, 3], [4, 5, 6],
                    [], [], [7], [8], [],
                    [9, 10], [], [], []]

# список непосредственных предков
ancestors_list = [-1, 0, 0, 0, 1, 1, 1, 4, 5, 7, 7]

print(to_ancestors_list(descendants_list))
print(to_descendants_list(ancestors_list))
'''
