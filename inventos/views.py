from django.shortcuts import render
from django.http import Http404

# Create your views here.
inventos_rotor = [
    {"id": 1, "nombre": "Bio-detector de Robians", "categoria": "Deteccion",
     "nivel_eficacia": 8.7, "estado": "operativo", "descripcion": "Detecta animales convertidos en robots por Robotnik."},

    {"id": 2, "nombre": "Turbo-planeador", "categoria": "Transporte",
     "nivel_eficacia": 7.3, "estado": "operativo", "descripcion": "Vehiculo aereo ligero para misiones de reconocimiento."},

    {"id": 3, "nombre": "Escudo de energia portatil", "categoria": "Defensa",
     "nivel_eficacia": 6.5, "estado": "en pruebas", "descripcion": "Genera una barrera temporal contra ataques laser."},

    {"id": 4, "nombre": "Comunicador subterraneo", "categoria": "Comunicaciones",
     "nivel_eficacia": 9.0, "estado": "operativo", "descripcion": "Permite comunicacion encriptada entre Knothole y la Resistencia."},

    {"id": 5, "nombre": "Guante magnetico", "categoria": "Herramienta",
     "nivel_eficacia": 5.5, "estado": "dañado", "descripcion": "Atrae piezas metalicas para reparaciones rapidas de emergencia."},

    {"id": 6, "nombre": "Rastreador de Anillos Caos", "categoria": "Deteccion",
     "nivel_eficacia": 8.2, "estado": "en pruebas", "descripcion": "Localiza fuentes de energia caotica en Mobius."},
]


def inicio(request):
    contexto = {"inventos": inventos_rotor, "total": len(inventos_rotor)}
    return render(request, "inventos/inicio.html", contexto)


def detalle(request, id):
    invento = next((i for i in inventos_rotor if i["id"] == id), None)
    if invento is None:
        raise Http404("Invento no encontrado")
    return render(request, "inventos/detalle.html", {"invento": invento})