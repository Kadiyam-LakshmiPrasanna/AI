statements = {
    "All students study AI" : "Ɐx(student(x)->studies(x,AI))",
    "some student uses a laptop" : "ⱻx(student(x)^uses(x,laptop))",
    "Every student has a mentor" : "Ɐx(student(x)->HasMentor(x,Mentor(x)))"
    }
for statement,fol in statements.items():
    print(statement)
    print("FOL: ",fol)
    print()
