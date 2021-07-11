import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Assembly, BaseProduct
from .enums import TypeEnum
from .exceptions import ObjectDoesNotExist
from .tree_transform_django import bd_to_dict
from users.permissions import project_permissions_required, ProjectPermissions


def index(request):
    return render(request, 'base.html')


@login_required
@project_permissions_required(
    permissions=[ProjectPermissions.PERM_PROJECT_UPDATE, ProjectPermissions.PERM_PROJECT_READ]
)
def show_tree(request):
    assembly = Assembly.objects.all()
    base_products = BaseProduct.objects.all()
    if assembly.count() == 0 and base_products.count() == 0:
        return JsonResponse({"": ""})

    response = bd_to_dict(assembly, base_products)

    return JsonResponse(response)  # ожидает словарь


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
        bd_model = 'Assembly' if item_type == TypeEnum.ASSEMBLY else 'BaseProduct'
        try:
            assembly = eval(bd_model).objects.filter(decimal_number=data['decimal_number']).get()
            assembly.delete()
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
            item_to_edit = eval(bd_model).objects.filter(decimal_number=data['decimal_number']).get()
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
