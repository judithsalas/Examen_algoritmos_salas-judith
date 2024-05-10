#Recursividad para calcular el factorial de un número.

''' def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    #Código a realizar.
'''
def factorial(n):
    """
    Calcula el factorial de un número entero no negativo de manera recursiva.

    Parámetros:
        n (int): El número entero del cual se calculará el factorial.

    Retorna:
        int: El factorial del número dado.

    Caso Base:
        Si n es 0, retorna 1 por definición.

    Paso Recursivo:
        Si n > 0, retorna n * factorial(n - 1).
    """
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Paso recursivo: factorial de n es n * factorial(n - 1)
    else:
        return n * factorial(n - 1)

# Ejemplo de uso adicional
num = 5
print(f"El factorial de {num} es: {factorial(num)}")


def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    

'''
Pseudocódigo

Función factorial:
    Hipótesis:
        Se espera que la función factorial calcule el factorial de un número entero no negativo de manera recursiva.

    Precondición:
        El parámetro de entrada `n` debe ser un número entero no negativo.

    Entrada:
        n (int): El número entero del cual se calculará el factorial.

    Salida:
        int: El factorial del número dado.

    Efecto:
        La función factorial calcula el factorial del número dado mediante un enfoque recursivo.

    Caso Base:
        Si n es 0, retorna 1 por definición.

    Paso Recursivo:
        Si n > 0, la función retorna n * factorial(n - 1).


 Función factorial(n):
        Si n es igual a 0, retorna 1. [Caso Base]
        Sino, retorna n * factorial(n - 1). [Paso Recursivo]

'''