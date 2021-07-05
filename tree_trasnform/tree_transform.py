
import pandas as pd
import trees_algorithms as ta
from pprint import pprint


# ---| Загрузка данных |---
data = pd.read_csv('data.csv')
assembly = data[['Децимальный номер', 'Наименовании позиции',
                 'Первичная входимость', 'Применяемость, шт.', 'Принадлежность']]

# Кодирование принадлежности (для занесения в словарь в значение принадлежность)
dict_type = {'Сборка': 'assembly',
             'Деталь': 'detail',
             'Стандартные изделия': 'sp',
             'Прочие изделия': 'op'}

assembly2 = assembly.copy()
assembly2['Принадлежность'] = assembly['Принадлежность'].map(dict_type)


# Отображение: дец. номер -> id (id - номер строки в БД)
def dict_1(frame):  # takes pandas DataFrame
    return {frame.iloc[i]['Децимальный номер']: i for i in frame.index}


# Пребразование БД в список непосредственных предков
def ancestors_list(frame):  # takes pandas DataFrame
    d = dict_1(frame)
    anc_lst = [-1]              # TODO: С учетом того, что список в БД уже упорядочен, иначе нужно искать,
    for i in frame.index[1:]:   # TODO: какая вершина корневая и сопоставлять ее номеру в списке предков -1
        anc_lst.append(d[frame.iloc[i]['Первичная входимость']])
    return anc_lst


# Преобразование БД во вложенный словарь
def bd_to_dict(frame, k=0, descs_lst=None):  # TODO: k=0 С учетом того, что список в БД уже упорядочен, иначе нужно
    '''                                      # TODO: искать, какой номер у корневой вершины
    frame: Pandas DataFrame
    k: Номер текущей вершины
    descs_lst: Список непосредственных потомков
    '''
    if descs_lst is None:
        descs_lst = ta.to_descendants_list(ancestors_list(frame))
    # Формирование словаря для текущей детали
    names = ['Принадлежность', 'Децимальный номер', 'Наименовании позиции',
             'Применяемость, шт.', 'Первичная входимость']
    values = frame.iloc[k][names]               # TODO: можно не переупорядочивать, если заранее (при создании изделия,
    d = {n: v for n,v in zip(names, values)}    # TODO: а соответственно при создании БД) упорядочить столбцы в БД как нужно
    d['sub'] = []
    # Формирование потомков для текущей детали
    for i in descs_lst[k]:
        d['sub'].append(bd_to_dict(frame, i, descs_lst))
    # Вывод вложенного словаря
    return d


pprint(bd_to_dict(assembly2))
