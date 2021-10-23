from django.shortcuts import render, HttpResponse
import datetime
from calendar import HTMLCalendar

# Create your views here.

def hello(request):
    # inicializando variáveis
    name = request.GET.get('name')
    year = request.GET.get('year')
    month = request.GET.get('month')
    now = datetime.datetime.now()
    time = now.strftime('%I:%M:%S %p')

    if not name:
        name = " Seu nome pode aparecer aqui: /helo/?seu nome "

    if year:
        current_year = int(year)
        current_month = int(month)
    else:
        current_year = now.year
        current_month = now.month

    month = datetime.date(1900, current_month, 1).strftime('%B')

    #criando um calendário
    cal = HTMLCalendar().formatmonth(current_year, current_month)

    #return HttpResponse('<h1>Hello Desenvolvedor. </h1>')
    return render(request, 'home.html', {
        "name": name,
        "year": year,
        "month": month,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })