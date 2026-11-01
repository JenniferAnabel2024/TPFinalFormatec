"""Punto B: procesamiento de métricas de consumo por planta."""

from .emisiones import calcular_emisiones_carbono


def obtener_metricas_consumo(registros):
    """Procesa el historial de consumos por planta industrial.

    Cada registro es un dict {"planta": str, "consumo_kwh": float}.
    Retorna el diccionario de contexto para la vista:

    - total_emisiones: suma global de emisiones (kg CO2).
    - planta_mayor_consumo: nombre de la planta con mayor consumo.
    - detalle: emisiones calculadas por planta.
    """
    detalle = []
    total_emisiones = 0.0
    planta_mayor_consumo = None
    mayor_consumo = float("-inf")

    for registro in registros:
        consumo = registro["consumo_kwh"]
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        detalle.append({
            "planta": registro["planta"],
            "consumo_kwh": consumo,
            "emisiones": emisiones,
        })
        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor_consumo = registro["planta"]

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "detalle": detalle,
    }
