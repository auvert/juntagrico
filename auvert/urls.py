from django.urls import path, include
from django.contrib import admin
from django.conf import settings
import juntagrico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impersonate/', include('impersonate.urls')),
    path('', include('juntagrico.urls')),
]

if 'juntagrico_billing' in settings.INSTALLED_APPS:
    urlpatterns.append(path('', include('juntagrico_billing.urls')))
