from django.db import models

# Create your models here.

class referrer(models.Model):
    firstName=models.CharField(max_length=150)
    lastName=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=254)
    university=models.CharField(max_length=150,default='scu')
    company=models.CharField(max_length=150,default='google')
    role=models.CharField(max_length=150,default='sde')
    linkedin=models.CharField(max_length=150,default='https://linkedin.com/')


    class Meta:
        db_table='referrer'

