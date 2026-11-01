from itertools import product
def model_check(kb,query,symbols):
    for values in product([False,True],repeat = len(symbols)):
        model = dict(zip(symbols,values))
        if kb(model) and not query(model):
            return False
    return True

def kb(model):
    return model["P"] and model["Q"]

def query(model):
    return model["P"]

symbols = ["P","Q"]
if model_check(kb,query,symbols):
    print("Query is entailed by knowledge base.")
else:
    print("Query is not enatiled by knowledge base.")
