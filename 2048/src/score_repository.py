
from initialize_database import create_tables_if_not_exists
from database_connection import get_database_connection


class ScoreRepository:
    """Luokka, jonka avulla ylläpidetään parhaimpia pistetuloksia.
    """

    def __init__(self):
        """Luokan konstruktori, joka avaa tietokanta yhteyden pisteiden tallettamiseen.

        Args:
            connection: yhteys tietokantaan
        """
        create_tables_if_not_exists()
        self.connection = get_database_connection()
    
    def get_top_5(self):
        pass
    

