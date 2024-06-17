from django.contrib.auth import views as auth_views

from django.urls import path, include

from . import views

from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('todo/', views.todo, name='todo'),
    path('edit_todo/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='core/sign-in.html', authentication_form=LoginForm), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
