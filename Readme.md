## Django - Calendário

**Fazer um calendário rápido e simples.**



Vamos utilizar uma função do python que retorna um calendário HTML.

A proposta é ter uma pagina home, onde passamos o nome do Dev, ano e mês e recebemos a imagem abaixo:

__Instalando e iniciando__

```
- instalar o python
- instalar o django
- instalar a virtualenv
- criar uma pasta para app - a minha ficou como Core

```

**Imagem**

![Calendario](C:\workspace\django\Img\Calendario.png)

**app - (helloworld)**

​	url.py

```
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url='/hello/')),
    path('hello/<nome>/<int:idade>', views.hello),
    path('hello/', views.hello),
    path('admin/', admin.site.urls),
]
```



​	settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
```



**pasta core**

​	views.py

```
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
```

**templates**

​	home.html

```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Hello Word</title>
</head>
<body>
    <center>
        <h1>Hello {{ name  }}! Calendário de {{ month }} {{ year }} </h1>

        hora atual {{ time }}
        <br/> <br/>

            {{ cal | safe }}
        <br/><br/><br/><br/>
        Copyright (c) {{ current_year }}
    </center>
</body>
</html>
```
