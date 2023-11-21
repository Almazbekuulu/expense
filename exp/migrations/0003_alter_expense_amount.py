

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0002_rename_category_expense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.FloatField(),
        ),
    ]
