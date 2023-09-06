from django.shortcuts import render
from Todo_app.models import Task
from django.shortcuts import render
from .models import Reminder
import requests
import datetime

def base(request):
    return render(request,'dashboard.html')
def create_todo_item(request):
    if (request.method == 'POST'):
        print(request.POST)
        u = request.POST['u']
        b = Task.objects.create(title=u,completed=False)
        b.save()
    s = Task.objects.all()
    return render(request, 'Todolist.html', {'task': s})
def DeleteTask(request,title):
    get_todo = Task.objects.get(title=title)
    get_todo.delete()
    return create_todo_item(request)
def Update(request, title):
    get_todo = Task.objects.get(title=title)
    get_todo.completed = True
    get_todo.save()
    return create_todo_item(request)
def weather(request):
    cities = ['Berlin', 'New York', 'London', 'Paris', 'Tokyo']
    appid = 'cb6dd4c22f3296906114c8292b284910'
    URL = 'https://api.openweathermap.org/data/2.5/weather'

    weather_data = []

    for city in cities:
        params = {'q': city, 'appid': appid, 'units': 'metric'}
        r = requests.get(url=URL, params=params)
        res = r.json()
        description = res['weather'][0]['description']
        icon = res['weather'][0]['icon']
        temp = res['main']['temp']
        day = datetime.date.today()

        city_weather = {
            'city': city,
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
        }

        weather_data.append(city_weather)

    return render(request, 'weather.html', {'weather_data': weather_data})
def reminder_page(request):
    if request.method == "POST":
        name = request.POST["name"]
        time = request.POST["time"]
        Reminder.objects.create(name=name, time=time)


    reminders = Reminder.objects.all()
    return render(request, "reminder.html", {"reminders": reminders})