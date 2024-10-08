from django.contrib import admin
from django.urls import path, include

from app.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name='home'),

    path('tarefas/', include('tarefas.urls')), 

    path('registros/', include('registros.urls')),
]
