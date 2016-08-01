from Brackets.Bracket.Bracket import Bracket
from Brackets.Bracket.State import State

northern_conference = Bracket(4)

game = northern_conference.access_game(5,4)

print game.get_row()
print game.get_col()

FL = State(1,"Florida", 1, 2, 3, 4, 5, 6)
GA = State(2,"Georgia", 7, 8, 9, 10, 11, 12)
game.set_team_one(FL)
game.set_team_two(GA)

print game.get_team_one().get_name()
print game.get_team_two().get_percent_obama()