from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import video_view, about_view

urlpatterns = [
    path('', about_view, name='about'),
    path('video/', video_view, name='video')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

