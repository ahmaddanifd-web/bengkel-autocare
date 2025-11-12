from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('booking/', include('booking.urls')),
    path('payment/', include('payment.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', TemplateView.as_view(template_name='registration/register.html'), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
