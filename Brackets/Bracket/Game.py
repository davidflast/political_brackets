class Game(object):
    def __init__(self, row, col, child_one, child_two):
        self.row = row
        self.col = col
        self.child_one = child_one
        self.child_two = child_two
        self.team_one = None
        self.team_two = None
        self.winner = None

    def set_team_one(self, team_one):
        self.team_one = team_one

    def set_team_two(self, team_two):
        self.team_two = team_two

    def set_winner(self, winner):
        self.winner = winner

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_child_one(self):
        return self.child_one

    def get_child_two(self):
        return self.child_two

    def get_team_one(self):
        return self.team_one

    def get_team_two(self):
        return self.team_two

    def get_winner(self):
        return self.winner