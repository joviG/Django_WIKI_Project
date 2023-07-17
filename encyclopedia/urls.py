from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="index"),
    path('<str:title>/', views.encyclopedia_entry, name='encyclopedia_entry')
]
