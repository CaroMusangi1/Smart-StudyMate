from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dotenv import load_dotenv
load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Make sure this line is here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)