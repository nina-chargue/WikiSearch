from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.content, name="content"),
    path('search/', views.search, name='search'),
    path('newpage/', views.new_page, name='new_page'),
    path('edit/<str:title>/', views.edit_page, name='edit_page'),
    path("randompage/", views.random_page, name="random_page"),
]
