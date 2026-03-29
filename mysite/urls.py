from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    # Ana sayfaya (boş adres) geleni direkt /polls/ adresine gönderir
    path('', lambda request: redirect('polls/', permanent=True)), 

    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]