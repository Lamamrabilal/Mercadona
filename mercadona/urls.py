# mercadona/urls.py
from django.urls import path
from .views import CatalogueView, PromotionView, AddProductView, AccueilView

urlpatterns = [
    path('', AccueilView.as_view(), name='home'),

    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('promotion/<int:produit_id>/', PromotionView.as_view(), name='promotion'),

]
