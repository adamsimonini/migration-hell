from tokenize import blank_re
from django.db import models

# Create your models here.

class BaseObject(models.Model): # https://docs.djangoproject.com/en/4.1/topics/db/models/#model-inheritance
    class Meta: # https://docs.djangoproject.com/en/4.1/ref/models/options/#available-meta-options
        abstract = True # https://docs.djangoproject.com/en/4.1/topics/db/models/#abstract-base-classes
        ordering = ['name'] # https://docs.djangoproject.com/en/4.1/ref/models/options/#ordering

    name = models.CharField(max_length=100) # https://docs.djangoproject.com/en/4.1/ref/models/fields/

class Farmer(BaseObject):
    age = models.IntegerField()
    is_married = models.BooleanField()

class Farm(BaseObject):
    PRODUCT = [
        ('dairy', 'Dairy'),
        ('poultry', 'Poultry'),
        ('flower', 'Flower'),
        ('organic', 'Organic'),
        ('fish', 'Fish'),
        ('apiary', 'Bee yard'),
        ('hay', 'Hay'),
    ]
    CATEGORY = [
        ('commercial', 'Commercial'),
        ('cooperative', 'Cooperative'),
    ]
    product = models.CharField(
        max_length = 40,
        choices = PRODUCT,
    )
    category = models.CharField(
        max_length = 40,
        choices = CATEGORY,
    )
    municipality = models.CharField(max_length=150)
    # we'll have to add a default value to province, since we have records in the database and we didn't set blank to true.
    # try setting "blank=True" afterwards, and see what happens in the migration files.
    province = models.CharField(max_length=50, blank=True)
    # the related_name field allows for a "reverse relationship"
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='farms') # https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/#many-to-one-relationships


