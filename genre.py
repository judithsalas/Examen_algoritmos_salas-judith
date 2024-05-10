

# Source packages.

class GENRE():
    """
    Class GENRE.

    This class is used to store the genre of a song.

    Syntax
    ------
        genre = GENRE()

    Parameters
    ----------
        Null .
    
    Returns
    -------
        The new genre.
    
    Example
    -------
        genre = GENRE()
    """
from enum import Enum

class Genre(Enum):
    ROCK = 1
    POP = 2
    EDM = 3
    COUNTRY = 4


#Test
genre = Genre.ROCK
print(genre)  # Output: Genre.ROCK
print(genre.value)  # Output: 1


'''
Clase Genre:
    Hipótesis:
        Se espera que la clase Genre permita representar diferentes géneros musicales.

    Precondición:
        Ninguna.

    Entrada:
        Ninguna.

    Salida:
        Ninguna.

    Efecto:
        La clase Genre define los géneros musicales disponibles como miembros de la clase.

    Métodos:
        Ninguno.

    Constantes de clase:
        ROCK
        POP
        EDM
        COUNTRY

'''

def main():
    """Function main of the module.

    The function main of this module is used to test the Class GENRE.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Check Class GENRE - Name.")
    print("=================================================================.")

    if isinstance(GENRE.ROCK, GENRE):
        print("Test PASS. The enum for ROCK has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.POP, GENRE):
        print("Test PASS. The enum for POP has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.EDM, GENRE):
        print("Test PASS. The enum for EDM has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.COUNTRY, GENRE):
        print("Test PASS. The enum for COUNTRY has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
