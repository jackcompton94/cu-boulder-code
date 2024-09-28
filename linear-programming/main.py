from pulp import *


# # # # # # # # # # Maximize # # # # # # # # # #
prob = LpProblem('', LpMaximize)

# Decision Variables (Integer Linear Programming because cat='Integer", 'cat' to LP Relax)
dec_vars = [LpVariable(f'x_{x}', lowBound=-15, upBound=15, cat='Integer') for x in range(1, 6)]

# Objective Function
C = [2, -3, 1]  # Coefficients
obj = lpSum([C[i] * dec_vars[i] for i in range(len(C))])

# Constraints
# x_1 - x_2 + x_3 <= 5
c1 = dec_vars[0] - dec_vars[1] + dec_vars[2] <= 5

# x_1 - x_2 + 4x_3 <= 7
c2 = dec_vars[0] - dec_vars[1] + 4 * dec_vars[2] <= 7

# x_1 + 2x_2 - x_3 + x_4 <= 14
c3 = dec_vars[0] + 2 * dec_vars[1] - dec_vars[2] + dec_vars[3] <= 14

# x_3 - x_4 + x_5 <= 7
c4 = dec_vars[2] - dec_vars[3] + dec_vars[4] <= 7

# -15 <= x1 ... x_5 <= 15
# Handled above when setting dec_vars in lowBound and upBound

# x_1 ... x_5 != decimal
# Handled above when setting dec_vars in cat='Integer'

# Add Objective Function, Constraints, and Solve
prob += obj
prob += c1
prob += c2
prob += c3
prob += c4
status = prob.solve()

if LpStatus[prob.status] == 'Optimal':
    print('Optimal Solution Found:')
    for v in prob.variables():
        print(f"{v.name} = {v.varValue}")
    print(f"Optimal Value: {value(prob.objective)}")

# # # # # # # # # # Minimize # # # # # # # # # #
prob = LpProblem('', LpMinimize)

# Decision Variables (Linear Programming because there is no cat='Integer', add 'cat='Integer'' to get ILP Solution)
dec_vars = [LpVariable(f'x_{x}', lowBound=-1, upBound=1) for x in range(1, 4)]

# Objective Function
C = [2, -3, 1]  # Coefficients
obj = lpSum([C[i] * dec_vars[i] for i in range(len(C))])

# Constraints
# x_1 - x_2 >= 0.5
c1 = dec_vars[0] - dec_vars[1] >= 0.5

# x_1 - x_2 <= 0.75
c2 = dec_vars[0] - dec_vars[1] <= 0.75

# x_2 - x_3 <= 1.25
c3 = dec_vars[1] - dec_vars[2] <= 1.25

# x_2 - x_3 >= 0.95
c4 = dec_vars[1] - dec_vars[2] >= 0.95

# -1 <= x_1 ... x_3 <= 1
# # Handled above when setting dec_vars in lowBound and upBound

# x_1 ... x_3 != decimal
# Handled above when setting dec_vars in cat='Integer'

# Add Objective Function, Constraints, and Solve
prob += obj
prob += c1
prob += c2
prob += c3
prob += c4
prob.solve()

if LpStatus[prob.status] == 'Optimal':
    print('Optimal Solution Found:')
    for v in prob.variables():
        print(f"{v.name} = {v.varValue}")
    print(f"Optimal Value: {value(prob.objective)}")
else:
    print(LpStatus[prob.status])
