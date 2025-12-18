from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AddCash, Expense
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def dashboard_view(request):
    addcash_transactions = AddCash.objects.filter(user=request.user)
    expense_transactions = Expense.objects.filter(user=request.user)
    total_income = sum(t.amount for t in addcash_transactions)
    total_expenses = sum(t.amount for t in expense_transactions)
    balance = total_income - total_expenses
    context = {
        'addcash_transactions': addcash_transactions,
        'expense_transactions': expense_transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_cash_view(request):
    if request.method == 'POST':
        source = request.POST['source']
        amount = request.POST['amount']
        description = request.POST['description']
        AddCash.objects.create(
            user=request.user,
            source=source,
            amount=amount,
            description=description,
            datetime=timezone.now()
        )
        messages.success(request, 'Cash added successfully.')
        return redirect('dashboard')
    return render(request, 'add_cash.html')

@login_required
def add_expense_view(request):
    if request.method == 'POST':
        description = request.POST['description']
        amount = request.POST['amount']
        Expense.objects.create(
            user=request.user,
            description=description,
            amount=amount,
            datetime=timezone.now()
        )
        messages.success(request, 'Expense added successfully.')
        return redirect('dashboard')
    return render(request, 'add_expense.html')

def logout_view(request):
    logout(request)
    return redirect('login')
