from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.models import Product

from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    paginate_by = 3  # Количество продуктов на странице
    template_name = (
        "catalog/products_list.html"  # Имя шаблона для отображения списка продуктов
    )
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        if self.request.method == "POST":
            name = self.request.POST.get("name")
            phone = self.request.POST.get("phone")
            message = self.request.POST.get("message")
            print(name)
            print(phone)
            print(message)
            return HttpResponse("Сообщение отправлено!")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete_confirm.html"
    success_url = reverse_lazy("catalog:home")
    context_object_name = "product"
