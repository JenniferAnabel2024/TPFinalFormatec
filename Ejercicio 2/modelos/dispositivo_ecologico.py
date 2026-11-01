"""Punto A: clase base del dominio del catálogo."""

from excepciones import StockInvalidoError


class DispositivoEcologico:
    """Clase base del catálogo.

    El stock se encapsula de forma explícita: toda asignación pasa por
    el setter, que impide valores negativos lanzando StockInvalidoError.
    """

    def __init__(self, producto_id, nombre, precio, stock=0):
        self.producto_id = producto_id  # identificador del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock  # pasa por el setter validador

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
        """Ficha comercial base; las subclases la personalizan."""
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
