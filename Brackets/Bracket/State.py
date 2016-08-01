from Brackets.Bracket.Team import Team
import pickle


class State(Team):
    # Holds data about individual state for people to look up
    def __init__(self, abb, name, electoral_votes, percent_obama, percent_romney, percent_white, percent_hispanic, percent_black):
        self.abb = abb
        self.name = name
        self.electoral_votes = electoral_votes
        self.percent_obama = percent_obama
        self.percent_romney = percent_romney
        self.percent_white = percent_white
        self.percent_hispanic = percent_hispanic
        self.percent_black = percent_black

    def write_state(self):
        path = "/Users/davidflast/Documents/political_brackets/Brackets/States/%s%s" %(self.abb, ".pkl")
        with open(path, "wb") as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
    def __str__(self):
        string = (self.abb + self.name + str(self.electoral_votes) + str(self.percent_obama) +
        str(self.percent_romney) + str(self.percent_white) + str(self.percent_hispanic) + str(self.percent_black))
        return string
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