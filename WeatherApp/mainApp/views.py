from django.shortcuts import render
import requests
import datetime

# Unsplash API Key (Replace with your actual key)
UNSPLASH_API_KEY = "y63o6CFLR9e2hAG5l_gzGEETFZXdT8q6O2WsTg50Anc"
UNSPLASH_URL = "https://api.unsplash.com/search/photos"

def home(request):
    city = request.POST.get('city', 'Nairobi')  # Default to Nairobi

    # OpenWeather API Call
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=78e6ad87cc9b4462ba61caf41284dc16'
    PARAMS = {'units': 'metric'}

    try:
        response = requests.get(url, params=PARAMS)
        response.raise_for_status()  
        data = response.json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

    except (requests.RequestException, KeyError, IndexError):
        description = "Weather data not available"
        icon = "default.png"  
        temp = "N/A"

    # Fetch City Image from Unsplash
    image_url = "https://source.unsplash.com/1600x900/?city"  # Default image

    try:
        headers = {
            "Authorization": f"Client-ID {UNSPLASH_API_KEY}"
        }
        image_response = requests.get(UNSPLASH_URL, headers=headers, params={"query": city})
        image_response.raise_for_status()
        image_data = image_response.json()
        
        # Get the first image from the results
        if image_data['results']:
            image_url = image_data['results'][0]['urls']['regular']

    except (requests.RequestException, KeyError):
        pass  # Use default image

    day = datetime.date.today()

    return render(request, 'index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
        'image_url': image_url
    })