"""Punto A: auditoría del algoritmo de emisiones (unittest)."""

import unittest

from servicios.emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):
    """Casos de prueba para calcular_emisiones_carbono."""

    def test_valor_nominal(self):
        # 100 kWh * 0.4 (factor por defecto) = 40.0 kg CO2
        self.assertEqual(calcular_emisiones_carbono(100), 40.0)

    def test_factor_emision_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(250, 0.25), 62.5)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo_lanza_valueerror(self):
        # Consumo fuera de rango: debe elevarse ValueError
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)

    def test_mensaje_de_la_excepcion(self):
        with self.assertRaises(ValueError) as ctx:
            calcular_emisiones_carbono(-50)
        self.assertIn("negativo", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()
