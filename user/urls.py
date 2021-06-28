from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('listUser/', views.listUser),
    path('listProfile/', views.listProfile),
    path('listOrder/', views.listOrder),
    path('listUserDetail/<int:key>/', views.listDetailUser),
    path('CreateUser/', views.CreateUser),
    path('CreateProfile', views.CreateProfile),
    path('DeleteUser/<str:key>/', views.DeleteUser),
    path('CreateOrder/', views.CreateOrder)
]

