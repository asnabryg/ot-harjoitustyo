
import random


class Game2048:
    """Luokka, jossa on pelin logiikka ja pelialusta.
    """

    def __init__(self, size, board=None, r_seed=None):
        """Luokan konstruktori, joka luo uuden pelialusta.

        Args:
            size (int): pelialustan koko (leveys ja pituus)
            board (list[list], valinnainen): Aloitus pelialusta. Oletus: None,
            r_seed (int, valinnainen): Käytetään pytesteihin. Oletus: None,
        """
        self.__size = size
        self.__score = 0
        self._game_over = False
        if board is None:
            self.__board = self.new_board(size)
        else:
            self.__board = board

        if r_seed is not None:
            # for pytests only
            random.seed(r_seed)

    def is_gameover(self):
        """Palauttaa booleanin, onko peli päättynyt. self.__gameover muuttuja muutetaan metodissa
        self._check_if_gameover, joten tämä metodi palauttaa vain totuusarvon,
        mikä on laskettu aikaisemmin,
        eikä laske tai muuta sitä itse.

        Returns:
            boolean: True, jos peli on päättynyt
        """
        return self._game_over

    def get_size(self):
        """Palauttaa pelialueen koon (leveys ja pituus)

        Returns:
            int: Pelialueen koko
        """
        return self.__size

    def get_board(self):
        """Palauttaa pelialustan 2d matriisina

        Returns:
            list[list]: pelialusta
        """
        return self.__board

    def get_score(self):
        """Palauttaa sen hetkisen pelin pistetilanteen

        Returns:
            int: pisteet
        """
        return self.__score

    def new_board(self, size):
        """Luo uuden tyhjän pelialustan 2d matriisina

        Args:
            size (int): Pelialstan leveys ja pituus

        Returns:
            list[list]: pelialusta
        """
        board = [0] * size
        for i in range(size):
            board[i] = [0] * size
        return board

    def get_random_empty_place(self):
        """Hakee jokaisen 0 kohdan pelialustasta ja valitsee yhden randomisti

        Returns:
            tuple: random 0 kohdan koordinaatti pelialustassa,
            jos löytyi vähintään yksi koordinaatti, muuten None
        """
        empty_places = []
        for board_y in range(self.__size):
            for board_x in range(self.__size):
                if self.__board[board_y][board_x] == 0:
                    empty_places.append((board_y, board_x))
        if len(empty_places) == 0:
            return None
        return random.choice(empty_places)

    def add_new_tile(self):
        """Lisää uuden laatan laudalle. Laatan numero on joko 2 tai 4.

        Returns:
            boolean: True, jos onnistui, muuten False
        """

        yx_coordinate = self.get_random_empty_place()
        if yx_coordinate is None:
            # Gameover
            return False
        rnd = random.randint(0, 2)
        if rnd == 2:
            rnd = 4
        else:
            rnd = 2
        self.__board[yx_coordinate[0]][yx_coordinate[1]] = rnd
        return True

    def _check_if_gameover(self):
        """Tarkistaa onko peli tilanteessa, missä pelaaja ei enää pysty liikuttamaan
        laattoja ja pelissä ei ole tyhjiä ruutuja.

        Returns:
            boolean: True, jos peli päättynyt
        """

        if self.get_random_empty_place() is None:
            for board_y in range(self.__size):
                for board_x in range(self.__size):
                    if board_x+1 < self.__size:
                        if self.__board[board_y][board_x] == self.__board[board_y][board_x+1]:
                            return False
                    if board_x+1 < self.__size:
                        if self.__board[board_x][board_y] == self.__board[board_x+1][board_y]:
                            return False
        else:
            return False
        return True

    def _checks_can_you_move(self, board_copy):
        """Metodi vertailee edellistä lautaa ja simoiloitua liikutettua lautaa,
        jos ne ovat samanlaiset, niin se tarkoittaa,
        että pelaaja ei voi liikuttaa pelissä tiettyyn suuntaan.
        Simuloitu liikutettu lauta ei päivity pelissä tai näy siellä mitenkään.
        Metodi palauttaa True, jos pelaaja voi liikuttaa laattoja tiettyyn suuntaan.

        Args:
            board_copy (2d matrix): Kopio laudasta, ennen kuin sitä on simuloidusti liikutettu.

        Returns:
            boolean: True, jos pelaaja voi liikuttaa laattoja tiettyyn suntaan.
        """

        similar = True
        for i in range(self.__size):
            if self.__board[i] != board_copy[i]:
                similar = False
                break
        return not similar

    def choose_board(self, copy=False):
        board = []
        board_copy = []
        if copy:
            for row in self.__board.copy():
                board_copy.append(row.copy())
            board = board_copy
        else:
            board = self.__board
        return board, board_copy

    def move(self, direction, check_if_can_move=False):
        """Jos parametri check_if_can_move on True, niin tämän metodin suoritus simuloidaan,
        eikä päivitetä peliruudulle.
        Metodi liikuttaa ensin peli laattoja annettuun suuntaan kokonaan,
        sen jälkeen yhdistää vierekkäiset saman numeroiset laatat.
        Lopuksi lisää uuden laatan pelialustaan, jos metodin parametri oli False.

        Args:
            direction (str): Suunta mihin päin li'utetaan laattoja.
                            ("up", "down", "right" or "left")
            check_if_can_move (bool, valinnainen): True, jos halutaan tarkistaa,
                                                    voiko pelaaja liikuttaa laattoja.

        Returns:
            bool: Palauttaa totuusarvon, vain jos metodin parametri on True. Palauttaa,
                        voidaanko liikuttaa lattoja.
        """
        board, board_copy = self.choose_board(check_if_can_move)

        for board_y in range(self.__size):
            row = []
            for board_x in range(self.__size):
                if direction in ("right", "left"):
                    if board[board_y][board_x] != 0:
                        row.append(board[board_y][board_x])
                else:
                    if board[board_x][board_y] != 0:
                        row.append(board[board_x][board_y])
            new_row = []
            if len(row) >= 2:
                board_x, addition = (0, 1) if direction in (
                    "left", "up") else (len(row)-1, -1)

                while (direction in ("left", "up") and board_x <= len(row)-1) or\
                        (direction in ("right", "down") and board_x >= 0):

                    if (direction in ("left", "up") and board_x+addition < len(row)) or\
                            (direction in ("right", "down") and board_x+addition >= 0):

                        if row[board_x] == row[board_x+addition]:
                            value = row[board_x] + row[board_x+addition]
                            new_row.append(value)
                            self.__score += value
                            board_x += addition
                        else:
                            new_row.append(row[board_x])
                    else:
                        new_row.append(row[board_x])
                    board_x += addition
            else:
                new_row = row

            for _ in range(self.__size - len(new_row)):
                new_row.append(0)
            if direction in ("right", "down"):
                new_row.reverse()
            if direction in ("right", "left"):
                board[board_y] = new_row
            else:
                for board_x in range(self.__size):
                    board[board_x][board_y] = new_row[board_x]

        if not check_if_can_move:
            if not self.add_new_tile() and self._check_if_gameover():
                self._game_over = True
        else:
            return self._checks_can_you_move(board_copy)
        return None
