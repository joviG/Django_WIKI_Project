from django.urls import path

from . import views

# tip: important to type 'slash/' at the end of the new created 'path'
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="entry"),
    path("new-page/", views.new_page, name="new page"),
    path("save-page", views.save_page, name="save page"),
    path("save-page/<str:title>", views.save_page, name="save edited page")
]
