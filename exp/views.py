from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    all_expenses = Expense.objects.all()
    all_time_expenses = all_expenses
    last_month = timezone.now() - timedelta(days=30)
    last_month_expenses = all_expenses.filter(date__gte=last_month)


    last_week = timezone.now() - timedelta(days=7)
    last_week_expenses = all_expenses.filter(date__gte=last_week)

    return render(request, 'exp/expense_list.html', {
        'all_time_expenses': all_time_expenses,
        'last_month_expenses': last_month_expenses,
        'last_week_expenses': last_week_expenses,
    })


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'exp/add_expense.html', {'form': form})

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'exp/edit_expense.html', {'form': form, 'expense': expense})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    expense.delete()
    return redirect('expense_list')


