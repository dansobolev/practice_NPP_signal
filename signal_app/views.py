import ast
from datetime import datetime
import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from openpyxl import Workbook
from openpyxl.styles import PatternFill

from users.models import UserProfile
from .models import Assembly, BaseProduct
from .enums import TypeEnum
from .exceptions import ObjectDoesNotExist
from .tree_transform_django import bd_to_dict, dict_to_table, ancestors_list, id_dict, delete_edge
from users.permissions import project_permissions_required, ProjectPermissions
from .trees_algorithms import to_descendants_list


def get_all_items_from_bd():
    return Assembly.objects.all(), BaseProduct.objects.all()


def bd_to_dict_helper(check_empty_bd: bool = False):
    assembly, base_products = get_all_items_from_bd()
    if check_empty_bd:
        if assembly.count() == 0 and base_products.count() == 0:
            return JsonResponse({"": ""})

    return bd_to_dict(assembly, base_products)


def index(request):
    return render(request, 'base.html')


@login_required
@project_permissions_required(
    permissions=[ProjectPermissions.PERM_PROJECT_UPDATE, ProjectPermissions.PERM_PROJECT_READ]
)
def show_tree(request):
    response = bd_to_dict_helper(check_empty_bd=True)

    return JsonResponse(response)


@login_required
@project_permissions_required(permissions=[ProjectPermissions.PERM_PROJECT_UPDATE])
def save_data(request):
    body = json.loads(request.body)
    type_ = TypeEnum(int(body['type']))
    body.update({'type': type_.name.title()})

    if type_.name != TypeEnum.ASSEMBLY.name:
        try:
            Assembly.objects.filter(decimal_number=body['number']).get()
        except Assembly.DoesNotExist:
            return JsonResponse({"message": "Данная сборка отсутствует в базе. Перепроверьте данные."})

        new_db_object = BaseProduct.objects.create(
            decimal_number=body['number'],
            name=body['name'],
            entry_number=body['vhod'],
            count_number=3,
            product_type=type_.value
        )
        new_db_object.save()

        # test: retrieve just created object from db
        created_object = BaseProduct.objects.get(decimal_number=body['number'])
        print(created_object)

        return HttpResponse(request, status=204)

    new_db_object = Assembly.objects.create(
        decimal_number=body['number'],
        name=body['name'],
        entry_number=body['vhod'],
    )
    new_db_object.save()

    # test: retrieve just created object from db
    created_object = Assembly.objects.get(decimal_number=body['number'])
    print(created_object)

    return HttpResponse(request, status=204)


@login_required
@project_permissions_required(permissions=[ProjectPermissions.PERM_PROJECT_UPDATE])
def delete_entity(request):
    data = json.loads(request.body)
    item_type = TypeEnum(int(data['type']))
    if 'decimal_number' in data:
        assembly, base_products = get_all_items_from_bd()
        product_dict = bd_to_dict_helper(check_empty_bd=False)
        ancs_list = ancestors_list(assembly, base_products)
        descs_list = to_descendants_list(ancs_list)
        id_d = id_dict(assembly, base_products)

        items_to_delete = delete_edge(data['decimal_number'], item_type.value, product_dict, ancs_list, descs_list, id_d)
        try:
            for item in items_to_delete:
                item_decimal_number, item_type_ = item[0], item[2]
                bd_model = 'Assembly' if item_type_ == 'assembly' else 'BaseProduct'
                item_to_delete = ast.literal_eval(bd_model).objects.filter(decimal_number=item_decimal_number).get()
                item_to_delete.delete()
        except Exception as e:
            return JsonResponse({"error": "Cannot find item with provided decimal number."})

    return JsonResponse({"status_code": 200, "message": "Item has been successfully deleted."})


@login_required
@project_permissions_required(permissions=[ProjectPermissions.PERM_PROJECT_UPDATE])
def edit_entity(request):
    data = json.loads(request.body)
    item_type = TypeEnum(int(data['type']))
    if 'decimal_number' and 'fields_to_edit' in data:
        bd_model = 'Assembly' if item_type == TypeEnum.ASSEMBLY else 'BaseProduct'
        try:
            item_to_edit = ast.literal_eval(bd_model).objects.filter(decimal_number=data['decimal_number']).get()
        except Exception as e:
            return JsonResponse({"error": "Cannot find item with provided decimal number."})
        # блок выполнится, если не вызвалось исключение выше (айтем не был найден в БД)
        else:
            fields_to_edit = data['fields_to_edit']
            for field in fields_to_edit.keys():
                try:
                    item_to_edit.field = fields_to_edit[field]
                except Exception:
                    return JsonResponse({"error": "Provided field doesn't exist."})
            item_to_edit.save()

    return JsonResponse({"status_code": 200, "message": "Item has been successfully edited."})


@login_required
@project_permissions_required(permissions=[ProjectPermissions.PERM_PROJECT_READ])
def export_page(request):
    current_user = UserProfile.objects.filter(user=request.user).get()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Products(created at {date} by {user}).xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
        user=current_user.firstname + current_user.lastname,
    )
    resp = bd_to_dict_helper(check_empty_bd=False)
    tab = dict_to_table(resp)
    type_dict = {
        0: 'Сборка',
        1: 'Деталь',
        2: 'Стандартное изделие',
        3: 'Прочие изделия',
        'assembly': 'Сборка'}
    t = list(map(lambda x: type_dict[x[-1]], tab))
    c = 1
    for i in range(len(tab)):
        tab[i][-1] = t[i]
        tab[i].insert(0, c)
        c += 1
    cols = ['ID', 'Децимальный номер', 'Наименование', 'Первичная входимость', 'Принадлежность']
    tab.insert(0, cols)
    color_dict = {
        'Сборка': '93C47D',
        'Деталь': 'E2EFDA',
        'Стандартное изделие': 'FCE4D6',
        'Прочие изделия': 'D9E1F2'
    }
    wb = Workbook()
    ws = wb.active
    # Заполнение
    for row, r in zip(ws.iter_rows(min_row=1, max_row=len(tab), max_col=len(tab[0])), tab):
        for cell, v in zip(row, r):
            cell.value = v
    # Форматирование
    for cell in list(ws)[1]:
        cell.fill = PatternFill(start_color='38761D',
                                end_color='38761D',
                                fill_type='solid')
    for row in list(ws)[2:]:
        color = color_dict[row[-1].value]
        for cell in row:
            cell.fill = PatternFill(start_color=color,
                                    end_color=color,
                                    fill_type='solid')
    wb.save(response)
    return response
