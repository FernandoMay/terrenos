from django.shortcuts import render
from catalogo.models import Terrenos

# Create your views here.
def mostrarCatalogo(request):
    terrenos = list()
    objetos = Terrenos.objects.all()
    for u in objetos:
        terrenos.append({
            'dueño': u.name,
            'fondo': u.fondo,
            'frente': u.frente,
            'precio': u.precio,
            'url_imagen': u.imagen,
        },)
    dec = [{
        'dueño': 'Ed',
        'fondo': '20m',
        'frente': '10m',
        'precio': '200',
        'url_imagen': 'https://s3.amazonaws.com/mercado-ideas/wp-content/uploads/sites/2/2018/09/10120620/09-terrenos.jpg',
    },
    {
        'dueño': 'Edd',
        'fondo': '30m',
        'frente': '15m',
        'precio': '350',
        'url_imagen': 'https://www.grupofarko.com/hs-fs/hubfs/terreno%20de%20inversion%20premium.jpg?width=1200&name=terreno%20de%20inversion%20premium.jpg',
    }]
    return render(request, 'base.html',{'datos': terrenos})