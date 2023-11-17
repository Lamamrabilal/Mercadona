from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
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
    def get(self, request, produit, *args, **kwargs):
        produit_obj = get_object_or_404(Produit, id=produit)
        promotions = Promotion.objects.filter(produit=produit_obj, date_fin__gte=timezone.now())
        context = {'promotions': promotions, 'produit': produit_obj}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, produit, *args, **kwargs):
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=True)
            promotion.produit = get_object_or_404(Produit, id=produit)
            return redirect('mercadona:promotion', produit_id=produit)
        context = {'form': form, 'produit': get_object_or_404(Produit, id=produit)}
        return render(request, self.template_name, context)

def is_admin(user):
    return user.is_authenticated and user.is_staff

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class AddProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'mercadona/add_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            produit_id = new_product.id
            return redirect('promo_app:promotion', produit_id=produit_id)
        return render(request, 'mercadona/add_product.html', {'form': form})

class AccueilView(View):
    template_name = 'mercadona/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
