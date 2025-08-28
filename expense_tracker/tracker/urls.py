from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Home page
    path('login/', views.user_login, name='login'),   # Custom login
    path('logout/', views.user_logout, name='logout'),# Custom logout
    path('add/', views.add_expense, name='add_expense'), # Add expense
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'), # Edit
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('register/', views.register, name='register'),


  
]

