from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(name)
        print(message)
        return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
    return render(request, 'catalog/contacts.html')


def products_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {

        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)
