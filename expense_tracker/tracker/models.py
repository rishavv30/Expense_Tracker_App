from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Categories
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# User profile for extra info like profile picture & budget
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Expenses
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)
    recurring = models.BooleanField(default=False)
    receipt = models.ImageField(upload_to='receipts/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
