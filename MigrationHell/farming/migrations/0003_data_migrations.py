# Generated by Django 4.1.2 on 2022-10-13 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("farming", "0002_farm_province"),
    ]

    operations = [
         migrations.RunSQL("INSERT INTO farming_farm (name, product, category, municipality, province, farmer_id) VALUES ('Napa Vally Farm', 'dairy', 'commercial', 'Smokey Wood', 'British Columbia', 1);")
    ]
