from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import video_view, test_view

urlpatterns = [
    path('', video_view, name='video'),
    path("mobile/", test_view, name="mobile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
