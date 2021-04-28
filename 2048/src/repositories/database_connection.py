
import os
import sqlite3

dirname = os.path.dirname(__file__)


def get_database_connection():
    """Palauttaa tietokanta yhteyden paikalliseen tiedostoon.

    Returns:
        connection: yhteys tietokantatiedostoon.
    """
    connection = sqlite3.connect(os.path.join(
        dirname, "../..", "data", "database.sqlite"))
    connection.row_factory = sqlite3.Row
    return connection


def get_fake_database_connection():
    """Palauttaa tekaistun tietokanta yhteyden paikalliseen tiedostoon.
    Tätä funktiota käytetään vain testauksessa.

    Returns:
        connection: tekaistu yhteys tietokantatiedostoon.
    """
    connection = sqlite3.connect(os.path.join(
        dirname, "../..", "data", "fake_database.sqlite"))
    connection.row_factory = sqlite3.Row
    return connection
