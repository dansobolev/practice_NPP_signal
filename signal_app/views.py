import json

from django.shortcuts import HttpResponse
from django.http import JsonResponse

from .models import Assembly, BaseProduct
from .enums import TypeEnum
from .exceptions import ObjectDoesNotExist

from .tree_transform_django import bd_to_dict


def show_tree(request):
    assembly = Assembly.objects.all()
    base_products = BaseProduct.objects.all()

    response = bd_to_dict(assembly, base_products)

    return JsonResponse(response)


def save_data(request):
    body = json.loads(request.body)
    type_ = TypeEnum(int(body['type'])).name
    body.update({'type': type_.title()})

    # if model != TypeEnum(type)
    if type_ != TypeEnum.ASSEMBLY.name:
        try:
            Assembly.objects.filter(number=body['vhod']).get()
        except Assembly.DoesNotExist:
            raise ObjectDoesNotExist("Object doesn't exist.")

        new_db_object = BaseProduct.objects.create(
            decimal_number=body['number'],
            name=body['name'],
            entry_number=body['vhod'],
            count_number=3,
            product_type=type_
        )
        new_db_object.save()

        return HttpResponse(request, '')

    new_db_object = Assembly.objects.create(
        decimal_number=body['number'],
        name=body['name'],
        entry_number=body['vhod'],
    )
    new_db_object.save()

    return HttpResponse(request, '')
