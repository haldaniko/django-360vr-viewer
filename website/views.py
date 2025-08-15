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
        'cinema_dash_manifest_url': '/media/ua_cinema/manifest.mpd',
        'grounding_dash_manifest_url': '/media/ua_grounding/manifest.mpd',
        'scan_dash_manifest_url': '/media/ua_scan/manifest.mpd',
        'triangle_dash_manifest_url': '/media/ua_triangle/manifest.mpd',
        'waterfall_dash_manifest_url': '/media/ua_waterfall/manifest.mpd',
    })


def test_view(request):
    return render(request, 'mobile.html', {
        'cinema_dash_manifest_url': '/media/ua_cinema/manifest.mpd',
        'grounding_dash_manifest_url': '/media/ua_grounding/manifest.mpd',
        'scan_dash_manifest_url': '/media/ua_scan/manifest.mpd',
        'triangle_dash_manifest_url': '/media/ua_triangle/manifest.mpd',
        'waterfall_dash_manifest_url': '/media/ua_waterfall/manifest.mpd',
    })
