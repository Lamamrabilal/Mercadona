from datetime import timezone

from django.shortcuts import render

# promo_app/views.py

from django.shortcuts import render
from django.views import View
from .models import Produit, Promotion

class CatalogueView(View):
    template_name = 'promo_app/catalogue.html'

    def get(self, request, *args, **kwargs):
        produits = Produit.objects.all()
        promotions = Promotion.objects.filter(date_fin__gte=timezone.now())
        context = {'produits': produits, 'promotions': promotions}
        return render(request, self.template_name, context)
