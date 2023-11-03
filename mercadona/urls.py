# mercadona/urls.py
from django.urls import path
from .views import CatalogueView, PromotionView

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('promotion/<int:produit_id>/', PromotionView.as_view(), name='promotion'),

]
