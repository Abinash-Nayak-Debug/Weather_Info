from django.shortcuts import render
import requests

# Create your views here.

def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '009b0729122f3b3926902284a9356003'  # Replace with your actual API key
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        response = requests.get(api_url)
        weather_data = response.json()

        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }

        return render(request, 'weather/weather.html', context)
    else:
        return render(request, 'weather/weather.html')
