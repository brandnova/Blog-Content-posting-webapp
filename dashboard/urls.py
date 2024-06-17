from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('products', views.products, name='products'),
    path('dashboard/allinfo/', views.allinfo, name='allinfo'),
    path('dashboard/info/<int:pk>/', views.info, name='info'),
    path('dashboard/single_message/<int:pk>/', views.info, name='single_message'),
    path('info', views.info, name='info'),
]