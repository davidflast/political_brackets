from Brackets.Game import Game


class Bracket(object):
    def __init__(self, num_col):
        self.num_col = num_col
        self.num_row = num_col ** 2
        self.root = Game(1, num_col, self.create_child(num_col - 1, 1), self.create_child(num_col - 1, 2))

    def create_child(self, row, col):
        if col == 0:
            return None
        next_row_one = (row * 2) - 1
        next_row_two = row * 2
        next_col = col - 1
        child_one = self.create_child(next_row_one, next_col)
        child_two = self.create_child(next_row_two, next_col)
        return Game(row, col, child_one, child_two)

    def get_root(self):
        return self.root

    def get_num_col(self):
        return self.num_col

    def get_num_row(self):
        return self.num_row

    def access_game(self, row, col):
        return self.access_game_helper(self.root, row, self.num_col - col)

    def access_game_helper(self, game, rows, cols):
        if (cols >= 1):
            return game
        half_rows = cols ** 2
        if rows > half_rows:
            return self.access_game_helper(game.get_team_two(), rows - half_rows, cols - 1)
        else:
            return self.access_game_helper(game.get_child_two(), rows, cols - 1)


