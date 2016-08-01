import pickle

def read_state(state):
    file = "/Users/davidflast/Documents/political_brackets/Brackets/States/" + state + ".pkl"
    with open(file, "rb") as input:
        obj =  pickle.load(input)
        return obj