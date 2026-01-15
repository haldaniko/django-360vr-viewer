from django.shortcuts import render


def home_view(request):
    lang = request.GET.get('lang', 'ua')

    template_map = {
        'en': 'english/video.html',
        'fr': 'french/video.html',
        'tr': 'turkish/video.html',
        'ua': 'ukrainian/video.html',
        'bg': 'bulgarian/video.html',
    }

    videos_map = {
        'en': {
            'cinema_dash_manifest_url': '/media/tr_cinema/manifest.mpd',
            'grounding_dash_manifest_url': '/media/tr_grounding/manifest.mpd',
            'scan_dash_manifest_url': '/media/tr_scan/manifest.mpd',
            'triangle_dash_manifest_url': '/media/tr_triangle/manifest.mpd',
            'waterfall_dash_manifest_url': '/media/tr_waterfall/manifest.mpd',
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

    template_name = template_map.get(lang, 'video.html')
    context = videos_map.get(lang, videos_map['ua'])

    return render(request, template_name, context)


def about_view(request):
    lang = request.GET.get('lang', 'ua')

    template_map = {
        'en': 'english/about.html',
        'fr': 'french/about.html',
        'tr': 'turkish/about.html',
        'ua': 'ukrainian/about.html',
        'bg': 'bulgarian/about.html',
    }

    template_name = template_map.get(lang, 'about.html')

    return render(request, template_name)


def howitworks_view(request):
    lang = request.GET.get('lang', 'ua')

    template_map = {
        'en': 'english/howitworks.html',
        'fr': 'french/howitworks.html',
        'tr': 'turkish/howitworks.html',
        'ua': 'ukrainian/howitworks.html',
        'bg': 'bulgarian/howitworks.html',
    }

    template_name = template_map.get(lang, 'howitworks.html')

    return render(request, template_name)


def guides_view(request):
    lang = request.GET.get('lang', 'ua')

    template_map = {
        'en': 'english/guides.html',
        'fr': 'french/guides.html',
        'tr': 'turkish/guides.html',
        'ua': 'ukrainian/guides.html',
        'bg': 'bulgarian/guides.html',
    }

    template_name = template_map.get(lang, 'guides.html')

    return render(request, template_name)


def results_view(request):
    lang = request.GET.get('lang', 'ua')

    template_map = {
        'en': 'english/results.html',
        'fr': 'french/results.html',
        'tr': 'turkish/results.html',
        'ua': 'ukrainian/results.html',
        'bg': 'bulgarian/results.html',
    }

    template_name = template_map.get(lang, 'results.html')

    return render(request, template_name)

