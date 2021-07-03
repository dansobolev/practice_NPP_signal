from django.shortcuts import render
from .models import Assembly, Detail, StandardProduct, OtherProduct


def index(request):
    return render(request, 'base.html')


def show_tree(request):
    assemblies = Assembly.objects.all()
    details = Detail.objects.all()
    standard_products = StandardProduct.objects.all()
    other_products = OtherProduct.objects.all()
    print(assemblies)
    print(details)
    print(standard_products)
    print(other_products)
    return render(request, 'base.html')
