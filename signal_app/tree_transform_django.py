
from .trees_algorithms import to_descendants_list
from pprint import pprint


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
        ancs_lst = ancestors_list(assembly, basep)
        descs_lst = to_descendants_list(ancs_lst)
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
    # Возвращает словарь изделия, список предков, список потомков
    return d


def find_path(k, ancs_lst, descs_lst):
    if ancs_lst[k] != -1:
        return [k] + find_path(ancs_lst[k], ancs_lst, descs_lst)
    else:
        return [k]


def add_edge(id, name, vhod, type, product_dict, ancestors_list, descendants_list, id_dict):
    '''
    param: id - Децимальный номер добалвяеомго изделия
    param: name - Наименование добавляемого изделия
    param: vhod - Дециальный номер предка (первичная входимость)
    param: type - Тип добавляемого объекта (assembly, detail)
    param: product_dict - Словарь изделия
    param: ancestors_list - Список непосредственных предков дерева
    param: descendants_list - Список непосредственных потомков дерева
    param: id_dict - Отображение (дец. номер -> номер вершины)
    '''
    k = len(ancestors_list)  # Номер добавляемой вершины
    # Обновление информации о дереве
    p_id_dict = id_dict.copy()  # Обновление словаря (дец. номер -> номер вершины)
    p_id_dict[id] = k
    ancs_lst = ancestors_list + [p_id_dict[vhod]]  # Обновление списка непосредственных предков
    descs_lst = descendants_list + [[]]  # Обновление списка непосредственных потомков
    descs_lst[p_id_dict[vhod]].append(k)
    # Добавление вершины в словарь изделия
    prod_dict = product_dict.copy()
    t = prod_dict
    path = list(reversed(find_path(k, ancs_lst, descs_lst)))[1:-1]
    for i in path:
        j = list(map(lambda x: p_id_dict[x['id']], t['sub_assembly'])).index(i)
        t = t['sub_assembly'][j]
    current_dict = {'id': id, 'name': name, 'vhod': vhod, 'type': type, 'sub_assembly': [], 'sub_details': []}
    if type:  # Если type != 0, то добавляется деталь
        t['sub_details'].append(current_dict)
    else:
        t['sub_assembly'].append(current_dict)
    return prod_dict


def dict_to_table(product_dict):
    table = [(product_dict['id'], product_dict['name'], product_dict['vhod'], product_dict['type'])]
    if product_dict['sub_details']:  # Если список деталей не пуст
        for i in product_dict['sub_details']: # TODO: Полагаем, что внутри деталей нет других деталей
            table.append((i['id'], i['name'], i['vhod'], i['type']))
    if product_dict['sub_assembly']:  # Если список подсборок не пуст
        for i in product_dict['sub_assembly']:
            table.extend(dict_to_table(i))
    return table


# Список потомков по словарю
# TODO: Функция не работает
def dict_to_descs_lst(product_dicts, edge_c=1, id_dict=None):
    if id_dict is None:
        id_dict = dict()
    if product_dicts:
        descs_lst = []  # Список потомков (Номера) для всех вершин на данном уровне
        for i in product_dicts:  # Рассматриваем конкретную вершину
            descs_lst_d = []  # Список потомков (словари) для конкретной вершины
            descs_lst_n = []  # Список потомков (номера) для конкретной вершины
            # Сборки (потомки)
            assembly_descs_d = []
            assembly_descs_n = []
            for j in i['sub_assembly']:  # Рассматриваем конкретного потомка вершины
                assembly_descs_d.append(j)  # Добалвение словаря потомка
                assembly_descs_n.append(edge_c)  # Добалвение номера потомка
                id_dict[i['id']] = edge_c  # Добалвение отображения (дец. ном. потомка -> ном. вершины)
                edge_c += 1
            descs_lst_d.extend(assembly_descs_d)
            descs_lst_n.extend(assembly_descs_n)
            # Детали (потомки)
            detail_descs_d = []
            detail_descs_n = []
            for j in i['sub_details']:  # Рассматриваем конкретного потомка вершины
                detail_descs_d.append(j)  # Добалвение словаря потомка
                detail_descs_n.append(edge_c)  # Добалвение номера потомка
                id_dict[i['id']] = edge_c  # Добалвение отображения (дец. ном. потомка -> ном. вершины)
                edge_c += 1
            descs_lst_d.extend(detail_descs_d)
            descs_lst_n.extend(detail_descs_n)
            descs_lst.append(descs_lst_n)
            return descs_lst
    else:
        return []
    return 'error'


# TODO: Реализуй удаление через формирование словаря и всего остального по готовой таблице
def delete_edge(id, type, product_dict, ancs_lst, descs_lst, id_dict):
    '''
    param: k - Номер удаляемой вершины
    param: product_dict - Словарь изделия
    param: ancestors_list - Список непосредственных предков дерева
    param: descendants_list - Список непосредственных потомков дерева
    param: id_dict - Отображение (дец. номер -> номер вершины)
    '''
    # Удаление вершины из словаря
    k = id_dict[id]  # Номер удаляемой вершины
    prod_dict = product_dict.copy()
    t = prod_dict
    path = list(reversed(find_path(k, ancs_lst, descs_lst)))[1:]
    for i in path[:-1]:
        j = list(map(lambda x: id_dict[x['id']], t['sub_assembly'])).index(i)
        t = t['sub_assembly'][j]
    if type:  # Если type != 0, то удаляется деталь
        j = list(map(lambda x: id_dict[x['id']], t['sub_details'])).index(path[-1])
        deleted = t['sub_details'][j].copy()
        t['sub_details'].pop(j)
    else:
        j = list(map(lambda x: id_dict[x['id']], t['sub_assembly'])).index(path[-1])
        deleted = t['sub_assembly'][j].copy()
        t['sub_assembly'].pop(j)
    # Обновление информации о дереве
    return dict_to_descs_lst([prod_dict])
    return prod_dict
