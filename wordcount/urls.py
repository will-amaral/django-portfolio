from django.urls import path
from . import views

urlpatterns = [
    path("", views.count_index, name="count_index"),
    path("result/", views.count_result, name="count_result"),
    path("error/", views.count_error, name="count_error")
]