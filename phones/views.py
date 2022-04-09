from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    phone_objects = Phone.objects.all()
    template = 'catalog.html'
    phones = [phone for phone in phone_objects]
    if sort is not None:
        if sort == 'max_price':
            phones.sort(key=lambda x: x.price, reverse=True)
        elif sort == 'min_price':
            phones.sort(key=lambda x: x.price)
        elif sort == 'name':
            phones.sort(key=lambda x: x.name)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    context = {'phone': phone_object}
    return render(request, template, context)
