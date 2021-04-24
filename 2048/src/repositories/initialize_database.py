
# from database_connection import get_database_connection, get_fake_database_connection
try:
    import repositories.database_connection as db
except ModuleNotFoundError:
    import database_connection as db


def drop_tables(connection):
    """Poistaa Highscore taulukon tietokannasta, jos se on olemassa.

    Args:
        connection: tietokantayhteys tiedostoon
    """
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Highscores;")
    connection.commit()
    cursor.close()


def create_tables(connection):
    """Lisää uuden Highscores taulukon tietokantaan.

    Args:
        connection: tietokantayhteys tiedostoon
    """
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE Highscores (board_size INTEGER, player_name TEXT, score INT);")
    connection.commit()
    cursor.close()


def initialize_database():
    """Luo uuden tyhjän tietokantatiedoston."""
    connection = db.get_database_connection()
    drop_tables(connection)
    create_tables(connection)


def initialize_fake_database():
    """Luo uuden tyhjän tietokantatiedoston. Tämä metodi tarkoitettu testaukseen"""
    connection = db.get_fake_database_connection()
    drop_tables(connection)
    create_tables(connection)


def create_tables_if_not_exists():
    """Luo taulukot tietokantaan, jos niitö ei vielä olemassa. Ei poista taulukoita, jos olemassa.
    """
    connection = db.get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Highscores (board_size INTEGER, player_name TEXT, score INT);")
    connection.commit()
    cursor.close()


if __name__ == '__main__':
    initialize_database()
