from cuckoo_main import CuckooProblem
from functions import FUNCTIONS

problem = CuckooProblem(function=FUNCTIONS['michalewicz'], nests=15, upper_boundary=4, lower_boundary=0, alpha=1,
                        max_generations=10, p_a=0.25)
best_nest = problem.solve()
problem.replay()
