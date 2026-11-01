def unify(expr1,expr2,substitution=None):
    if substitution is None:
        substitution = {}
    if expr1 == expr2:
        return substitution
    if isinstance(expr1,str) and expr1.islower():
        substitution[expr1] = expr2
        return substitution
    if isinstance(expr2,str) and expr2.islower():
        substitution[expr2] = expr1
        return substitution
    if isinstance(expr1,tuple) and isinstance(expr2,tuple):
        if expr1[0] != expr2[0] or len(expr1) != len(expr2):
            return None
        for a,b in zip(expr1[1:],expr2[1:]):
            substitution = unify(a,b,substitution)
            if substitution is None:
                return None
        return substitution
expr1 = ("knows","x","AI")
expr2 = ("knows","john","y")
result = unify(expr1,expr2)
print("Expression 1: ",expr1)
print("Expression 2: ",expr2)
print("Substitution: ",result)
