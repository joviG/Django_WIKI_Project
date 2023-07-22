from django.urls import path

from . import views

# tip: important to type 'slash/' at the end of the new created 'path'
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="index"),
    path('wiki/<str:title>/', views.entry_page, name='entry_page'),
    path('new-page/', views.new_page, name='new page')
]
