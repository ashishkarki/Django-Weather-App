from django.shortcuts import render


def home(request):
    import json
    import requests
    import weather_app_secrets

    api_url = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=02452&date=2021-01-27&distance=25&API_KEY=" + weather_app_secrets.API_KEY
    api_request = requests.get(api_url)

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
