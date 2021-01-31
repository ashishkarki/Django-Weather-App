from django.shortcuts import render


def home(request):
    import json
    import requests
    import weather_app_secrets
    import lookup.lookup_constants
    from datetime import date

    zipCode = '02453' # default zip: Boston area, MA, USA
    if request.method == "POST":
        zipCode = request.POST.get('zipCode', '02453')

    date_today = date.today()
    api_url = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+ zipCode + "&date="+ str(date_today) + "&distance=25&API_KEY=" + weather_app_secrets.API_KEY
    api_request = requests.get(api_url)

    try:
        api_response = json.loads(api_request.content)
    except Exception as e:
        api_response = lookup.lookup_constants.ERROR_STRING

    if api_response != lookup.lookup_constants.ERROR_STRING and len(api_response) > 0:
        CATEGORY_NAME = api_response[0]['Category']['Name']
    else:
        CATEGORY_NAME = "None- Goes to Else"

    category_description = ""

    if CATEGORY_NAME == "Good":
        category_description = "(0 to 50) Air quality issatisfactory, and air pollution poses little or no risk"
        category_color = "good"
    elif CATEGORY_NAME == "Moderate":
        category_description = "(51 to 100) Air quality isacceptable. However, there may be a risk for somepeople, particthose who are unusually sensitive to airpoll"
        category_color = "moderate"
    elif CATEGORY_NAME == "Unhealthy for Sensitive Groups":
        category_description = "(101 to 150) Members ofsensitive groups may experience health effects. Thegeneral public ilikely to be aff"
        category_color = "usg"
    elif CATEGORY_NAME == "Unhealthy":
        category_description = "(151 to 200) Some members ofthe general public may experience health effects"
        category_color = "unhealthy"
    elif CATEGORY_NAME == "Very Unhealthy":
        category_description = "(201 to 300) Health alert: Therisk of health effects is increased for eve"
        category_color = "veryunhealthy"
    elif CATEGORY_NAME == "Hazardous":
        category_description = "(301 and higher) Health warningof emergency conditions: everyone is more likely to beaffect"
        category_color = "hazardous"
    else:
        category_description = "The lookup didn't returnanything. Please try again."
        category_color = "blue-grey darken-1"
    ###

    return render(request, 'home.html', {
        'api': api_response,
        'category_color': category_color,
        'category_description': category_description,
    })


def about(request):
    return render(request, 'about.html', {})
