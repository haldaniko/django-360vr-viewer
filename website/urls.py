from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('home/', home_view, name='video'),
    path('howitworks/', home_view, name='howitworks'),
    path('guides/', home_view, name='guides'),
    path('results/', home_view, name='results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

