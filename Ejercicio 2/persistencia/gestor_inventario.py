import json


class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos = [dispositivo.to_dict() for dispositivo in lista_dispositivos]
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        print(f"Catálogo exportado a '{ruta_archivo}' "
              f"({len(datos)} productos).")
