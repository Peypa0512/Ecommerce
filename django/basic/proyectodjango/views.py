from django.http import HttpResponse
from django.shortcuts import render

# definimos la funcion home con el parametro de request porque nos han solicitado algo
def home(request):
    
    # la respuesta a la solicitud
    return render(request,'home.html')