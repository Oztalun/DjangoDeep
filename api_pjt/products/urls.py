from django.urls import path
from . import views


app_name = "articles"
urlpatterns = [
    path("", views.product_list, name="product_list"),
]
