
from database_connection import get_database_connection

def drop_tables(connection):
    """Poistaa Highscore taulukon tietokannasta, jos se on olemassa.

    Args:
        connection: tietokantayhteys tiedostoon
    """
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Highscores;")
    connection.commit()

def create_tables(connection):
    """Lisää uuden Highsscores taulukon tietokantaan.

    Args:
        connection: tietokantayhteys tiedostoon
    """
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Highscores (board_size INTEGER, player_name TEXT, score INT);")
    connection.commit()

def initialize_database():
    """Luo uuden tyhjän tietokantatiedoston."""
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == '__main__':
    initialize_database()
