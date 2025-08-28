from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expense

# ================== Expense Form ==================
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["title", "amount", "category"]

# ================== User Registration Form ==================
class SimpleUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1")  # only username + password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove all default help_text
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
