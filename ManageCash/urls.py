from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_cash/', views.add_cash_view, name='add_cash'),
    path('add_expense/', views.add_expense_view, name='add_expense'),
    path('logout/', views.logout_view, name='logout'),
]
