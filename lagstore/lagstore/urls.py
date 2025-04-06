from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),  # Atualize este caminho para incluir as URLs da aplicação store
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
