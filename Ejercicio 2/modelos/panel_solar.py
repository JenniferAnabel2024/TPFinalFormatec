from .dispositivo_ecologico import DispositivoEcologico


class PanelSolar(DispositivoEcologico):

    def __init__(self, producto_id, nombre, precio, stock,
                 potencia_watts, eficiencia_porcentaje, garantia_anios):
        super().__init__(producto_id, nombre, precio, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia_porcentaje = eficiencia_porcentaje
        self.garantia_anios = garantia_anios

    def ficha_tecnica(self):
        return (
            f"{super().ficha_tecnica()} | "
            f"Potencia: {self.potencia_watts} W | "
            f"Eficiencia: {self.eficiencia_porcentaje}% | "
            f"Garantía: {self.garantia_anios} años"
        )

    def to_dict(self):
        datos = super().to_dict()
        datos.update({
            "potencia_watts": self.potencia_watts,
            "eficiencia_porcentaje": self.eficiencia_porcentaje,
            "garantia_anios": self.garantia_anios,
        })
        return datos
