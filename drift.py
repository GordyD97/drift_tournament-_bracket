from pprint import pprint
from bracketool.single_elimination import SingleEliminationGen
from bracketool.domain import *

se = SingleEliminationGen(
    use_three_way_final=False,
    third_place_clash=True,
    use_rating=True,
    random_seed=42)

# this would be the exact scenario for a thursday night battle first state hobbies. 

clist = [
    competitor("Acomp", "2435")
    competitor("Bcomp", "3245")
    competitor("Ccomp", "6789")
    competitor("Dcomp", "2345")
    competitor("Ecomp", "6587")
    competitor("Fcomp", "5466")
]

output = se.generate(clist)

pprint(output.rounds[0])


# example code from package repo. 


