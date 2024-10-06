#ChatGPT assisted Code

import pulp

# Create a linear programming problem 
diet_problem = pulp.LpProblem("DietProblem", pulp.LpMinimize)

# Decision variables
x1 = pulp.LpVariable("Shin_Ramen", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Arizona_Green_Tea", lowBound=0, cat='Continuous')
x3 = pulp.LpVariable("Kimchi", lowBound=0, cat='Continuous')
x4 = pulp.LpVariable("Eggs", lowBound=0, cat='Continuous')
x5 = pulp.LpVariable("Vienna_Sausages", lowBound=0, cat='Continuous')

# Objective function
diet_problem += (1.11 * x1 + 0.75 * x2 + 0.10 * x3 + 0.42 * x4 + 0.83 * x5, "Total Cost")

# Constraints
diet_problem += (380 * x1 + 120 * x2 + 50 * x3 + 70 * x4 + 200 * x5 >= 2000, "Calories")
diet_problem += (10 * x1 + 0 * x2 + 1 * x3 + 6 * x4 + 10 * x5 >= 60, "Protein")
diet_problem += (1 * x1 + 0 * x2 + 2 * x3 + 0 * x4+ 0 * x5 >= 25, "Fiber")

# Solve the problem
diet_problem.solve()

# Print the results
print("Status:", pulp.LpStatus[diet_problem.status])
for variable in diet_problem.variables():
    print(f"{variable.name}: {variable.varValue}")

print("Total Cost: $", pulp.value(diet_problem.objective))
