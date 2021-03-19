
from sqlite3.dbapi2 import Cursor
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

def create_tables_if_not_exists():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Highscores (board_size INTEGER, player_name TEXT, score INT);")
    connection.commit()


if __name__ == '__main__':
    initialize_database()