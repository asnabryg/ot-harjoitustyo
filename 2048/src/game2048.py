
import random


class Game2048:
    """Luokka, jossa on pelin logiikka ja pelialusta.

    Attributes:
        __n: pelialustan pituus ja leveys
        __board: pelialusta 2d matriisina
    """

    def __init__(self, size, r_seed=None):
        """Luokan konstruktori, joka luo uuden pelialusta.

        Args:
            n (int): pelialustan koko (leveys ja pituus)
            r_seed (int, valinnainen): Käytetään pytesteihin. Oletus: None.
        """
        self.__size = size
        self.__board = self.new_board(size)
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
                # hakee jokaisen 0 kohdan listaan
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
