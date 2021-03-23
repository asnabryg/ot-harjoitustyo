
from game2048 import Game2048
from ui.ui import Userinterface

board = [[2, 0, 0, 0],
         [0, 2, 0, 0],
         [2, 0, 2, 2],
         [2, 2, 2, 2]]

def main():
    print("Start!")
    # ui = Userinterface()  # pylint: disable=invalid-name
    peli = Game2048(4, board=board)
    # peli.add_new_tile()
    peli.print_board()
    peli.move_left()
    peli.print_board()
    # peli.move_right()
    # peli.print_board()



if __name__ == '__main__':
    main()
