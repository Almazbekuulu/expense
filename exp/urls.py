from django.urls import path
from .views import expense_list, add_expense, edit_expense, delete_expense

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('expenses/add/', add_expense, name='add_expense'),
    path('expenses/edit/<int:expense_id>/', edit_expense, name='edit_expense'),
    path('expenses/delete/<int:expense_id>/', delete_expense, name='delete_expense'),
]
