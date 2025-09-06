from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expense, UserProfile, Category

# ---------- User Registration ----------
class SimpleUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_password2(self):
        # Override password validation to remove "too short/common" restrictions
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


# ---------- Expense Form ----------
class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    recurring = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Expense
        fields = ["title", "amount", "category", "date", "notes", "recurring", "receipt"]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Expense title'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes', 'rows': 2}),
            'category': forms.Select()
        }


# ---------- Profile Form ----------
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
       
        fields = ['profile_picture', 'bio']
        
        widgets = {
            'budget': forms.NumberInput(attrs={'placeholder': 'Monthly Budget'}),
            'bio': forms.Textarea(attrs={
                'class': 'w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400',
                'placeholder': 'Tell us about yourself...',
                'rows': 3
            }),
        }
