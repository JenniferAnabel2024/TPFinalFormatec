"""Excepciones de negocio del catálogo EcoTech Solutions."""


class StockInvalidoError(Exception):
    """Se lanza cuando se intenta asignar un stock negativo a un producto."""
