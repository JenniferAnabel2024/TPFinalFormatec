FACTOR_EMISION_POR_DEFECTO = 0.4


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError(
            f"El consumo no puede ser negativo: {consumo_kwh} kWh"
        )
    return consumo_kwh * factor_emision
