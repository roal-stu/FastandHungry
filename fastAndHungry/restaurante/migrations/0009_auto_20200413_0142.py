# Generated by Django 3.0.3 on 2020-04-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0008_auto_20200410_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='a@gmail.com', help_text='Required', max_length=200),
        ),
    ]
