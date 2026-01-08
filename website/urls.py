from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    home_view,
    about_view,
    howitworks_view,
    guides_view,
    results_view
)

urlpatterns = [
    path('about/', about_view, name='about'),
    path('home/', home_view, name='video'),
    path('howitworks/', howitworks_view, name='howitworks'),
    path('guides/', guides_view, name='guides'),
    path('results/', results_view, name='results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
