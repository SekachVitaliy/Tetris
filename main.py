import sys
import time
from tetris import GameTetris

tetris = GameTetris()


def game():
    tetris.generate_current_figure()
    while not tetris.curr_figure_fall:
        time.sleep(0.5)
        tetris.drowe_current_figure()
        tetris.show_matrix()
        key = input('Put Key:')
        if key == 'w':
            tetris.clear_current_figure()
            if tetris.can_move_current_figure('i') == 1:
                tetris.current_rotate = tetris.rotate_inc()
            tetris.drowe_current_figure()
        elif key == 's':
            tetris.clear_current_figure()
            if tetris.can_move_current_figure('d') == 1:
                tetris.current_rotate = tetris.rotate_inc()
            tetris.drowe_current_figure()
        elif key == 'a':
            tetris.clear_current_figure()
            if tetris.can_move_current_figure('l') == 1:
                tetris.base_col -= 1
            tetris.drowe_current_figure()
        elif key == 'd':
            tetris.clear_current_figure()
            if tetris.can_move_current_figure('r') == 1:
                tetris.base_col += 1
            tetris.drowe_current_figure()
        elif key == 'x':
            sys.exit()
        tetris.clear_current_figure()
        if tetris.can_move_current_figure('b') == 1:
            tetris.base_row += 1
        if tetris.can_move_current_figure('b') == -1:
            tetris.curr_figure_fall = 1
        tetris.drowe_current_figure()
        if tetris.can_move_current_figure('b') and tetris.base_row == 0:
            tetris.curr_figure_fall = 1
            print(f'You lose! Your score: {tetris.hi_score}')
            sys.exit()
    while tetris.curr_figure_fall:
        time.sleep(0.5)
        print('\n')
        tetris.show_matrix()
        while tetris.check_and_delete_bottomest_full_row() != 0:
            time.sleep(0.5)
            print('\n')
            tetris.show_matrix()
            tetris.hi_score += 100 * tetris.check_and_delete_bottomest_full_row()
            print('Score: {tetris.hi_score}')
        tetris.curr_figure_fall = 0
    game()


if __name__ == '__main__':
    game()
