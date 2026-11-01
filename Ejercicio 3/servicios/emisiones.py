"""Punto A: algoritmo de cálculo de huella de carbono industrial."""

FACTOR_EMISION_POR_DEFECTO = 0.4  # kg CO2 por kWh


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """Calcula las emisiones de CO2 (kg) de un consumo eléctrico.

    Eleva ValueError si el consumo es negativo (fuera de rango).
    """
    if consumo_kwh < 0:
        raise ValueError(
            f"El consumo no puede ser negativo: {consumo_kwh} kWh"
        )
    return consumo_kwh * factor_emision
