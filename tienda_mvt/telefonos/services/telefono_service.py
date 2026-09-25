import json

from django.conf import settings

from ..models import Telefono

RUTA_JSON = settings.BASE_DIR / "telefonos" / "data" / "telefonos.json"

def get_telefonos():
    if not RUTA_JSON.exists():
        print(f"No se encontro el archivo de datos: {RUTA_JSON}")
        return []
    with open(RUTA_JSON, encoding = "utf-8") as archivo:
        return json.load(archivo)

def load_telefonos():
    if Telefono.objects.count():
        return f"Ya existen {Telefono.objects.count()} telefonos"

    telefonos = get_telefonos()
    for telefono in telefonos:
        Telefono.objects.create(
            nombre = telefono["nombre"],
            marca = telefono["marca"],
            descripcion = telefono["descripcion"],
            imagen = telefono["imagen"],
            precio = telefono["precio"],
            almacenamiento = telefono["almacenamiento"],
            ram = telefono["ram"],
            color = telefono.get("color", ""),
            stock = telefono.get("stock", 0),
        )
    return f"Se cargaron {Telefono.objects.count()} telefonos"
