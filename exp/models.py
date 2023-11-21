from django.db import models

class Expense(models.Model):
    amount = models.FloatField()
    description = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f'{self.description} - {self.amount} - {self.date}'

