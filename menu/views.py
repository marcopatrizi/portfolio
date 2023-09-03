from django.shortcuts import render
# Create your views here.

def  home(request):
    nome = 'Cecilia'
    return render(request, 'index.html', {'nome': nome})
