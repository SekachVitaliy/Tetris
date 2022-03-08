import random


class GameTetris:
    def __init__(self):
        self.Dx = 8
        self.Dy = 8
        self.base_row = 0
        self.base_col = 1
        self.curr_figure_fall = 0
        self.hi_score = 0
        self.matrix = []
        self.rotating = ['ROT_LEFT', 'ROT_UP', 'ROT_RIGHT', 'ROT_DOWN']
        self.figures = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']
        self.joysticks = ['J_LEFT', 'J_RIGHT', 'J_UP', 'J_DOWN', 'J_PUSH', 'J_UNDEF']
        self.current_rotate = ''
        self.current_figure = ''
        for i in range(self.Dx):
            self.matrix.append([])
            for j in range(self.Dy):
                self.matrix[i].append(0)

    def generate_current_figure(self):
        x = random.randint(0, 5)
        self.current_figure = self.figures[x]
        self.base_row = 0
        self.base_col = 3
        self.current_rotate = 'ROT_LEFT'
        self.curr_figure_fall = 0

    def show_matrix(self):
        print("**********************************************************")
        print(f'HISCORE: {self.hi_score}')
        for i in range(self.Dx):
            for j in range(self.Dy):
                if self.matrix[i][j] == 1:
                    print("% ", end='')
                else:
                    print("_ ", end='')
            print()
        print("**********************************************************")

    def rotate_inc(self):
        if self.current_rotate == 'ROT_LEFT':
            return self.rotating[1]
            # self.current_rotate = self.rotating[4]  # ROT_UP
        elif self.current_rotate == 'ROT_UP':
            return self.rotating[2]
            # self.current_rotate = self.rotating[2]  # ROT_RIGHT
        elif self.current_rotate == 'ROT_RIGHT':
            return self.rotating[3]
            # self.current_rotate = self.rotating[1]  # ROT_DOWN
        elif self.current_rotate == 'ROT_DOWN':
            return self.rotating[0]
            # self.current_rotate = self.rotating[0]  # ROT_LEFT

    def rotate_dec(self):
        if self.current_rotate == 'ROT_LEFT':
            return self.rotating[3]
            # self.current_rotate = self.rotating[3]  # ROT_DOWN
        elif self.current_rotate == 'ROT_UP':
            return self.rotating[0]
            # self.current_rotate = self.rotating[0]  # ROT_LEFT
        elif self.current_rotate == 'ROT_RIGHT':
            return self.rotating[1]
            # self.current_rotate = self.rotating[1]  # ROT_UP
        elif self.current_rotate == 'ROT_DOWN':
            return self.rotating[2]
            # self.current_rotate = self.rotating[2]  # ROT_RIGHT

    def drowe_current_figure(self):
        self.drowe_or_clear_figure(1)  # устанавливает значение

    def clear_current_figure(self):
        self.drowe_or_clear_figure(0)  # обнуляет значение

    def can_move_current_figure(self, direct):
        test_pos_row = 0
        test_pos_col = 0
        rotate = 0
        non_overlap = False
        in_bounds = False

        if direct == 'l':
            test_pos_row = self.base_row
            test_pos_col = self.base_col - 1
            rotate = self.current_rotate
        elif direct == 'r':
            test_pos_row = self.base_row
            test_pos_col = self.base_col + 1
            rotate = self.current_rotate
        elif direct == 'b':
            test_pos_row = self.base_row + 1
            test_pos_col = self.base_col
            rotate = self.current_rotate
        elif direct == 'i':
            test_pos_row = self.base_row
            test_pos_col = self.base_col
            rotate = self.rotate_inc()
        elif direct == 'd':
            test_pos_row = self.base_row
            test_pos_col = self.base_col
            rotate = self.rotate_dec()

        if self.current_figure == 'ONE':
            if 8 > test_pos_row + 0 > -1 and 8 > test_pos_col + 0 > -1:
                in_bounds = True
                if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0:
                    non_overlap = True

        if self.current_figure == 'TWO':
            if rotate == 'ROT_LEFT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col + 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_UP':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_col + 0 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col + 0] == 0:
                        non_overlap = True
            elif rotate == 'ROT_RIGHT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col - 1] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col + 0] == 0:
                        non_overlap = True
            elif rotate == 'ROT_DOWN':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_col + 0 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 0] == 0:
                        non_overlap = True

        if self.current_figure == 'THREE':
            if rotate == 'ROT_LEFT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_col + 0 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 0] == 0:
                        non_overlap = True
            elif rotate == 'ROT_UP':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col + 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_RIGHT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_col + 0 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row - 1][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col + 0] == 0:
                        non_overlap = True
            elif rotate == 'ROT_DOWN':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col - 1] == 0:
                        non_overlap = True
        if self.current_figure == 'FOUR':
            if rotate == 'ROT_LEFT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col + 1] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_UP':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col + 1] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col + 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_RIGHT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col - 1] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col - 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_DOWN':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col - 1] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col - 1] == 0:
                        non_overlap = True

        if self.current_figure == 'FIVE':
            if rotate == 'ROT_LEFT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_UP':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col + 1] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col + 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_RIGHT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col - 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_DOWN':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 0][test_pos_col - 1] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col - 1] == 0:
                        non_overlap = True
        if self.current_figure == 'SIX':
            if rotate == 'ROT_LEFT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1 and \
                        8 > test_pos_col + 2 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 1] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col + 2] == 0:
                        non_overlap = True
            elif rotate == 'ROT_UP':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_row - 2 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col + 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col + 1] == 0 and \
                            self.matrix[test_pos_row - 2][test_pos_col + 1] == 0:
                        non_overlap = True
            elif rotate == 'ROT_RIGHT':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row - 1 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1 and \
                        8 > test_pos_col - 2 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col - 1] == 0 and \
                            self.matrix[test_pos_row - 1][test_pos_col - 2] == 0:
                        non_overlap = True
            elif rotate == 'ROT_DOWN':
                if 8 > test_pos_row + 0 > -1 and \
                        8 > test_pos_row + 1 > -1 and \
                        8 > test_pos_row + 2 > -1 and \
                        8 > test_pos_col + 0 > -1 and \
                        8 > test_pos_col - 1 > -1:
                    in_bounds = True
                    if self.matrix[test_pos_row + 0][test_pos_col + 0] == 0 and \
                            self.matrix[test_pos_row + 1][test_pos_col - 1] == 0 and \
                            self.matrix[test_pos_row + 2][test_pos_col - 1] == 0:
                        non_overlap = True

        if non_overlap and in_bounds:
            return 1
        elif not non_overlap and direct == 'b':
            return -1
        elif not in_bounds and direct == 'b':
            return -1
        else:
            return 0

    def sum_of_row(self, row):
        return sum(self.matrix[row])

    def check_and_delete_bottomest_full_row(self):
        i = 7
        factor = 0
        while i > -1:
            if self.sum_of_row(i) == 8:
                for j in range(i, 0, -1):
                    for k in range(0, 8):
                        self.matrix[j][k] = self.matrix[j - 1][k]
                factor += 1
            i -= 1
        return factor

    def drowe_or_clear_figure(self, value):
        """ принимает значение 0 или 1 и заносит его в масисв относительно данной фигуры """

        if self.current_figure == 'ONE':  # figure *

            self.matrix[self.base_row + 0][self.base_col + 0] = value

        elif self.current_figure == 'TWO':  # figure **

            if self.current_rotate == 'ROT_LEFT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col + 1] = value
            elif self.current_rotate == 'ROT_UP':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row - 1][self.base_col + 0] = value

            elif self.current_rotate == 'ROT_RIGHT':
                self.matrix[self.base_row + 0][self.base_col - 1] = value
                self.matrix[self.base_row + 0][self.base_col + 0] = value

            elif self.current_rotate == 'ROT_DOWN':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col + 0] = value

        elif self.current_figure == 'THREE':  # figure      *
            #                                               *

            if self.current_rotate == 'ROT_LEFT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col + 0] = value

            elif self.current_rotate == 'ROT_UP':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col + 1] = value

            elif self.current_rotate == 'ROT_RIGHT':
                self.matrix[self.base_row - 1][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col + 0] = value

            elif self.current_rotate == 'ROT_DOWN':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col - 1] = value

        elif self.current_figure == 'FOUR':  # figure      **
            #                                              **

            if self.current_rotate == 'ROT_LEFT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col + 1] = value
                self.matrix[self.base_row + 1][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col + 1] = value

            elif self.current_rotate == 'ROT_UP':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col + 1] = value
                self.matrix[self.base_row - 1][self.base_col + 0] = value
                self.matrix[self.base_row - 1][self.base_col + 1] = value

            elif self.current_rotate == 'ROT_RIGHT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row - 1][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col - 1] = value
                self.matrix[self.base_row - 1][self.base_col - 1] = value

            elif self.current_rotate == 'ROT_DOWN':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col - 1] = value
                self.matrix[self.base_row + 1][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col - 1] = value

        elif self.current_figure == 'FIVE':  # figure      *
            #                                              * *

            if self.current_rotate == 'ROT_LEFT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col + 1] = value

            elif self.current_rotate == 'ROT_UP':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col + 1] = value
                self.matrix[self.base_row - 1][self.base_col + 1] = value

            elif self.current_rotate == 'ROT_RIGHT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row - 1][self.base_col + 0] = value
                self.matrix[self.base_row - 1][self.base_col - 1] = value

            elif self.current_rotate == 'ROT_DOWN':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 0][self.base_col - 1] = value
                self.matrix[self.base_row + 1][self.base_col - 1] = value

        elif self.current_figure == 'SIX':  # figure      *
            #                                              **
            if self.current_rotate == 'ROT_LEFT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col + 1] = value
                self.matrix[self.base_row + 1][self.base_col + 2] = value
            elif self.current_rotate == 'ROT_UP':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row - 1][self.base_col + 1] = value
                self.matrix[self.base_row - 2][self.base_col + 1] = value

            elif self.current_rotate == 'ROT_RIGHT':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row - 1][self.base_col - 1] = value
                self.matrix[self.base_row - 1][self.base_col - 2] = value

            elif self.current_rotate == 'ROT_DOWN':
                self.matrix[self.base_row + 0][self.base_col + 0] = value
                self.matrix[self.base_row + 1][self.base_col - 1] = value
                self.matrix[self.base_row + 2][self.base_col - 1] = value
