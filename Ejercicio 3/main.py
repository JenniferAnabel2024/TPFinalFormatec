"""Bloque de prueba del Ejercicio 3.

Simula la tubería de datos: registros de consumo -> obtener_metricas_consumo
-> contexto que vista_panel_sustentabilidad entrega a panel.html.
"""

from servicios.metricas import obtener_metricas_consumo

# Historial de consumos por planta (en producción vendría de la ETL/BD)
registros = [
    {"planta": "Planta Norte", "consumo_kwh": 12500},
    {"planta": "Planta Sur", "consumo_kwh": 9800},
    {"planta": "Planta Oriente", "consumo_kwh": 15200},
    {"planta": "Planta Occidente", "consumo_kwh": 7300},
]

contexto = obtener_metricas_consumo(registros)

print("=== MÉTRICAS DE CONSUMO ===")
for fila in contexto["detalle"]:
    print(f"  {fila['planta']}: {fila['consumo_kwh']} kWh "
          f"-> {fila['emisiones']:.1f} kg CO2")

print(f"\nEmisiones totales:      {contexto['total_emisiones']:.1f} kg CO2")
print(f"Planta de mayor consumo: {contexto['planta_mayor_consumo']}")

print("\nEste diccionario es el que vista_panel_sustentabilidad()")
print("entrega como contexto a sustentabilidad/panel.html")
