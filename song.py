
# Importar los módulos necesarios para la ejecución del programa.


class Song():
    """Constructor of the class.

        The constructor of the class Song is used to create a new song.

        Syntax
        ------
          song = Song(id, name, artist, duration, release_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the song.
          name : str
            The name of the song.
          artist : str
            The artist of the song.
          duration : int
            The duration of the song in seconds.
          release_date : date
            The release date of the song.
          genres : list
            The genres of the song.

        Returns
        -------
          The new song.

        Example
        -------
          song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])
        """
    #Realizar la implementación de la clase Song.

'''
Pseudocódigo

Clase Song:
    Hipótesis:
        Se espera que la clase Song permita representar y manipular canciones, incluyendo su información básica y los géneros asociados.

    Precondición:
        La precondición para la creación de una instancia de la clase Song es que los datos proporcionados para nombre, artista, duración, fecha de lanzamiento y géneros deben ser válidos y coherentes.

    Entrada:
        - Nombre: Cadena que representa el nombre de la canción.
        - Artista: Cadena que representa el nombre del artista.
        - Duración: Entero que indica la duración en segundos (debe ser mayor a 10 segundos).
        - Fecha de Lanzamiento: Fecha en la que la canción fue lanzada (no puede ser una fecha futura).
        - Géneros: Conjunto de instancias de la clase Genre que representan los géneros musicales asociados a la canción.

    Salida:
        Ninguna salida directa durante la creación de la instancia de la clase Song.

    Efecto:
        La creación de una instancia de la clase Song implica la validación de los datos proporcionados y la creación de un objeto que representa una canción con la información dada. Se garantiza que la canción creada sea coherente y válida según las restricciones establecidas.

    Métodos:
        - validate_song: Método interno para validar los atributos de la canción, como la duración, la fecha de lanzamiento y los géneros.
        - add_genre: Método para añadir un género a la canción.
        - __eq__: Método para comparar si dos canciones son iguales basadas en el nombre y el artista.
        - __str__: Método para obtener una representación en cadena de la canción.

    Ejemplo de uso:
        # Crear una instancia de Song con datos válidos
        song = Song("Californication", "Red Hot Chili Peppers", 300, datetime(1999, 6, 8), {Genre.ROCK})

        # Imprimir la representación en cadena de la canción
        print(song)

        # Añadir un género adicional a la canción
        song.add_genre(Genre.POP)

        # Imprimir los géneros de la canción
        print(song.genres)

        Se han importado los módulos genre y datetime
from datetime import datetime
from genre import Genre  Importamos la clase Genre del módulo genre

'''
from datetime import datetime
from genre import Genre  # Importamos la clase Genre del módulo genre

class Song:
    def __init__(self, name, artist, duration, release_date, genres, main):
        if not genres:
            genres = set()
        self.name = name
        self.artist = artist
        self.duration = duration
        self.release_date = release_date
        self.genres = genres
        self.validate_song()

    def validate_song(self):
        if self.duration <= 10:
            raise ValueError("La duración debe ser mayor de 10 segundos.")
        if self.release_date > datetime.now():
            raise ValueError("La fecha de lanzamiento no puede ser futura.")
        if not all(isinstance(genre, Genre) for genre in self.genres):
            raise ValueError("Todos los géneros deben ser instancias de Genre.")

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            self.genres.add(genre)
        else:
            raise ValueError("El género debe ser una instancia de Genre.")

    def __eq__(self, other):
        if not isinstance(other, Song):
            return NotImplemented
        return self.name == other.name and self.artist == other.artist

    def __str__(self):
        return f"{self.artist} tocando {self.name} durante {self.duration} segundos."


    def main():
      """Function main of the module.

    The function main of this module is used to test the Class Song.

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
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))


    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
    


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()