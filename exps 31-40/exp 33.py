def resolve(c1,c2):
    resolvents = []
    for literal in c1:
        opposite = -literal
        if opposite in c2:
            new_clause = (c1-{literal}) | (c2-{opposite})
            resolvents.append(new_clause)
    return resolvents
clauses = [
    {-1,2},
    {1},
    {-2}
    ]
print("Initial clauses: ",clauses)
new1 = resolve(clauses[0],clauses[1])[0]
print("Resolve (~P or Q) with P: ",new1)

new2 = resolve(new1,clauses[2])[0]
print("Resolve Q with ~Q: ",new2)

if len(new2)==0:
    print("Empty clause derived.")
    print("Contradiction found:Query Q is entailed.")
