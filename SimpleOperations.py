import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
# twenty_percent_discount 
# vat_tax

# Usar las funciones preconfiguradas.

from functools import partial

class SimpleOperations:
    def apply_discount(self, price, discount):
        """
        Calcula el precio final después de aplicar un descuento.

        Parámetros:
            price (float): El precio original.
            discount (float): El porcentaje de descuento (decimal).

        Retorna:
            float: El precio final después de aplicar el descuento.
        """
        return price * (1 - discount)

    def calculate_tax(self, price, tax_rate):
        """
        Calcula el precio final después de aplicar un impuesto.

        Parámetros:
            price (float): El precio original.
            tax_rate (float): El porcentaje de impuesto (decimal).

        Retorna:
            float: El precio final después de aplicar el impuesto.
        """
        return price * (1 + tax_rate)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la clase SimpleOperations
    simple_ops = SimpleOperations()

    # Definir descuentos y tasas de impuestos preconfigurados
    discount_10_percent = partial(simple_ops.apply_discount, discount=0.10)
    tax_21_percent = partial(simple_ops.calculate_tax, tax_rate=0.21)

    # Calcular precios finales con descuentos y tasas de impuestos preconfigurados
    final_price_discounted = discount_10_percent(100)
    final_price_with_tax = tax_21_percent(100)

    # Imprimir resultados
    print("Precio final después de aplicar un descuento del 10%:", final_price_discounted)
    print("Precio final después de agregar un impuesto del 21%:", final_price_with_tax)
