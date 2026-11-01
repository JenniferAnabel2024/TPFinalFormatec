"""Bloque de prueba del Ejercicio 2.

Verifica la captura controlada de StockInvalidoError y finaliza con
la exportación de los productos válidos al archivo JSON.
"""

import modelos, persistencia, excepciones

# INSTANCIAS
dispositivo_1 = modelos.DispositivoEcologico(
    "ECO-001", "Bomba de agua solar", 250000, stock=10)
dispositivo_2 = modelos.DispositivoEcologico(
    "ECO-002", "Termotanque solar", 480000, stock=3)
panel_1 = modelos.PanelSolar(
    "ECO-003", "Panel Solar Mono 450W", 890000, 5, 450, 21.5, 10)
panel_2 = modelos.PanelSolar(
    "ECO-004", "Panel Solar Poly 330W", 520000, 8, 330, 17.8, 5)

# FICHAS TÉCNICAS (polimorfismo: cada clase emite su propia ficha)
print("=== FICHAS TÉCNICAS ===")
print(dispositivo_1)
print(dispositivo_2)
print(panel_1)
print(panel_2)

# CAPTURA CONTROLADA DE StockInvalidoError
print("\n=== VALIDACIÓN DE STOCK ===")
try:
    dispositivo_1.stock = -4  # asignación errónea por el setter
except excepciones.StockInvalidoError as e:
    print("Excepción capturada:", e)

try:
    panel_malo = modelos.PanelSolar(  # stock negativo en el constructor
        "ECO-005", "Panel defectuoso", 100000, -1, 100, 10, 1)
except excepciones.StockInvalidoError as e:
    print("Excepción capturada:", e)

# EXPORTACIÓN DE LOS PRODUCTOS VÁLIDOS
persistencia.GestorInventario.guardar_catalogo_json(
    [dispositivo_1, dispositivo_2, panel_1, panel_2],
    "catalogo_ecotech.json",
)
