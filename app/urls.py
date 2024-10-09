from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name='home'),

    path('tarefas/', include('tarefas.urls')), 

    path('registros/', include('registros.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
