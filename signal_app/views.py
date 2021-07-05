from django.shortcuts import render, HttpResponse
from .models import Assembly, Detail, StandardProduct, OtherProduct
import json
import enum


class ObjectDoesNotExist(Exception):
    pass


class TypeEnum(enum.Enum):
    ASSEMBLY = 0
    DETAIL = 1
    STANDARD_PRODUCTS = 2
    OTHER_PRODUCTS = 3

    __mapping__ = {
        'ASSEMBLY': 'Cборка',
        'DETAIL': 'Деталь',
        'STANDARD_PRODUCTS': 'Стандартные изделия',
        'OTHER_PRODUCTS': 'Прочие изделия',
    }


def index(request):
    return render(request, 'base.html')


def show_tree(request):
    assembly = Assembly.objects.all()
    for i in assembly:
        print(i.number)
    return render(request, 'base.html')


def save_data(request):
    body = json.loads(request.body)
    type_ = TypeEnum(int(body['type'])).name
    body.update({'type': type_.title()})

    model = eval(body['type'])
    # if model != TypeEnum(type)
    if model != TypeEnum.ASSEMBLY.name:
        try:
            item_parent = Assembly.objects.filter(number=body['vhod']).get()
        except Assembly.DoesNotExist:
            raise ObjectDoesNotExist("Object doesn't exist.")

        new_db_object = model.objects.create(
            number=body['number'],
            name=body['name'],
            entry_number=item_parent.id,
            count_number=3
        )
        new_db_object.save()

    model = eval(body['type'])  # converts string type to Python Class object
    new_db_object = model.objects.create(
        number=body['number'],
        name=body['name'],
        entry_number=body['vhod']
    )
    new_db_object.save()

    return_new_object = model.objects.all().last()
    print(return_new_object)
    return HttpResponse(request, {'Hello': 'world'})
