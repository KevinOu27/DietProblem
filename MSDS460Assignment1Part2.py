import pulp

#Creating the Linear Programming Problem
lp_problem = pulp.LpProblem("Diet_Optimization", pulp.LpMinimize)

#Decision variables: servings of each item
food_items = ['Shin Ramen', 'Kimchi', 'Eggs', 'Vienna Sausage', 'Arizona Green Tea']
costs = [1.11, 5.49 / 54, 0.42, 0.83, 0.75] #Prices based on what I purchase them for usually at local Costco
servings = pulp.LpVariable.dicts("Servings", food_items, lowBound=0, cat='Continuous')

#Nutrition data from label (per serving)
calories = [510, 10, 70, 160, 130]
protein = [10, 1, 6, 10, 0]
sodium = [1390, 180, 70, 790, 0]
vitamin_d = [0, 0, 1, 0, 0]
calcium = [0, 0, 30, 130, 0]
iron = [2.9, 0, 0.9, 1.1, 0]
potassium = [260, 74, 70, 110, 0]

#Weekly requirements (7 day totals)
min_calories = 7 * 2000
min_protein = 7 * 50
max_sodium = 7 * 5000
min_vitamin_d = 7 * 20
min_calcium = 7 * 1300
min_iron = 7 * 18
min_potassium = 7 * 4700

#Objective function: minimizing cost
lp_problem += pulp.lpSum([costs[i] * servings[food_items[i]] for i in range(len(food_items))]), "Total Cost"

# Constraints

#Calories constraint (minimum)
lp_problem += pulp.lpSum([calories[i] * servings[food_items[i]] for i in range(len(food_items))]) >= min_calories, "MinCalories"

#Protein constraint (minimum)
lp_problem += pulp.lpSum([protein[i] * servings[food_items[i]] for i in range(len(food_items))]) >= min_protein, "MinProtein"

#Sodium constraint (maximum)
lp_problem += pulp.lpSum([sodium[i] * servings[food_items[i]] for i in range(len(food_items))]) <= max_sodium, "MaxSodium"

#Vitamin D constraint (minimum)
lp_problem += pulp.lpSum([vitamin_d[i] * servings[food_items[i]] for i in range(len(food_items))]) >= min_vitamin_d, "MinVitaminD"

#Calcium constraint (minimum)
lp_problem += pulp.lpSum([calcium[i] * servings[food_items[i]] for i in range(len(food_items))]) >= min_calcium, "MinCalcium"

#Iron constraint (minimum)
lp_problem += pulp.lpSum([iron[i] * servings[food_items[i]] for i in range(len(food_items))]) >= min_iron, "MinIron"

#Potassium constraint (minimum)
lp_problem += pulp.lpSum([potassium[i] * servings[food_items[i]] for i in range(len(food_items))]) >= min_potassium, "MinPotassium"

for item in food_items:
    lp_problem += servings[item] >= 1, f"Min_One_Serving_{item}"


lp_problem.solve()

#Results
print(f"Status: {pulp.LpStatus[lp_problem.status]}")
for v in lp_problem.variables():
    print(f"{v.name} = {v.varValue}")

#Total cost
print(f"Total Cost of the Diet: ${pulp.value(lp_problem.objective):.2f}")

#Outputting the results to a plain text file
with open('/Users/kevinou/Desktop/Grad/Projects/MSDS460Assignment1/diet_problem_outputminconstraint.txt', 'w') as f:
    f.write(f"Status: {pulp.LpStatus[lp_problem.status]}\n")
    for v in lp_problem.variables():
        f.write(f"{v.name} = {v.varValue}\n")
    f.write(f"Total Cost of the Diet: ${pulp.value(lp_problem.objective):.2f}\n")
