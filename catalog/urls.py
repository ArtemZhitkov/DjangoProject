from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.ProductListView.as_view(), name="home"),
    path("contacts/", views.ContactTemplateView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("add_product", views.ProductCreateView.as_view(), name="add_product"),
    path(
        "edit_product/<int:pk>/", views.ProductUpdateView.as_view(), name="edit_product"
    ),
    path(
        "delete_product/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="delete_product",
    ),
]
