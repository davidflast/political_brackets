from Brackets.Team import Team


class State(Team):
    # Holds data about individual state for people to look up
    def __init__(self, name, electoral_votes, percent_obama, percent_romney, percent_white, percent_hispanic, percent_black):
        self.name = name
        self.electoral_votes = electoral_votes
        self.percent_obama = percent_obama
        self.percent_romney = percent_romney
        self.percent_white = percent_white
        self.percent_hispanic = percent_hispanic
        self.percent_black = percent_black

    def get_electoral_votes(self):
        return self.electoral_votes

    def get_percent_obama(self):
        return self.percent_obama

    def get_percent_romney(self):
        return self.percent_romney

    def get_percent_white(self):
        return self.percent_white

    def get_percent_hispanic(self):
        return self.percent_hispanic

    def get_percent_black(self):
        return self.percent_black