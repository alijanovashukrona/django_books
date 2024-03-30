
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    # path('kitob_ochir/',kitob_ochir),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
