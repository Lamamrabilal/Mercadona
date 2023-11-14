# promo_app/forms.py
from django import forms
from .models import Promotion

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['pourcentage_remise', 'date_debut', 'date_fin']


# forms.py
from django import forms
from .models import Produit

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['libelle', 'description', 'prix', 'image', 'categorie']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }