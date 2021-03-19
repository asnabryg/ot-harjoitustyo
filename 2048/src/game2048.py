
import random

class Game2048:

    def __init__(self, n, r_seed=None):
        self.__n = n
        self.__board = self.new_board(n)
        print(self.__board)
        if r_seed != None:
            # pytest käyttää seed, jotta testit voidaan suorittaa
            random.seed(r_seed)
    
    def get_n(self):
        return self.__n

    def get_board(self):
        return self.__board

    def new_board(self, n):
        #luo uuden tyhjän laudan
        board = [0] * n
        for i in range(n):
            board[i] = [0] * n
        return board

    def get_random_empty_place(self):
        empty_places = []
        for y in range(self.__n):
            for x in range(self.__n):
                # hakee jokaisen 0 kohdan listaan
                if self.__board[y][x] == 0:
                    empty_places.append((y, x))
        if len(empty_places) == 0:
            # palauttaa None nolla kohtana
            return None
        # palauttaa yhden random nolla kohdan
        return random.choice(empty_places)

    def add_new_tile(self):
        # lisää uuden laatan laudalle. Laatan numero on joko 2 tai 4.
        yx= self.get_random_empty_place()
        if yx == None:
            # Gameover
            # ei tyhjiä kohtia enään
            return False
        rnd = random.randint(0, 2)
        if rnd == 2:
            rnd = 4
        else:
            rnd = 2
        self.__board[yx[0]][yx[1]] = rnd
        return True
