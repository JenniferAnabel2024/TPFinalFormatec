"""Bloque de ejecución: flujo completo limpieza -> resumen -> reporte."""

from servicios import limpiar_registro_sensor, generar_resumen_sensores

UMBRAL_TEMPERATURA = 28.0

# Registros crudos tal cual llegan en el JSON de los microcontroladores
registros_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": "SENSOR-002", "temperatura": "31.2 c", "ubicacion": "  Planta Sur "},
    {"sensor_id": "  SENSOR-003 ", "temperatura": 27.8, "ubicacion": ""},
    {"sensor_id": "SENSOR-004", "temperatura": "35C", "ubicacion": None},
    {"sensor_id": " SENSOR-005", "temperatura": "22.9C", "ubicacion": "Bodega Central"},
]


def main():
    # Punto A: limpieza de registros crudos
    sensores_limpios = [limpiar_registro_sensor(r) for r in registros_crudos]

    print("=== REGISTROS NORMALIZADOS ===")
    for s in sensores_limpios:
        print(f"  {s['sensor_id']} | {s['temperatura']} °C | {s['ubicacion']}")

    # Punto B: resumen estadístico
    alertas, promedio = generar_resumen_sensores(sensores_limpios, UMBRAL_TEMPERATURA)

    print("\n=== REPORTE FINAL ===")
    print(f"Umbral de alerta:     {UMBRAL_TEMPERATURA} °C")
    print(f"Temperatura promedio: {promedio:.2f} °C")
    print(f"Sensores en alerta ({len(alertas)}):")
    for sensor_id in alertas:
        print(f"  - {sensor_id}")


if __name__ == "__main__":
    main()
