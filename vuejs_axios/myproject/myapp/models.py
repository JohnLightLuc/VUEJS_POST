from django.db import models

# Create your models here.
class Inscription(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images")
    statut = models.BooleanField(default=False)
    date_add = models.DateField(auto_now_add=True)
    date_up = models.DateField(auto_now=True)
