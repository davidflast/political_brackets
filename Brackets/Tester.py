from Brackets.Bracket import Bracket
from Brackets import Game
from Brackets import State
from Brackets import Team

northern_conference = Bracket(4)

print northern_conference.access_game(3,2).row
print northern_conference.access_game(3,2).col
