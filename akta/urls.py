from django.urls import path
from . import views

urlpatterns = [
    path('buat/', views.buat, name='buat'),
    path('', views.akta, name='akta'),
    path('detail/<str:slug>', views.detail, name='detail'),
]