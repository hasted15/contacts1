from django.db import models

class Test(models.Model):
   testname = models.CharField(max_length=20)

class ModTest(models.Model):
   modtestname = models.CharField(max_length=20)

class Order(models.Model):
   SKU = models.CharField(max_length=20)
   Strih = models.CharField(max_length=20)
   Articul = models.CharField(max_length=20)
   NameTovara = models.CharField(max_length=20)
   BrendTovara = models.CharField(max_length=20)
   Image = models.ImageField()
   Opisanie = models.CharField(max_length=100)

