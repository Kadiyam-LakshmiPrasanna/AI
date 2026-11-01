from itertools import product
def AND(p,q):
    return p and q
def OR(p,q):
    return p and q
def NOT(p):
    return not p
def IMPLIES(p,q):
    return (not p) or q
def BICONDITIONAL(p,q):
    return p==q
print("P Q | AND OR NOT(p) IMPLIES BICONDITIONAL")
for p,q in product([True,False],repeat=2):
    print(
        int(p),int(q),"|",
        int (AND(p,q)),
        int (OR(p,q)),
        int (NOT(p)),
        int (IMPLIES(p,q)),
        int (BICONDITIONAL(p,q))
        )
    
    
