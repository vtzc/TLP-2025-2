from django.shortcuts import render, HttpResponse
from .models import Contacto
import requests

def home(request):

    url_api =  "https://api.gael.cloud/general/public/clima/SCVM"
    conexion_api = requests.get(url_api)
    datos_api = conexion_api.json()
    
    dpa_api = "https://apis.modernizacion.cl/dpa/regiones"
    conexion_dpa = requests.get(dpa_api)
    datos_dpa = conexion_dpa.json()

    titulo = "Inicio"

    productos = ['computadores','periféricos','servidores']
    
    data = {
        "titulo": titulo,
        "productos":productos,
        "clima": datos_api,
    }
     
    #return HttpResponse(titulo)
    return render(request,'core/home.html',data)
    
def contacto(request):
    titulo = "Contacto"

    if request.POST:
        #capturar el mensaje
        nombre = request.POST["txtNombre"]
        email = request.POST["txtEmail"]
        mensaje = request.POST["txtMensaje"]

        #validaciones de negocio

        #crear nuevo objeto
        nuevoContacto = Contacto()
        nuevoContacto.nombre = nombre
        nuevoContacto.email = email
        nuevoContacto.mensaje = mensaje

        nuevoContacto.save()



    return render(request,'core/contacto.html')