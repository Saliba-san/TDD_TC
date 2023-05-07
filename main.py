from neighbour_structs import NeighbourStructs
from metaheuristics import GVNS

gvns = GVNS( NeighbourStructs().structs )

for i in range(5):
    solution_C = gvns.gvns(x, f_C)
    solution_E = gvns.gvns(x, f_E)
    print(f"\n\n-----------Solutions {i}--------\n\n")
    print(solution_C)
    print(solution_E)
