from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from treat.views import Index, Order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('order/', Order.as_view(), name='order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)