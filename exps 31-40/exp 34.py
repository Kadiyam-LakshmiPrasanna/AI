def dpll(clauses,assignment={}):
    clauses = [[l for l in c if -l not in assignment]
                for c in clauses
                if not any(l in assignment for l in c)]
    if not clauses:
        return assignment
    if any(len(c)==0 for c in clauses):
        return None
    for clause in clauses:
        if len(clause) == 1:
            literal = clause[0]
            new_assignment = assignment.copy()
            new_assignment[abs(literal)] = literal>0
            return dpll(clauses,new_assignment)
        variable = abs(clauses[0][0])
        for value in [True,False]:
            new_assignment = assignment.copy()
            new_assignment[variable] = value
            result = dpll(clauses,new_assignment)
            if result is not None:
                return result
        return None
clauses = [[1,2],[-1,2]]
result = dpll(clauses)
if result:
    print("SAT")
    print("Assignment: ",result)
else:
    print("UNSAT")
        
