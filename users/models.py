from django.db import models

# Create your models here.

class referrer(models.Model):
    firstName=models.CharField(max_length=150)
    lastName=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=254)
    company=models.CharField(max_length=150)

    class Meta:
        db_table='referrer'
