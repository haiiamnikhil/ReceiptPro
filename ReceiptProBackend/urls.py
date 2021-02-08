from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)