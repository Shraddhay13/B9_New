from django.db import models

# Create your models here.


# table - column - data types - length - primary key - column name

class Student(models.Model):
    # id -- django gives a default id column -- primary key = True
    name = models.CharField(max_length=100)
    marks = models.BigIntegerField()
    address = models.CharField(max_length=200)