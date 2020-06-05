# Generated by Django 3.0.3 on 2020-06-03 12:42

from django.db import migrations, models
import django.db.models.deletion
import restaurante.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=280)),
                ('image', models.ImageField(null=True, upload_to=restaurante.models.element_image_directory_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.Category')),
            ],
        ),
    ]
