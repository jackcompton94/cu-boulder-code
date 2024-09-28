from pulp import *


def compute_optimal_vertex_cover(n, edge_list):
    prob = LpProblem('vert_cover', LpMinimize)
    dvars = [LpVariable(f'w_{i}', cat='Binary') for i in range(1, n+1)]
    prob += lpSum(dvars)
    for (i, j) in edge_list:
        prob += dvars[i-1] + dvars[j-1] >= 1
    prob.solve(PULP_CBC_CMD(msg=False))
    vert_cover = [i+1 for i in range(n) if dvars[i].varValue > 0]
    print(vert_cover)
    return len(vert_cover)


def compute_lp_relaxation_vertex_cover(n, edge_list):
    prob = LpProblem('vert_cover', LpMinimize)
    dvars = [LpVariable(f'z_{i}', lowBound=0.0, upBound=1.0, cat='Continuous') for i in range(1, n+1)]
    prob += lpSum(dvars)
    for (i, j) in edge_list:
        prob += dvars[i-1] + dvars[j-1] >= 1
    prob.solve(PULP_CBC_CMD(msg=False))
    vert_cover = [x.varValue for x in dvars]
    print(vert_cover)
    return sum(vert_cover)