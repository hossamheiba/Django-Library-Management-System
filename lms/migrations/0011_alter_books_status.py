# Generated by Django 5.0.6 on 2024-06-09 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0010_alter_books_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable'), ('مستأجر', 'مستأجر')], max_length=50),
        ),
    ]
