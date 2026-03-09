from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        scheme = 'https' if request.is_secure() else 'http'
        host = request.get_host()
        base_url = f"{scheme}://{host}/api/"
    return Response({
        'users': base_url + 'users/',
        'userprofiles': base_url + 'userprofiles/',
        'activities': base_url + 'activities/',
        'teams': base_url + 'teams/',
        'leaderboard': base_url + 'leaderboard/',
        'workouts': base_url + 'workouts/',
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.api_urls')),
]
