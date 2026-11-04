from django.shortcuts import render

from servicios.metricas import obtener_metricas_consumo


REGISTROS_CONSUMO = [
    {"planta": "Planta Norte", "consumo_kwh": 12500},
    {"planta": "Planta Sur", "consumo_kwh": 9800},
    {"planta": "Planta Oriente", "consumo_kwh": 15200},
    {"planta": "Planta Occidente", "consumo_kwh": 7300},
]


def vista_panel_sustentabilidad(request):
    contexto = obtener_metricas_consumo(REGISTROS_CONSUMO)
    return render(request, "sustentabilidad/panel.html", contexto)
