from django.shortcuts import render, HttpResponse
from django.conf import settings
import json
import facebook

def index(request):
    # Retrieve the access token from Django settings
    token = getattr(settings, 'FACEBOOK_ACCESS_TOKEN', None)

    if not token:
        return HttpResponse("Access token not configured.", status=500)

    try:
        graph = facebook.GraphAPI(access_token=token)
        user_data = graph.get_object('me', fields='id,name,gender,email')

        return HttpResponse(json.dumps(user_data, indent=4), content_type='application/json')
    except facebook.GraphAPIError as e:
        return HttpResponse(f"Facebook API Error: {e}", status=500)
