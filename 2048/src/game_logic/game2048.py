
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
        self.__game_over = False
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
        return self.__game_over

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
        for y in range(self.__size):  # pylint: disable=invalid-name
            for x in range(self.__size):  # pylint: disable=invalid-name
                if self.__board[y][x] == 0:
                    empty_places.append((y, x))
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
            for y in range(self.__size):  # pylint: disable=invalid-name
                for x in range(self.__size):  # pylint: disable=invalid-name
                    if x+1 < self.__size:
                        if self.__board[y][x] == self.__board[y][x+1]:
                            return False
                    if x+1 < self.__size:
                        if self.__board[x][y] == self.__board[x+1][y]:
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

    def move_left(self, check_if_can_move=False):
        """Jos metodin parametri on True, niin tämän metodin suoritus simuloidaan,
        eikä päivitetä peliruudulle.
        Liikuttaa ensin pelin laattoja kokonaan vasemmalle,
        sen jälkeen yhdistää vierekkäiset saman numeroiset laatat
        vaakasuoralla akselilla vasemmalta oikealle.
        Lopuksi lisää uuden laattarivin pelialustaan, jos metodin parametri on False.

        Args:
            check_if_can_move (boolean, valinnainen): True, jos halutaan tarkistaa,
                                                        voiko pelaaja liikuttaa laattoja.

        Returns:
            boolean: Palauttaa totuusarvon, vain jos metodin parametri on True. Palauttaa,
                        voidaanko liikuttaa lattoja.
        """

        board = []
        board_copy = []
        if check_if_can_move:
            for row in self.__board.copy():
                board_copy.append(row.copy())
            board = board_copy
        else:
            board = self.__board

        for y in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for x in range(self.__size):  # pylint: disable=invalid-name
                if board[y][x] != 0:
                    row.append(board[y][x])
            new_row = []
            if len(row) >= 2:
                x = 0  # pylint: disable=invalid-name
                while x <= len(row)-1:
                    if x+1 < len(row):
                        if row[x] == row[x+1]:
                            value = row[x] + row[x+1]
                            new_row.append(value)
                            self.__score += value
                            x += 1  # pylint: disable=invalid-name
                        else:
                            new_row.append(row[x])
                    else:
                        new_row.append(row[x])
                    x += 1  # pylint: disable=invalid-name
            else:
                new_row = row
            for _ in range(self.__size - len(new_row)):
                new_row.append(0)
            board[y] = new_row

        if not check_if_can_move:
            if not self.add_new_tile() and self._check_if_gameover():
                self.__game_over = True
        else:
            return self._checks_can_you_move(board_copy)
        return None

    def move_right(self, check_if_can_move=False):
        """Jos metodin parametri on True, niin tämän metodin suoritus simuloidaan,
        eikä päivitetä peliruudulle.
        Liikuttaa ensin pelin laattoja kokonaan oikealle,
        sen jälkeen yhdistää vierekkäiset saman numeroiset laatat
        vaakasuoralla akselilla oikealta vasemmalle.
        Lopuksi lisää uuden laattarivin pelialustaan, jos metodin parametri on False.

        Args:
            check_if_can_move (boolean, valinnainen): True, jos halutaan tarkistaa,
                                                        voiko pelaaja liikuttaa laattoja.

        Returns:
            boolean: Palauttaa totuusarvon, vain jos metodin parametri on True. Palauttaa,
                        voidaanko liikuttaa lattoja.
        """
        board = []
        board_copy = []
        if check_if_can_move:
            for row in self.__board.copy():
                board_copy.append(row.copy())
            board = board_copy
        else:
            board = self.__board

        for y in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for x in range(self.__size):  # pylint: disable=invalid-name
                if board[y][x] != 0:
                    row.append(board[y][x])
            new_row = []
            if len(row) >= 2:
                x = len(row)-1  # pylint: disable=invalid-name
                while x >= 0:
                    if x-1 >= 0:
                        if row[x] == row[x-1]:
                            value = row[x] + row[x-1]
                            new_row.insert(0, value)
                            self.__score += value
                            x -= 1  # pylint: disable=invalid-name
                        else:
                            new_row.insert(0, row[x])
                    else:
                        new_row.insert(0, row[x])
                    x -= 1  # pylint: disable=invalid-name
            else:
                new_row = row
            for _ in range(self.__size - len(new_row)):
                new_row.insert(0, 0)

            board[y] = new_row

        if not check_if_can_move:
            if not self.add_new_tile() and self._check_if_gameover():
                self.__game_over = True
        else:
            return self._checks_can_you_move(board_copy)
        return None

    def move_up(self, check_if_can_move=False):
        """Jos metodin parametri on True, niin tämän metodin suoritus simuloidaan,
        eikä päivitetä peliruudulle.
        Liikuttaa ensin pelin laattoja kokonaan ylös,
        sen jälkeen yhdistää peräkkäiset saman numeroiset laatat
        pystysuoralla akselilla ylhäältä alas.
        Lopuksi lisää uuden laattarivin pelialustaan, jos metodin parametri on False.

        Args:
            check_if_can_move (boolean, valinnainen): True, jos halutaan tarkistaa,
                                                        voiko pelaaja liikuttaa laattoja.

        Returns:
            boolean: Palauttaa totuusarvon, vain jos metodin parametri on True. Palauttaa,
                        voidaanko liikuttaa lattoja.
        """
        board = []
        board_copy = []
        if check_if_can_move:
            for row in self.__board.copy():
                board_copy.append(row.copy())
            board = board_copy
        else:
            board = self.__board

        for x in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for y in range(self.__size):  # pylint: disable=invalid-name
                if board[y][x] != 0:
                    row.append(board[y][x])
            new_row = []
            if len(row) >= 2:
                y = 0  # pylint: disable=invalid-name
                while y <= len(row)-1:
                    if y+1 < len(row):
                        if row[y] == row[y+1]:
                            value = row[y] + row[y+1]
                            new_row.append(value)
                            self.__score += value
                            y += 1  # pylint: disable=invalid-name
                        else:
                            new_row.append(row[y])
                    else:
                        new_row.append(row[y])
                    y += 1  # pylint: disable=invalid-name
            else:
                new_row = row
            for _ in range(self.__size - len(new_row)):
                new_row.append(0)
            for y in range(self.__size):  # pylint: disable=invalid-name
                board[y][x] = new_row[y]

        if not check_if_can_move:
            if not self.add_new_tile() and self._check_if_gameover():
                self.__game_over = True
        else:
            return self._checks_can_you_move(board_copy)
        return None

    def move_down(self, check_if_can_move=False):
        """Jos metodin parametri on True, niin tämän metodin suoritus simuloidaan,
        eikä päivitetä peliruudulle.
        Liikuttaa ensin pelin laattoja kokonaan alas,
        sen jälkeen yhdistää peräkkäiset saman numeroiset laatat
        pystysuoralla akselilla alhaalta ylös.
        Lopuksi lisää uuden laattarivin pelialustaan, jos metodin parametri on False.

        Args:
            check_if_can_move (boolean, valinnainen): True, jos halutaan tarkistaa,
                                                        voiko pelaaja liikuttaa laattoja.

        Returns:
            boolean: Palauttaa totuusarvon, vain jos metodin parametri on True. Palauttaa,
                        voidaanko liikuttaa lattoja.
        """

        board = []
        board_copy = []
        if check_if_can_move:
            for row in self.__board.copy():
                board_copy.append(row.copy())
            board = board_copy
        else:
            board = self.__board

        for x in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for y in range(self.__size):  # pylint: disable=invalid-name
                if board[y][x] != 0:
                    row.append(board[y][x])
            new_row = []
            if len(row) >= 2:
                y = len(row) - 1  # pylint: disable=invalid-name
                while y >= 0:
                    if y-1 >= 0:
                        if row[y] == row[y-1]:
                            value = row[y] + row[y-1]
                            new_row.insert(0, value)
                            self.__score += value
                            y -= 1  # pylint: disable=invalid-name
                        else:
                            new_row.insert(0, row[y])
                    else:
                        new_row.insert(0, row[y])
                    y -= 1  # pylint: disable=invalid-name
            else:
                new_row = row
            for _ in range(self.__size - len(new_row)):
                new_row.insert(0, 0)
            for y in range(self.__size):  # pylint: disable=invalid-name
                board[y][x] = new_row[y]

        if not check_if_can_move:
            if not self.add_new_tile() and self._check_if_gameover():
                self.__game_over = True
        else:
            return self._checks_can_you_move(board_copy)
        return None
