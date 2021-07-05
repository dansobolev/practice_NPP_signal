
from .trees_algorithms import to_descendants_list


# Отображение: дец. номер -> id (id - номер строки в БД)
def id_dict(assembly, basep):
    str_count = 0  # Счетчик количества срок
    d = dict()  # Отображение: дец. номер -> id
    for i in assembly:
        d[i.decimal_number] = str_count
        str_count +=1
    for i in basep:
        d[i.decimal_number] = str_count
        str_count +=1
    return d


# Пребразование БД в список непосредственных предков
def ancestors_list(assembly, basep):
    d = id_dict(assembly, basep)
    ancs_lst = [-1]  # TODO: С учетом того, что крень дерева первый в табилце assembly
    for j in [assembly[1:], basep]:
        for i in j:
            ancs_lst.append(d[i.entry_number])
    return ancs_lst


# Преобразование БД во вложенный словарь
def bd_to_dict(assembly, basep, k=0, descs_lst=None):
    if descs_lst is None:
        descs_lst = to_descendants_list(ancestors_list(assembly, basep))
    # Формирование словаря для текущей детали
    # names = ['id', 'name', 'amount', 'vhod', 'type']
    names = ['id', 'name', 'vhod', 'type']
    n = len(assembly)
    if k < n:
        values = [assembly[k].decimal_number, assembly[k].name, assembly[k].entry_number, 'assembly']
    else:
        values = [basep[k-n].decimal_number, basep[k-n].name, basep[k-n].entry_number, basep[k-n].product_type]
    d = {n: v for n, v in zip(names, values)}
    d['sub_assembly'] = []
    d['sub_details'] = []
    # Формирование потомков для текущей детали
    for i in descs_lst[k]:
        if i < n:
            d['sub_assembly'].append(bd_to_dict(assembly, basep, i, descs_lst))
        else:
            d['sub_details'].append(bd_to_dict(assembly, basep, i, descs_lst))
    return d

