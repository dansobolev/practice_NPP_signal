import json

from django.shortcuts import render, HttpResponse

from .models import Assembly, BaseProduct
from .enums import TypeEnum
from .exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'base.html')


def show_tree(request):
    assembly = BaseProduct.objects.all()
    for i in assembly:
        print(i.product_type)
    return render(request, 'base.html')


def save_data(request):
    body = json.loads(request.body)
    type_ = TypeEnum(int(body['type'])).name
    body.update({'type': type_.title()})

    # if model != TypeEnum(type)
    if type_ != TypeEnum.ASSEMBLY.name:
        try:
            item_parent = Assembly.objects.filter(number=body['vhod']).get()
        except Assembly.DoesNotExist:
            raise ObjectDoesNotExist("Object doesn't exist.")

        new_db_object = BaseProduct.objects.create(
            number=body['number'],
            name=body['name'],
            entry_number=item_parent.id,
            count_number=3,
            product_type=type_
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
