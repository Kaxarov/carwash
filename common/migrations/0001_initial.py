# Generated by Django 3.2.6 on 2022-02-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt')),
                ('title', models.CharField(max_length=128, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Mashina modeli',
                'verbose_name_plural': 'Mashina modellari',
            },
        ),
    ]