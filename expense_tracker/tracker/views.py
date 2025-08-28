from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm, SimpleUserCreationForm
# from .forms import ExpenseForm, SimpleUserCreationForm




# ================= USER REGISTRATION =================
def register(request):
    if request.method == "POST":
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
    else:
        form = SimpleUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


# ================= AUTHENTICATION =================

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # after login, go to home
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "registration/login.html")



def user_logout(request):
    logout(request)
    return redirect("login")


# ================= EXPENSE MANAGEMENT =================

@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expense = sum(exp.amount for exp in expenses)
    return render(request, "tracker/home.html", {
        "expenses": expenses,
        "total_expense": total_expense
    })


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # link expense to logged-in user
            expense.save()
            messages.success(request, "Expense added successfully!")
            return redirect("home")
    else:
        form = ExpenseForm()
    return render(request, "tracker/add_expense.html", {"form": form})


@login_required
def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id, user=request.user)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated successfully!")
            return redirect("home")
    else:
        form = ExpenseForm(instance=expense)

    return render(request, "tracker/edit_expense.html", {"form": form})


@login_required
def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id, user=request.user)
    expense.delete()
    messages.success(request, "Expense deleted successfully!")
    return redirect("home")
