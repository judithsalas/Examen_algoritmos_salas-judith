# Judith M.ª Salas García

## Explicación Factorial

Este código implementa el algoritmo del factorial de manera recursiva, utilizando un enfoque donde se calcula el factorial de un número multiplicándolo por el factorial del número anterior, y se maneja el caso base cuando el número es igual a 0.

El algoritmo del factorial es un procedimiento matemático que se utiliza para calcular el producto de todos los enteros positivos desde 1 hasta un número entero no negativo dado n, denotado como n!. Aquí está el proceso del algoritmo:

Definición del Factorial: 
El factorial de un número entero no negativo 𝑛n, denotado como n!, se define como el producto de todos los enteros positivos menores o iguales a n.

Caso Base: Si n es igual a 0, entonces el factorial de n es igual a 1 por definición. Esto es una regla base fundamental del cálculo de factoriales.

Caso Recursivo: Si n es mayor que 0, entonces el factorial de n se calcula multiplicando n por el factorial de n−1. Este proceso se repite recursivamente hasta que se alcance el caso base.
Por ejemplo, si queremos calcular 5!:

n* (n-1)* (n-2)* ... *(n-n+1)*= n * (n-1)! = n *(n-1) * (n-2)! = ...
Iniciamos con 5, n=5:
Multiplicamos 5 por el factorial de 4 (n-1), que es 4!.
Para calcular 4!, multiplicamos 4 por el factorial de 3 (n-2), que es 3! Continuamos este proceso hasta llegar a 0!, que es 1 por definición.
Entonces, 5!=5×4×3×2×1=120.
Este algoritmo es comúnmente implementado de manera recursiva en lenguajes de programación como Python, donde se puede definir una función que llame a sí misma para calcular el factorial de un número dado.



## Bubble Sort

El método Bubble Sort es un algoritmo de ordenamiento simple y fundamental que funciona iterando sobre la lista que se desea ordenar, comparando elementos adyacentes y realizando intercambios si están en el orden incorrecto. Este proceso se repite hasta que la lista esté completamente ordenada.

### Funcionamiento:
Compara cada par de elementos adyacentes de la lista.
Si los elementos están en el orden incorrecto, los intercambia.
Repite este proceso hasta que no se realicen intercambios en un pasaje completo a través de la lista.
Casos de Uso:
El Bubble Sort es adecuado para ordenar listas pequeñas o cuando la eficiencia no es una preocupación principal. Sin embargo, es ineficiente en comparación con otros algoritmos de ordenamiento, especialmente para listas grandes, debido a su complejidad cuadrática. Por lo tanto, se recomienda su uso solo para listas pequeñas o para fines educativos y de aprendizaje.

### Ejemplo Conceptual:
Consideremos la lista de números [34, 7, 23, 32, 5]. Aplicaremos el algoritmo Bubble Sort para ordenar esta lista:

Comenzamos con la lista [34, 7, 23, 32, 5].
Comparamos 34 y 7, y como 7 es menor que 34, los intercambiamos. La lista se convierte en [7, 34, 23, 32, 5].
Continuamos comparando e intercambiando por pares en orden  los números que son menores posicionandolos a la izquierda, el 34 es mayor que el 23 por lo que se intercambian [7, 23, 34, 32, 5], el 24 por el 32, [7, 23, 32, 34, 5], y el 34 por el 5, quedandonos el la primera permutación la siguiente lista [7, 23, 32, 5, 34].

A continuación repetiremos el proceso en una segunda permutación por pares [7, 23, 32, 5, 34], [7, 23, 5, 32, 34],

Volveremos a recorrer la lista [7, 5, 23, 32, 34] y una última vez, obteniendo una lista ordenada de forma creciente [5, 7, 23, 32, 34].
