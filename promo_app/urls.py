from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from promo_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promo_app/', include('mercadona.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)