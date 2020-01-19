
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('products.urls', namespace='mainapp')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
