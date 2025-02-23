from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("product/create/", views.createProducts, name="create_product")
]
