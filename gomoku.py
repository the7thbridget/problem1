class Gomoku:

    def __init__(self):
        self.board = [[0 for i in range(15)] for j in range(15)]
        self.cur_step = 0

    def player_move(self):
        while True:
            try:
                pos_x = int(input("x: "))
                pos_y = int(input("y: "))
                if 0 <= pos_x <= 14 and 0 <= pos_y <= 14:
                    if self.board[pos_x][pos_y] == 0:
                        self.board[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
                    else:
                        print("Position already taken")
                else:
                    print("Wrong input: x, y should be any integer between 0-14")
            except ValueError:
                print("Wrong input")
                continue

    def game_result(self, show=False):
        for x in range(11):
            for y in range(15):
                if self.board[x][y] == 1 and self.board[x + 1][y] == 1 and self.board[x + 2][y] == 1 and \
                        self.board[x + 3][y] == 1 and self.board[x + 4][y] == 1:
                    if show:
                        return 1, [(r, y) for r in range(x, x + 5)]
                    else:
                        return 1
                if self.board[x][y] == 2 and self.board[x + 1][y] == 2 and self.board[x + 2][y] == 2 and \
                        self.board[x + 3][y] == 2 and self.board[x + 4][y] == 2:
                    if show:
                        return 2, [(r, y) for r in range(x, x + 5)]
                    else:
                        return 2

        for x in range(15):
            for y in range(11):
                if self.board[x][y] == 1 and self.board[x][y + 1] == 1 and self.board[x][y + 2] == 1 and self.board[x][y + 3] == 1 and self.board[x][y + 4] == 1:
                    if show:
                        return 1, [(x, r) for r in range(y, y + 5)]
                    else:
                        return 1
                if self.board[x][y] == 2 and self.board[x][y + 1] == 2 and self.board[x][y + 2] == 2 and self.board[x][y + 3] == 2 and self.board[x][y + 4] == 2:
                    if show:
                        return 2, [(x, r) for r in range(y, y + 5)]
                    else:
                        return 2
        for x in range(15):
            for y in range(15):
                if self.board[x][y] == 1 and self.board[x + 1][y + 1] == 1 and self.board[x + 2][y + 2] == 1 and \
                        self.board[x + 3][y + 3] == 1 and self.board[x + 4][y + 4] == 1:
                    if show:
                        return 1, [(x + r, y + r) for r in range(5)]
                    else:
                        return 1
                if self.board[x][y] == 2 and self.board[x + 1][y + 1] == 2 and self.board[x + 2][y + 2] == 2 and \
                        self.board[x + 3][y + 3] == 2 and self.board[x + 4][y + 4] == 2:
                    if show:
                        return 2, [(x + r, y + r) for r in range(5)]
                    else:
                        return 2

        for x in range(11):
            for y in range(11):
                if self.board[x + 4][y] == 1 and self.board[x + 3][y + 1] == 1 and self.board[x + 2][y + 2] == 1 and \
                        self.board[x + 1][y + 3] == 1 and self.board[x][y + 4] == 1:
                    if show:
                        return 1, [(x + r, y + 4 - r) for r in range(5)]
                    else:
                        return 1
                if self.board[x + 4][y] == 2 and self.board[x + 3][y + 1] == 2 and self.board[x + 2][y + 2] == 2 and \
                        self.board[x + 1][y + 3] == 2 and self.board[x][y + 4] == 2:
                    if show:
                        return 2, [(x + r, y + 4 - r) for r in range(5)]
                    else:
                        return 2

        for x in range(15):
            for y in range(15):
                if self.board[x][y] == 0:
                    if show:
                        return 0, [(-1, -1)]
                    else:
                        return 0

        if show:
            return 3, [(-1, -1)]
        else:
            return 3

    def computer_move(self):
        for x in range(15):
            for y in range(15):
                if self.board[x][y] == 0:
                    self.board[x][y] = 2
                    self.cur_step += 1
                    return

    def show(self, res):
        for y in range(15):
            for x in range(15):
                if self.board[x][y] == 0:
                    print(chr(46), end='')
                elif self.board[x][y] == 1:
                    print(chr(42), end='')
                elif self.board[x][y] == 2:
                    print(chr(43), end='')

                if x != 14:
                    print('-', end='')
            print('\n', end='')

        if res == 1:
            print("Player wins!")
        elif res == 2:
            print("Computer wins!")
        elif res == 3:
            print("Tie!")

    def play(self):
        while True:
            self.player_move()
            res = self.game_result()
            if res != 0:
                self.show(res)
                return 1
            self.computer_move()
            res = self.game_result()
            if res != 0:
                self.show(res)
                return 1
            self.show(0)
            val = input("Do you want to keep playing? ")
            if val == 'q' or val == 'Q':
                return 0
