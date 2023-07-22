from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="index"),
    path('wiki/<str:title>', views.entry_page, name='entry_page'),
    path('new-page', views.new_page, name='new page')
]
