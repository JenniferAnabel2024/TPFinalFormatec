from excepciones import StockInvalidoError


class DispositivoEcologico:

    def __init__(self, producto_id, nombre, precio, stock=0):
        self.producto_id = producto_id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(
                f"Stock inválido ({valor}) para '{self.nombre}': "
                "no puede ser negativo."
            )
        self.__stock = valor

    def ficha_tecnica(self):
        return (
            f"[{self.producto_id}] {self.nombre} | "
            f"${self.precio:,.0f} | Stock: {self.stock}"
        )

    def __str__(self):
        return self.ficha_tecnica()

    def to_dict(self):
        return {
            "tipo": type(self).__name__,
            "producto_id": self.producto_id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }
