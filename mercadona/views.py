# promo_app/views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import PromotionForm, ProductForm
from .models import Categorie, Produit, Promotion


class CatalogueView(View):
    template_name = 'mercadona/catalogue.html'

    def get(self, request, timezgione=None, *args, **kwargs):
        categories = Categorie.objects.all()
        produits = Produit.objects.all()
        promotions = Promotion.objects.filter(date_fin__gte=timezone.now())
        context = {'categories': categories, 'produits': produits, 'promotions': promotions}
        return render(request, self.template_name, context)


class PromotionView(View):
    template_name = 'mercadona/promotion.html'

    @method_decorator(login_required)
    def get(self, request, produit_id, *args, **kwargs):
        produit = Produit.objects.get(pk=produit_id)
        form = PromotionForm(initial={'produit': produit})
        return render(request, self.template_name, {'form': form, 'produit': produit})

    @method_decorator(login_required)
    def post(self, request, produit_id, *args, **kwargs):
        produit = Produit.objects.get(pk=produit_id)
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.produit = produit
            promotion.save()
            return redirect('catalogue')  # Rediriger vers le catalogue après ajout de la promotion
        return render(request, self.template_name, {'form': form, 'produit': produit})



@method_decorator(login_required, name='dispatch')
class AddProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'mercadona/add_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        return render(request, 'add_product.html', {'form': form})



class AccueilView(View):
    template_name = 'mercadona/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CustomLoginView(LoginView):
    template_name = 'login.html'


