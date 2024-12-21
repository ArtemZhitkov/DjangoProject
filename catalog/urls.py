from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
    ]