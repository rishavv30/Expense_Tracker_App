from django.core.management.base import BaseCommand
from tracker.models import Expense
from datetime import date

class Command(BaseCommand):
    help = 'Create recurring expenses for the new month'

    def handle(self, *args, **kwargs):
        today = date.today()
        recurring_expenses = Expense.objects.filter(recurring=True)
        for exp in recurring_expenses:
            Expense.objects.create(
                user=exp.user,
                title=exp.title,
                amount=exp.amount,
                category=exp.category,
                date=today,
                notes=exp.notes,
                recurring=True
            )
        self.stdout.write(self.style.SUCCESS('Recurring expenses created'))
