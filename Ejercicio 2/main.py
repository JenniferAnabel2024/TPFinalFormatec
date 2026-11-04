import modelos, persistencia, excepciones


dispositivo_1 = modelos.DispositivoEcologico(
    "ECO-001", "Bomba de agua solar", 250000, stock=10)
dispositivo_2 = modelos.DispositivoEcologico(
    "ECO-002", "Termotanque solar", 480000, stock=3)
panel_1 = modelos.PanelSolar(
    "ECO-003", "Panel Solar Mono 450W", 890000, 5, 450, 21.5, 10)
panel_2 = modelos.PanelSolar(
    "ECO-004", "Panel Solar Poly 330W", 520000, 8, 330, 17.8, 5)


print("=== FICHAS TÉCNICAS ===")
print(dispositivo_1)
print(dispositivo_2)
print(panel_1)
print(panel_2)


print("\n=== VALIDACIÓN DE STOCK ===")
try:
    dispositivo_1.stock = -4
except excepciones.StockInvalidoError as e:
    print("Excepción capturada:", e)

try:
    panel_malo = modelos.PanelSolar(
        "ECO-005", "Panel defectuoso", 100000, -1, 100, 10, 1)
except excepciones.StockInvalidoError as e:
    print("Excepción capturada:", e)


persistencia.GestorInventario.guardar_catalogo_json(
    [dispositivo_1, dispositivo_2, panel_1, panel_2],
    "catalogo_ecotech.json",
)
