"""Ejercicio 1 - Sanitización y Análisis Estadístico de Sensores.

Funciones para normalizar registros crudos de sensores de EcoTech
Solutions y generar un resumen estadístico de temperaturas.
"""

import re

UBICACION_POR_DEFECTO = "Sin ubicación"


def limpiar_registro_sensor(registro_raw):
    """Punto A: normaliza un registro crudo de sensor.

    - sensor_id: sin espacios al inicio ni al final.
    - temperatura: float sin sufijo de unidad ("24.5C" -> 24.5).
    - ubicacion: valor por defecto si llega vacía o None.
    """
    sensor_id = str(registro_raw.get("sensor_id", "")).strip()

    temperatura_raw = registro_raw.get("temperatura", 0)
    if isinstance(temperatura_raw, (int, float)):
        temperatura = float(temperatura_raw)
    else:
        # Elimina la unidad ("24.5C", "31 c", "°C 22") y castea a float
        coincidencia = re.search(r"-?\d+(?:\.\d+)?", str(temperatura_raw))
        temperatura = float(coincidencia.group()) if coincidencia else 0.0

    ubicacion_raw = registro_raw.get("ubicacion")
    if ubicacion_raw is None or not str(ubicacion_raw).strip():
        ubicacion = UBICACION_POR_DEFECTO
    else:
        ubicacion = str(ubicacion_raw).strip()

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Punto B: retorna (lista_sensores_alerta, promedio_temperatura).

    - lista_sensores_alerta: IDs cuya temperatura supera el umbral.
    - promedio_temperatura: promedio térmico global de la planta
      (0.0 si la lista está vacía).
    """
    lista_sensores_alerta = [
        sensor["sensor_id"]
        for sensor in lista_sensores_limpios
        if sensor["temperatura"] > umbral_temperatura
    ]

    if lista_sensores_limpios:
        promedio_temperatura = (
            sum(s["temperatura"] for s in lista_sensores_limpios)
            / len(lista_sensores_limpios)
        )
    else:
        promedio_temperatura = 0.0

    return lista_sensores_alerta, promedio_temperatura
