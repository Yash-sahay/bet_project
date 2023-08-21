from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='AutoBest Api')),
    path('verify/', include('autobest_master.urls')),
    path('api/v1/procurement/', include("procurement.urls")),
    path('api/v1/refub/', include("refub.urls")),
    path('api/v1/checklist_app/', include("checklist_app.urls")),
    path('api/v1/vendor/', include("vendor.urls")),
    path('api/v1/inventory/', include("inventory.urls")),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
