from django.urls import path
from mercadona.views import CatalogueView

app_name = 'mercadona'
urlpatterns =[
    path('', CatalogueView.as_view(),name ='catalogue')
]