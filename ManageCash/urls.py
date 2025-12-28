from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("add_cash/", views.add_cash_view, name="add_cash"),
    path("edit_cash/<int:pk>/", views.edit_cash_view, name="edit_cash"),
    path("delete_cash/<int:pk>/", views.delete_cash_view, name="delete_cash"),
    path("add_expense/", views.add_expense_view, name="add_expense"),
    path("edit_expense/<int:pk>/", views.edit_expense_view, name="edit_expense"),
    path("delete_expense/<int:pk>/", views.delete_expense_view, name="delete_expense"),
    path("logout/", views.logout_view, name="logout"),
]
