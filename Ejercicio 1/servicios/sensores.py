import re

UBICACION_POR_DEFECTO = "Sin ubicación"


def limpiar_registro_sensor(registro_raw):
    sensor_id = str(registro_raw.get("sensor_id", "")).strip()

    temperatura_raw = registro_raw.get("temperatura")
    if isinstance(temperatura_raw, (int, float)):
        temperatura = float(temperatura_raw)
    else:
        coincidencia = re.search(r"-?\d+(?:\.\d+)?", str(temperatura_raw))
        if not coincidencia:
            raise ValueError(
                f"La temperatura ingresada ({temperatura_raw}) "
                "no contiene valor numérico"
            )
        temperatura = float(coincidencia.group())

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
