# custom_filters.py
from django import template

register = template.Library()

@register.filter
def calculer_prix_reduction(prix, pourcentage_remise):
    reduction = prix * pourcentage_remise / 100
    nouveau_prix = prix - reduction
    return nouveau_prix
