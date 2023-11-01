from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return self.libelle

class Produit(models.Model):

    libelle = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')

    def __str__(self):
        return self.libelle

class Promotion(models.Model):

    produit = models.OneToOneField(Produit, on_delete=models.CASCADE, related_name='promotion')
    pourcentage_remise = models.DecimalField(max_digits=5, decimal_places=2)
    date_debut = models.DateField(default=timezone.now)
    date_fin = models.DateField()

    def __str__(self):
        return f"Promotion sur {self.produit.libelle}"
