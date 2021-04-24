
from repositories.initialize_database import create_tables_if_not_exists
from repositories.database_connection import get_database_connection


class ScoreRepository:
    """Luokka, jonka avulla ylläpidetään parhaimpia pistetuloksia.

    Attributes:
        connection: yhteys tietokantaan
    """

    def __init__(self, connection=None):
        """Luokan konstruktori,
        joka avaa tietokanta yhteyden pisteiden tallettamiseen.

        Args:
            connection (valinnainen): yhteys tietokantaan,
            oletuksena tekee itse uuden, jos tarvittava
        """

        create_tables_if_not_exists()
        if connection is None:
            self.connection = get_database_connection()
        else:
            # testaukeen tarkoitettu
            self.connection = connection

    def get_top5(self, board_size: int):
        """Hakee top 5 pelaajaa ja tulosta tietokannasta

        Args:
            board_size (int): pelialustan leveys ja pituus

        Returns:
            list: lista top5 pelaajista
        """

        cursor = self.connection.cursor()
        sql = """SELECT player_name, score
                    FROM Highscores
                    WHERE board_size=?
                    ORDER BY score DESC
                    LIMIT 5;"""
        result = cursor.execute(sql, (board_size, )).fetchall()

        length = len(result)
        for i in range(length):
            result[i] = tuple(result[i])

        cursor.close()
        return result

    def add_new_highscore(self, player_name: str, score: int, board_size=4):
        """Lisää pelaajan ja tuloksen tietokantaan

        Args:
            player_name (str): Pelaajan nimimerkki
            score (int): tulos
            board_size (int, valinnainen): pelialustan koko. Oletus: 4.
        """

        cursor = self.connection.cursor()
        sql = "INSERT INTO Highscores VALUES (?, ?, ?);"
        cursor.execute(sql, (board_size, player_name, score))
        self.connection.commit()
        cursor.close()

    def check_if_highscore(self, score: int, board_size: int):
        """Tarkistaa, onko tulos parempi, kuin viidennen parhaan pelajan tulos.

        Args:
            score (int): tulos

        Returns:
            boolean: True, jos on parempi
        """
        if score == 0:
            return False

        top5 = self.get_top5(board_size)
        if len(top5) == 5:
            last_player = top5[len(top5)-1]
            if last_player[1] < score:
                return True
        else:
            return True
        return False
    
    def get_highscore(self, grid_size):
        top5 = self.get_top5(grid_size)
        if len(top5) > 0:
            return top5[0][1]
        else:
            return 0
