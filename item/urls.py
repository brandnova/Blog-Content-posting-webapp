from django.urls import include, path
from . import views

app_name = 'items'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk/add_comment/', views.add_comment, name='add_comment'),

]

