from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     #Django Admin
    
    path('accounts/', include('allauth.urls')), #For auth model
    
    path('', include('pages.urls')),     #Local apps pages
    path('books/', include('books.urls')),  #URL path for books app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
