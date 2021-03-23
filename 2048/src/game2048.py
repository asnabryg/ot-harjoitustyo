
import random


class Game2048:
    """Luokka, jossa on pelin logiikka ja pelialusta.

    Attributes:
        __n: pelialustan pituus ja leveys
        __board: pelialusta 2d matriisina
    """

    def __init__(self, size, board=None, r_seed=None):
        """Luokan konstruktori, joka luo uuden pelialusta.

        Args:
            n (int): pelialustan koko (leveys ja pituus)
            board (list[list], valinnainen): Aloitus pelialusta. Oletus: None
            r_seed (int, valinnainen): Käytetään pytesteihin. Oletus: None.
        """
        self.__size = size
        if board is None:
            self.__board = self.new_board(size)
        else:
            self.__board = board
        print(self.__board)
        if r_seed is not None:
            # for pytests only
            random.seed(r_seed)

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
        for y in range(self.__size): # pylint: disable=invalid-name
            for x in range(self.__size): # pylint: disable=invalid-name
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
            # ei tyhjiä kohtia enään
            return False
        rnd = random.randint(0, 2)
        if rnd == 2:
            rnd = 4
        else:
            rnd = 2
        self.__board[yx_coordinate[0]][yx_coordinate[1]] = rnd
        return True

    def check_if_gameover(self):
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

    def move_left(self):
        """Liikuttaa ensin pelin laattoja kokonaan vasemmalle,
        sen jälkeen yhdistää vierekkäiset saman numeroiset laatat
        vaakasuoralla akselilla vasemmalta oikealle.
        Lopuksi lisää uuden laattarivin pelialustaan."""

        for y in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for x in range(self.__size):  # pylint: disable=invalid-name
                if self.__board[y][x] != 0:
                    row.append(self.__board[y][x])
            new_row = []
            if len(row) >= 2:
                x = 0  # pylint: disable=invalid-name
                while x <= len(row)-1:
                    if x+1 < len(row):
                        if row[x] == row[x+1]:
                            new_row.append(row[x] + row[x+1])
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
            self.__board[y] = new_row
        self.add_new_tile()

    def move_right(self):
        """Liikuttaa ensin pelin laattoja kokonaan oikealle,
        sen jälkeen yhdistää vierekkäiset saman numeroiset laatat
        vaakasuoralla akselilla oikealta vasemmalle.
        Lopuksi lisää uuden laattarivin pelialustaan."""

        for y in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for x in range(self.__size):  # pylint: disable=invalid-name
                if self.__board[y][x] != 0:
                    row.append(self.__board[y][x])
            new_row = []
            if len(row) >= 2:
                x = len(row)-1  # pylint: disable=invalid-name
                while x >= 0:
                    if x-1 >= 0:
                        if row[x] == row[x-1]:
                            new_row.insert(0, row[x] + row[x-1])
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

            self.__board[y] = new_row
        self.add_new_tile()

    def move_up(self):
        """Liikuttaa ensin pelin laattoja kokonaan ylös,
        sen jälkeen yhdistää peräkkäiset saman numeroiset laatat
        pystysuoralla akselilla ylhäältä alas.
        Lopuksi lisää uuden laattarivin pelialustaan."""

        for x in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for y in range(self.__size):  # pylint: disable=invalid-name
                if self.__board[y][x] != 0:
                    row.append(self.__board[y][x])
            new_row = []
            if len(row) >= 2:
                y = 0  # pylint: disable=invalid-name
                while y <= len(row)-1:
                    if y+1 < len(row):
                        if row[y] == row[y+1]:
                            new_row.append(row[y] + row[y+1])
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
                self.__board[y][x] = new_row[y]
        self.add_new_tile()

    def move_down(self):
        """Liikuttaa ensin pelin laattoja kokonaan alas,
        sen jälkeen yhdistää peräkkäiset saman numeroiset laatat
        pystysuoralla akselilla alhaalta ylös.
        Lopuksi lisää uuden laattarivin pelialustaan."""

        for x in range(self.__size):  # pylint: disable=invalid-name
            row = []
            for y in range(self.__size):  # pylint: disable=invalid-name
                if self.__board[y][x] != 0:
                    row.append(self.__board[y][x])
            new_row = []
            if len(row) >= 2:
                y = len(row) - 1  # pylint: disable=invalid-name
                while y >= 0:
                    if y-1 >= 0:
                        if row[y] == row[y-1]:
                            new_row.insert(0, row[y] + row[y-1])
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
                self.__board[y][x] = new_row[y]
        self.add_new_tile()

    def print_board(self):
        """Tulostaa komentoriville pelialustan matriisina.
        """

        print()
        for row in self.__board:
            print(row)
        print()
