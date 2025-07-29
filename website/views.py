from django.shortcuts import render


def video_view(request):
    return render(request,
                  'video.html',
                  {'dash_manifest_url': '/media/video1/manifest.mpd'})
