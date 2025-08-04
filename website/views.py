from django.shortcuts import render


def video_view(request):
    lang = request.GET.get('lang', 'en')

    template_map = {
        'en': 'video_en.html',
        'fr': 'video_fr.html',
        'tr': 'video_tr.html',
        'ua': 'video_ua.html',
        'bg': 'video_bg.html',
    }

    template_name = template_map.get(lang, 'video_en.html')

    return render(request, template_name, {
        'dash_manifest_url': '/media/video1/manifest.mpd'
    })
