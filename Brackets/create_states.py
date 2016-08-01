import csv
from Brackets.Bracket.State import State
from Brackets.ReadState import read_state




with open('/Users/davidflast/Documents/political_brackets/Brackets/stateData', 'rb') as csvfile:
    state_reader = csv.reader(csvfile, delimiter = ",", quotechar = "|")
    parsed = ((row[0],row[1],int(row[2]),int(row[3]),int(row[4]), int(row[5]),int(row[6]), int(row[7]))
              for row in state_reader)
    print parsed

    for row in parsed:
        abb = row[0]
        name = row[1]
        electoral = row[2]
        obama = row[3]
        romney = row[4]
        white = row[5]
        hispanic = row[6]
        black = row[7]
        print abb
        state = State(abb,name, electoral, obama, romney, white, hispanic, black)
        state.write_state()

    AK = read_state('AK')
    print AK.get_name()