# mercadona/urls.py
from django.template.context_processors import static
from django.urls import path, re_path
from promo_app import settings
from .views import CatalogueView, PromotionView, AddProductView, AccueilView

urlpatterns = [
    path('', AccueilView.as_view(), name='home'),

    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('promotion/<int:produit>/', PromotionView.as_view(), name='promotion'),

]
