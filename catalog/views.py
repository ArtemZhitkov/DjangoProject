from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category


def home_view(request):
    products = Product.objects.all()
    p = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        page_obj = p.get_page(page)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'products_list.html', context)


# def products_list(request):
#     # Получение всех продуктов из БД
#     products = Product.objects.all()
#     return render(request, 'products_list.html', {'products': products})


def product_detail(request, pk):
    # Получение продукта из БД по его ID
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def contacts_view(request):
    return render(request, 'contacts.html')


def contact(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        print(name)
        print(message)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contact.html')


def add_product(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')  # Загрузка изображения продукта (если оно есть)
        stock = request.POST.get('stock')
        # Создание нового продукта
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            category_id=category_id,
            image=image,
            stock=stock,
        )
        return HttpResponse(f"Продукт '{product.name}' успешно добавлен.")
    # Формирование формы добавления продукта
    categories = Category.objects.all()
    return render(request, 'add_product.html', {'categories': categories})