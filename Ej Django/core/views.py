from django.shortcuts import render, HttpResponse

def home(request):
    titulo = "Inicio"
    
    productos = ['computadores', 'impresoras', 'monitores']
    
    data= {
        "titulo": titulo,
        "productos":productos
        }
    return render(request, "core/home.html")
    
def contacto(request):
    msj = "<h1>Contacto</h1>"
    return render(request, "core/contacto.html")
    
