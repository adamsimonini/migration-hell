# Generated by Django 4.0.5 on 2022-10-12 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('married', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.CharField(choices=[('dairy', 'Dairy'), ('poultry', 'Poultry'), ('flower', 'Flower'), ('organic', 'Organic'), ('fish', 'Fish'), ('apiary', 'Bee yard'), ('hay', 'Hay')], max_length=40)),
                ('category', models.CharField(choices=[('commercial', 'Commercial'), ('cooperative', 'Cooperative')], max_length=40)),
                ('municipality', models.CharField(max_length=150)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farming.farmer')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
