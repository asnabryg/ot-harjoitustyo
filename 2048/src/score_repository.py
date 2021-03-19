
import os
from initialize_database import create_tables_if_not_exists
from database_connection import get_database_connection


class ScoreRepository:
    """Luokka, jonka avulla ylläpidetään parhaimpia pistetuloksia.
    """

    def __init__(self):
        create_tables_if_not_exists()
        self.connection = get_database_connection()

