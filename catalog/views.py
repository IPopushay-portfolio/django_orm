from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


def example_view(request):
    return render(request, 'catalog/example.html')


def index(request):
    product = Product.objects.get(id=1)
    context = {
        'category': f'{product.category}',
        'prod_name': f'{product.prod_name}',
        'description': f'{product.description}',
        'image': f'{product.image}',
        'price': f'{product.price}'

    }
    return render(request, 'catalog/index.html', context)


def product_detail(request):
    product = Product.objects.get(id=1)
    context = {

        'product': product,

    }
    return render(request, 'catalog/product_detail.html', context=context)


def product_list(request):
    product = Product.objects.all()
    context = {"products": product}

    return render(request, 'catalog/product_list.html', context)


def base_test(request):
    product = Product.objects.all()
    context = {"products": product}

    return render(request, 'catalog/base_test.html', context)
