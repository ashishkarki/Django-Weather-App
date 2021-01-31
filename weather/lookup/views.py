from django.shortcuts import render


def home(request):
    import json
    import requests
    import weather_app_secrets
    import lookup.lookup_constants

    if request.method == "POST":
        zipCode = request.POST.get('zipCode', '02453')

        api_url = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+ zipCode + "&date=2021-01-27&distance=25&API_KEY=" + weather_app_secrets.API_KEY
        api_request = requests.post(api_url)

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = lookup.lookup_constants.ERROR_STRING

        ###
        # print("api: " + str(api))
        if len(api) > 0:
            CATEGORY_NAME = api[0]['Category']['Name']
        else:
            CATEGORY_NAME = "None- Goes to Else"

        category_description = ""

        if CATEGORY_NAME == "Good":
            category_description = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif CATEGORY_NAME == "Moderate":
            category_description = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particthose who are unusually sensitive to air poll"
            category_color = "moderate"
        elif CATEGORY_NAME == "Unhealthy for Sensitive Groups":
            category_description = "(101 to 150) Members of sensitive groups may experience health effects. The general public ilikely to be aff"
            category_color = "usg"
        elif CATEGORY_NAME == "Unhealthy":
            category_description = "(151 to 200) Some members of the general public may experience health effects"
            category_color = "unhealthy"
        elif CATEGORY_NAME == "Very Unhealthy":
            category_description = "(201 to 300) Health alert: The risk of health effects is increased for eve"
            category_color = "veryunhealthy"
        elif CATEGORY_NAME == "Hazardous":
            category_description = "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affect"
            category_color = "hazardous"
        else:
            category_description = "The lookup didn't return anything. Please try again."
            category_color = "blue-grey darken-1"
        ###

        return render(request, 'home.html', {
            'api': api,
            'category_color': category_color,
            'category_description': category_description,
        })
    else:  # if it a GET request in our case
        api_url = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=02452&date=2021-01-27&distance=25&API_KEY=" + weather_app_secrets.API_KEY
        api_request = requests.get(api_url)

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = lookup.lookup_constants.ERROR_STRING

        ###
        CATEGORY_NAME = api[0]['Category']['Name']
        category_description = ""
        if CATEGORY_NAME == "Good":
            category_description = "(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif CATEGORY_NAME == "Moderate":
            category_description = "(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particthose who are unusually sensitive to air poll"
            category_color = "moderate"
        elif CATEGORY_NAME == "Unhealthy for Sensitive Groups":
            category_description = "(101 to 150) Members of sensitive groups may experience health effects. The general public ilikely to be aff"
            category_color = "usg"
        elif CATEGORY_NAME == "Unhealthy":
            category_description = "(151 to 200) Some members of the general public may experience health effects"
            category_color = "unhealthy"
        elif CATEGORY_NAME == "Very Unhealthy":
            category_description = "(201 to 300) Health alert: The risk of health effects is increased for eve"
            category_color = "veryunhealthy"
        elif CATEGORY_NAME == "Hazardous":
            category_description = "(301 and higher) Health warning of emergency conditions: everyone is more likely to be affect"
            category_color = "hazardous"
        else:
            category_color = "blue-grey darken-1"
        ###

        return render(request, 'home.html', {
            'api': api or [],
            'category_color': category_color,
            'category_description': category_description,
        })


def about(request):
    return render(request, 'about.html', {})
