import arcade
import math


# class MenuView(arcade.View):
#     def on_show(self):
#         arcade.set_background_color(arcade.color.WHITE)
#
#     def on_draw(self):
#         arcade.start_render()
#
#         menu = arcade.load_texture("okk.jpg)")
#         scaled = 1.1
#         arcade.draw_scaled_texture_rectangle(700, 200, menu, scaled)
#
#     def on_mouse_press(self, _x, _y, _button, _modifiers):
#         mygame = Game()
#         mygame.setup()
#         arcade.run()


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1300, height=730, title="Game", center_window=True)

        self.point_x = 200
        self.point_y = 200

        # splash coordinate
        self.splash_x = None
        self.splash_y = None

        # row and column
        self.row = None
        self.column = None

        # players list
        self.player_list = None

        # sprite_1 coordinate
        self.sprite1 = None
        self.sprite2 = None

        # legal
        self.legal = False

        # scores
        self.sprite1_score = 00
        self.sprite2_score = 00

        # sprite turnings
        self.sprite1_turn = True
        self.sprite2_turn = False

        self.legal_left = False
        self.legal_right = False
        self.legal_up = False
        self.legal_down = False

        # sprite  movement controls
        self.sprite_left = False
        self.sprite_right = False
        self.sprite_up = False
        self.sprite_down = False

    def is_legal(self):

        if self.legal_left:
            if self.sprite1_turn:
                print('left')
                self.column = (self.sprite1.center_x - 80) // 80
                self.row = self.sprite1.center_y // 80
                print(self.row, self.column)
                if self.backend_grid[self.row][self.column - 1] != 20 and \
                        self.backend_grid[self.row][self.column - 1] != 2:

                    self.sprite_left = True
                    self.legal_left = False

                    # spalsh
                    self.splash_1 = arcade.Sprite("grens.jpg", .17)
                    self.splash_1.center_x = self.sprite1.center_x
                    self.splash_1.center_y = self.sprite1.center_y
                    self.player_list.append(self.splash_1)
                    self.sprite1.center_x -= 80

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True

            elif self.sprite2_turn:

                self.column = (self.sprite2.center_x - 80) // 80
                self.row = self.sprite2.center_y // 80
                if self.backend_grid[self.row][self.column - 1] != 10 and \
                        self.backend_grid[self.row][self.column - 1] != 1:

                    self.sprite_left = True
                    self.legal_left = False

                    self.splash_2 = arcade.Sprite("yelow.png", .33)
                    self.splash_2.center_x = self.sprite2.center_x
                    self.splash_2.center_y = self.sprite2.center_y
                    self.player_list.append(self.splash_2)
                    self.sprite2.center_x -= 80

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True

        if self.legal_right:

            if self.sprite1_turn:
                self.column = ((self.sprite1.center_x) - 80) // 80
                self.row = (self.sprite1.center_y) // 80
                print(self.row, self.column)
                if self.backend_grid[self.row][self.column + 1] != 20 and \
                        self.backend_grid[self.row][self.column + 1] != 2:

                    self.sprite_right = True
                    self.legal_right = False

                    self.splash_1 = arcade.Sprite("grens.jpg", .17)
                    self.splash_1.center_x = self.sprite1.center_x
                    self.splash_1.center_y = self.sprite1.center_y
                    self.player_list.append(self.splash_1)
                    self.sprite1.center_x += 80

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True

            elif self.sprite2_turn:
                self.column = ((self.sprite2.center_x) - 80) // 80
                self.row = (self.sprite2.center_y) // 80

                if self.backend_grid[self.row][self.column + 1] != 10 and \
                        self.backend_grid[self.row][self.column + 1] != 1:

                    self.sprite_right = True
                    self.legal_right = False

                    # spalsh
                    self.splash_2 = arcade.Sprite("yelow.png", .33)
                    self.splash_2.center_x = self.sprite2.center_x
                    self.splash_2.center_y = self.sprite2.center_y
                    self.player_list.append(self.splash_2)
                    self.sprite2.center_x += 80

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True

        if self.legal_up:

            if self.sprite1_turn:
                self.column = ((self.sprite1.center_x) - 80) // 80
                self.row = (self.sprite1.center_y) // 80
                print(self.row, self.column)
                if self.backend_grid[self.row + 1][self.column] != 20 and \
                        self.backend_grid[self.row + 1][self.column] != 2:
                    self.sprite1.center_y += 80
                    self.sprite_up = True
                    self.legal_up = False

                    self.splash_1 = arcade.Sprite("grens.jpg", .17)
                    self.splash_1.center_x = self.sprite1.center_x
                    self.splash_1.center_y = self.sprite1.center_y - 80
                    self.player_list.append(self.splash_1)

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True

            elif self.sprite2_turn:
                self.column = ((self.sprite2.center_x) - 80) // 80
                self.row = (self.sprite2.center_y) // 80

                if self.backend_grid[self.row + 1][self.column] != 10 and \
                        self.backend_grid[self.row + 1][self.column] != 1:
                    self.sprite2.center_y += 80
                    self.sprite_up = True
                    self.legal_up = False

                    # spalsh

                    self.splash_2 = arcade.Sprite("yelow.png", .33)
                    self.splash_2.center_x = self.sprite2.center_x
                    self.splash_2.center_y = self.sprite2.center_y - 80
                    self.player_list.append(self.splash_2)

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True

        if self.legal_down:

            if self.sprite1_turn:
                print('down h')
                self.column = ((self.sprite1.center_x) - 80) // 80
                self.row = (self.sprite1.center_y) // 80
                print(self.row, self.column)
                if self.backend_grid[self.row - 1][self.column] != 20 and \
                        self.backend_grid[self.row - 1][self.column] != 2:
                    self.sprite1.center_y -= 80
                    self.sprite_down = True
                    self.legal_down = False

                    self.splash_1 = arcade.Sprite("grens.jpg", .17)
                    self.splash_1.center_x = self.sprite1.center_x
                    self.splash_1.center_y = self.sprite1.center_y + 80
                    self.player_list.append(self.splash_1)

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True

            elif self.sprite2_turn:
                print('down')
                self.column = ((self.sprite2.center_x) - 80) // 80
                self.row = (self.sprite2.center_y) // 80

                if self.backend_grid[self.row - 1][self.column] != 10 and \
                        self.backend_grid[self.row - 1][self.column] != 1:
                    self.sprite2.center_y -= 80
                    self.sprite_down = True
                    self.legal_down = False

                    # spalsh
                    self.splash_2 = arcade.Sprite("yelow.png", .33)
                    self.splash_2.center_x = self.sprite2.center_x
                    self.splash_2.center_y = self.sprite2.center_y + 80
                    self.player_list.append(self.splash_2)

                    return True
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True

        # sprite movment

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT:
            if self.sprite1_turn:
                if self.sprite1.center_x - 80 > 80:
                    self.legal_left = True
                    self.legal = self.is_legal()
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True

            elif self.sprite2_turn:
                if self.sprite2.center_x - 80 > 80:
                    self.legal_left = True
                    self.legal = self.is_legal()
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True

        if symbol == arcade.key.RIGHT:

            if self.sprite1_turn:
                if self.sprite1.center_x + 80 < 900:
                    self.legal_right = True
                    self.legal = self.is_legal()

                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True
            elif self.sprite2_turn:
                if self.sprite2.center_x + 80 < 900:
                    self.legal_right = True
                    self.legal = self.is_legal()

                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True

        if symbol == arcade.key.UP:
            if self.sprite1_turn:
                if self.sprite1.center_y + 80 < 670:
                    self.legal_up = True
                    self.legal = self.is_legal()

                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True
            elif self.sprite2_turn:
                if self.sprite2.center_y + 80 < 670:
                    self.legal_up = True
                    self.legal = self.is_legal()

                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True
            pass

        if symbol == arcade.key.DOWN:
            if self.sprite1_turn:
                print('before h')
                if self.sprite1.center_y - 80 > 30:
                    self.legal_down = True
                    self.legal = self.is_legal()

                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite1_turn = False
                    self.sprite2_turn = True
            elif self.sprite2_turn:
                print('before legal')
                if self.sprite2.center_y - 80 > 30:
                    self.legal_down = True
                    self.legal = self.is_legal()
                else:
                    wrong = arcade.load_sound("wrong.wav")
                    wrong.play(1.0)
                    self.sprite2_turn = False
                    self.sprite1_turn = True

    def on_key_release(self, symbol: int, modifiers: int):

        if symbol == arcade.key.UP or arcade.key.DOWN:
            self.sprite_up = False
            self.sprite_down = False
            self.legal_down = False
            self.legal_up = False

        if symbol == arcade.key.LEFT or arcade.key.RIGHT:
            self.sprite_left = False
            self.sprite_right = False
        # self.legal_right=False
        # self.legal_left=False

    def on_update(self, delta_time: float):

        if self.sprite_left and self.legal:
            move = arcade.load_sound("move.wav")
            move.play(1.0)

            if self.sprite1_turn:

                self.legal = False
                # sliding
                if self.backend_grid[self.row][self.column - 1] == 10:
                    self.backend_grid[self.row][self.column] = 10

                    col = self.column - 1
                    while self.backend_grid[self.row][col] == 10 and col > 0:
                        self.sprite1.center_x -= 80
                        col -= 1
                        if col > 0:
                            if self.backend_grid[self.row][col - 1] != 10:
                                break
                    self.column = (self.sprite1.center_x - 80) // 80
                    self.backend_grid[self.row][self.column] = 1
                    print(self.backend_grid)
                    self.result()
                    self.sprite1_turn = False
                    self.sprite2_turn = True

                else:

                    self.backend_grid[self.row][self.column] = 10
                    self.backend_grid[self.row][self.column - 1] = 1
                    self.sprite1_turn = False
                    self.sprite2_turn = True
                    self.result()
                    print(self.backend_grid)
            # self.sprite1_turn = False

            elif self.sprite2_turn:
                self.legal = False

                # sliding
                if self.backend_grid[self.row][self.column - 2] == 20:
                    self.backend_grid[self.row][self.column] = 20
                    col = self.column - 1
                    while self.backend_grid[self.row][col] == 20 and col > 0:
                        self.sprite2.center_x -= 80
                        col -= 1
                        if col > 0:
                            if self.backend_grid[self.row][col - 1] != 20:
                                break
                    self.column = (self.sprite2.center_x - 80) // 80
                    self.backend_grid[self.row][self.column] = 2
                    print(self.backend_grid)
                    self.result()
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                else:
                    self.backend_grid[self.row][self.column] = 20
                    self.backend_grid[self.row][self.column - 1] = 2
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                    self.result()
                    print(self.backend_grid)
            # self.sprite1_turn = True

        if self.sprite_right and self.legal:
            move = arcade.load_sound("move.wav")
            move.play(1.0)

            if self.sprite1_turn:
                self.legal = False
                print('yes right nh')
                # sliding
                if self.backend_grid[self.row][self.column + 1] == 10:
                    self.backend_grid[self.row][self.column] = 10
                    col = self.column + 1
                    while self.backend_grid[self.row][col] == 10 and col < 9:
                        self.sprite1.center_x += 80
                        col += 1
                        if col < 9:
                            if self.backend_grid[self.row][col + 1] != 10:
                                break
                    self.column = (self.sprite1.center_x - 80) // 80
                    self.backend_grid[self.row][self.column] = 1
                    print(self.backend_grid)
                    self.sprite1_turn = False
                    self.sprite2_turn = True
                    self.result()
                else:
                    self.backend_grid[self.row][self.column] = 10
                    self.backend_grid[self.row][self.column + 1] = 1
                    self.sprite1_turn = False
                    self.sprite2_turn = True
                    self.result()
                    print(self.backend_grid)

            # self.sprite1_turn = False

            else:
                print('right')
                self.legal = False

                # sliding
                if self.backend_grid[self.row][self.column + 1] == 20:
                    self.backend_grid[self.row][self.column] = 20
                    col = self.column + 1
                    while self.backend_grid[self.row][col] == 20 and col < 9:
                        self.sprite2.center_x += 80
                        col += 1
                        if col < 9:
                            if self.backend_grid[self.row][col + 1] != 20:
                                print('gg')
                                break
                    self.column = (self.sprite2.center_x - 80) // 80
                    self.backend_grid[self.row][self.column] = 2
                    print(self.backend_grid)
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                    self.result()

                else:
                    self.backend_grid[self.row][self.column] = 20
                    self.backend_grid[self.row][self.column + 1] = 2
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                    self.result()
                    print(self.backend_grid)
                # self.sprite1_turn = True

        if self.sprite_up and self.legal:
            move = arcade.load_sound("move.wav")
            move.play(1.0)
            if self.sprite1_turn:
                self.legal = False
                # sliding

                if self.backend_grid[self.row + 1][self.column] == 10:
                    self.backend_grid[self.row][self.column] = 10
                    roww = self.row + 1
                    while self.backend_grid[roww][self.column] == 10 and roww < 7:
                        self.sprite1.center_y += 80
                        roww += 1
                        if roww < 7:
                            if self.backend_grid[roww + 1][self.column] != 10:
                                break
                    self.row = self.sprite1.center_y // 80
                    self.backend_grid[self.row][self.column] = 1
                    print(self.backend_grid)
                    self.sprite1_turn = False
                    self.sprite2_turn = True
                    self.result()
                else:
                    self.backend_grid[self.row + 1][self.column] = 1
                    self.backend_grid[self.row][self.column] = 10
                    self.sprite1_turn = False
                    self.sprite2_turn = True
                    # self.sprite1_turn = False
                    self.result()
                    print(self.backend_grid)
            else:
                self.legal = False
                # sliding

                if self.backend_grid[self.row + 1][self.column] == 20:
                    self.backend_grid[self.row][self.column] = 20
                    roww = self.row + 1
                    while self.backend_grid[roww][self.column] == 20 and roww < 7:
                        self.sprite2.center_y += 80
                        roww += 1
                        if roww < 7:
                            if self.backend_grid[roww + 1][self.column] != 20:
                                break
                    self.row = self.sprite2.center_y // 80
                    self.backend_grid[self.row][self.column] = 2
                    print(self.backend_grid)
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                    self.result()
                else:
                    self.backend_grid[self.row + 1][self.column] = 2
                    self.backend_grid[self.row][self.column] = 20
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                    self.result()
                    print(self.backend_grid)
            # self.sprite1_turn = True

        if self.sprite_down and self.legal:
            move = arcade.load_sound("move.wav")
            move.play(1.0)

            if self.sprite1_turn:
                self.legal = False
                # sliding
                if self.backend_grid[self.row - 1][self.column] == 10:
                    self.backend_grid[self.row][self.column] = 10
                    roww = self.row - 1
                    while self.backend_grid[roww][self.column] == 10 and roww > 0:
                        self.sprite1.center_y -= 80
                        roww -= 1
                        if roww > 0:
                            if self.backend_grid[roww - 1][self.column] != 10:
                                break
                    self.row = self.sprite1.center_y // 80
                    self.backend_grid[self.row][self.column] = 1
                    print(self.backend_grid)
                    self.sprite1_turn = False
                    self.sprite2_turn = True
                    self.result()
                else:
                    self.backend_grid[self.row - 1][self.column] = 1
                    self.backend_grid[self.row][self.column] = 10
                    self.sprite1_turn = False
                    self.sprite2_turn = True
                    self.result()
                    print(self.backend_grid)
                #  self.sprite1_turn = False

                print(self.backend_grid)
            else:
                self.legal = False
                # sliding
                if self.backend_grid[self.row - 1][self.column] == 20:
                    self.backend_grid[self.row][self.column] = 20
                    roww = self.row - 1
                    while self.backend_grid[roww][self.column] == 20 and roww > 0:
                        self.sprite2.center_y -= 80
                        roww -= 1
                        if roww > 0:
                            if self.backend_grid[roww - 1][self.column] != 20:
                                break
                    self.row = self.sprite2.center_y // 80
                    self.backend_grid[self.row][self.column] = 2
                    print(self.backend_grid)
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                    self.result()
                else:
                    self.backend_grid[self.row - 1][self.column] = 2
                    self.backend_grid[self.row][self.column] = 20
                    self.sprite2_turn = False
                    self.sprite1_turn = True
                    self.result()
                    print(self.backend_grid)

    def result(self):
        score1 = 0
        score2 = 0
        for i in range(8):

            for k in range(10):
                if self.backend_grid[i][k] == 10 or self.backend_grid[i][k] == 20:
                    if self.backend_grid[i][k] == 10:
                        score1 += 1
                    if self.backend_grid[i][k] == 20:
                        score2 += 1

        self.sprite2_score = score2
        self.sprite1_score = score1

        if self.sprite1_score == 40 or self.sprite2_score == 40:
            if self.sprite1_score == 40:
                arcade.exit()
            else:
                arcade.exit()

    def setup(self):
        self.player_list = arcade.SpriteList()

        # 1st sprite

        self.sprite1 = arcade.Sprite("smile.png", .33)
        self.sprite1.center_x = 120
        self.sprite1.center_y = 70
        # self.player_list.append(self.sprite1)

        # 2nd sprite
        self.sprite2 = arcade.Sprite("yel.jpg", .34)
        self.sprite2.center_x = 840
        self.sprite2.center_y = 630
        # self.player_list.append(self.sprite2)

        # backend grid formation
        column = 10
        rows = 8
        self.backend_grid = [[0 for i in range(column)] for i in range(rows)]

        # // initializing sprites's initial positions
        self.backend_grid[0][0] = 1
        self.backend_grid[7][9] = 2
        print(self.backend_grid)

    def on_draw(self):
        arcade.start_render()
        background = arcade.load_texture("background 2.jpg")
        arcade.draw_scaled_texture_rectangle(700, 450, background, 5.0)

        arcade.draw_rectangle_filled(1080, 230, 190, 280, arcade.color.WHITE_SMOKE)
        spr1 = arcade.load_texture("smile.jpg")
        arcade.draw_scaled_texture_rectangle(1080, 280, spr1, .63)

        arcade.draw_rectangle_filled(1080, 580, 190, 260, arcade.color.WHITE_SMOKE)
        spr1 = arcade.load_texture("yel.jpg")
        arcade.draw_scaled_texture_rectangle(1080, 640, spr1, .54)

        arcade.draw_text(str(self.sprite1_score), 1066, 130, arcade.color.RED, font_size=40)
        arcade.draw_text(str(self.sprite2_score), 1062, 490, arcade.color.RED, font_size=40)

        arcade.draw_rectangle_outline(950, 380, 10, 780, arcade.color.BLUE)
        # x_lines
        for x_line in range(30, 790, 80):
            arcade.draw_line(80, x_line, 880, x_line, arcade.color.BLACK, 6)

        # y_lines
        for y_line in range(80, 950, 80):
            arcade.draw_line(y_line, 30, y_line, 670, arcade.color.BLACK, 4)

        self.player_list.draw()
        self.sprite1.draw()
        self.sprite2.draw()
        # splash drawing


mygame = Game()
mygame.setup()
arcade.run()
# def main():
#     window = arcade.Window(800, 650, "Snails Game")
#
#     menu_view = MenuView()
#     window.show_view(menu_view)
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()
