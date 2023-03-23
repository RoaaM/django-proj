from django.shortcuts import render

# Create your views here.
# we connect views with templets and with models(database)
# dtl for templets 
# dtl--> django templets languages

def index(request):
    data = {'name':'roaa mamoun abdelqader sartawi',
             'age':'24'}
    return render(request, 'pages/index.html', data)

def about(request):
    return render(request, 'pages/about.html')