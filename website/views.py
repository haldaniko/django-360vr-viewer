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

    videos_map = {
        'en': {
            'cinema_dash_manifest_url': '/media/en_cinema/manifest.mpd',
            'grounding_dash_manifest_url': '/media/en_grounding/manifest.mpd',
            'scan_dash_manifest_url': '/media/en_scan/manifest.mpd',
            'triangle_dash_manifest_url': '/media/en_triangle/manifest.mpd',
            'waterfall_dash_manifest_url': '/media/en_waterfall/manifest.mpd',
        },
        'fr': {
            'cinema_dash_manifest_url': '/media/fr_cinema/manifest.mpd',
            'grounding_dash_manifest_url': '/media/fr_grounding/manifest.mpd',
            'scan_dash_manifest_url': '/media/fr_scan/manifest.mpd',
            'triangle_dash_manifest_url': '/media/fr_triangle/manifest.mpd',
            'waterfall_dash_manifest_url': '/media/fr_waterfall/manifest.mpd',
        },
        'tr': {
            'cinema_dash_manifest_url': '/media/tr_cinema/manifest.mpd',
            'grounding_dash_manifest_url': '/media/tr_grounding/manifest.mpd',
            'scan_dash_manifest_url': '/media/tr_scan/manifest.mpd',
            'triangle_dash_manifest_url': '/media/tr_triangle/manifest.mpd',
            'waterfall_dash_manifest_url': '/media/tr_waterfall/manifest.mpd',
        },
        'ua': {
            'cinema_dash_manifest_url': '/media/ua_cinema/manifest.mpd',
            'grounding_dash_manifest_url': '/media/ua_grounding/manifest.mpd',
            'scan_dash_manifest_url': '/media/ua_scan/manifest.mpd',
            'triangle_dash_manifest_url': '/media/ua_triangle/manifest.mpd',
            'waterfall_dash_manifest_url': '/media/ua_waterfall/manifest.mpd',
        },
        'bg': {
            'cinema_dash_manifest_url': '/media/bg_cinema/manifest.mpd',
            'grounding_dash_manifest_url': '/media/bg_grounding/manifest.mpd',
            'scan_dash_manifest_url': '/media/bg_scan/manifest.mpd',
            'triangle_dash_manifest_url': '/media/bg_triangle/manifest.mpd',
            'waterfall_dash_manifest_url': '/media/bg_waterfall/manifest.mpd',
        },
    }

    template_name = template_map.get(lang, 'video_en.html')
    context = videos_map.get(lang, videos_map['en'])

    return render(request, template_name, context)



def about_view(request):
    lang = request.GET.get('lang', 'en')

    template_map = {
        'en': 'about_en.html',
        'fr': 'about_fr.html',
        'tr': 'about_tr.html',
        'ua': 'about_ua.html',
        'bg': 'about_bg.html',
    }

    template_name = template_map.get(lang, 'about_en.html')

    return render(request, template_name)
