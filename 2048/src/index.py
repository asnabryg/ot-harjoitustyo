
from game2048 import Game2048
from ui.ui import Userinterface

board = [[4, 0, 2, 2],
         [0, 0, 2, 0],
         [4, 2, 0, 0],
         [4, 0, 0, 0]]

def main():
    print("Start!")
    # ui = Userinterface()  # pylint: disable=invalid-name
    peli = Game2048(4, board=board)
    peli.print_board()
    peli.move_down()
    peli.print_board()



if __name__ == '__main__':
    main()
