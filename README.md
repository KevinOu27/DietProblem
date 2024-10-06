# Diet Problem Optimization

## Overview

The **Diet Problem** is a classic example of constrained optimization, first introduced by Stigler (1945) and expanded upon by Dantzig (1990). The goal is to find the minimum-cost diet that satisfies essential nutritional requirements such as caloric intake, sodium limits, and other key nutrients. This project aims to solve a personalized version of the Diet Problem using Python's `PuLP` library.

## Food Selection

I selected five prepackaged food items that are part of my regular diet. These items are:

1. **Shin Ramen**
2. **Kimchi**
3. **Eggs**
4. **Vienna Sausage**
5. **Arizona Green Tea**

The prices per serving were calculated based on the total cost and number of servings in each package. Here’s a breakdown of the price per serving for each item:

- **Shin Ramen**: $1.11 per pack (1 serving)
- **Kimchi**: $0.10 per serving (54 servings per container, $5.49 per container)
- **Eggs**: $0.42 per egg (1 serving)
- **Vienna Sausage**: $0.83 per can (1 serving)
- **Arizona Green Tea**: $0.75 per can (1 serving)

## Problem Formulation

### Objective
The objective of the Diet Problem is to minimize the total weekly food cost while meeting nutritional requirements. The decision variables represent the number of servings of each food item consumed in a week.

Let:
- \(x_1\) be the servings of **Shin Ramen**
- \(x_2\) be the servings of **Kimchi**
- \(x_3\) be the servings of **Eggs**
- \(x_4\) be the servings of **Vienna Sausage**
- \(x_5\) be the servings of **Arizona Green Tea**

The **objective function** is to minimize the total cost of the diet:

\[
\text{Minimize } C = 1.11x_1 + 0.10x_2 + 0.42x_3 + 0.83x_4 + 0.75x_5
\]

### Nutritional Constraints

The diet must meet certain nutritional requirements, including:
- **Calories**: At least 14,000 kcal per week
- **Protein**: At least 350g per week
- **Sodium**: No more than 35,000mg per week
- **Vitamin D**: At least 140mcg per week
- **Calcium**: At least 9,100mg per week
- **Iron**: At least 126mg per week
- **Potassium**: At least 32,900mg per week

These constraints are formulated as:

- **Calories**:  
  \[
  510x_1 + 10x_2 + 70x_3 + 160x_4 + 130x_5 \geq 14,000
  \]
  
- **Protein**:  
  \[
  10x_1 + 1x_2 + 6x_3 + 10x_4 + 0x_5 \geq 350
  \]

- **Sodium**:  
  \[
  1390x_1 + 180x_2 + 70x_3 + 790x_4 \leq 35,000
  \]

- **Vitamin D**:  
  \[
  0x_1 + 0x_2 + 1x_3 + 0x_4 + 0x_5 \geq 140
  \]

- **Calcium**:  
  \[
  0x_1 + 0x_2 + 30x_3 + 130x_4 + 0x_5 \geq 9,100
  \]

- **Iron**:  
  \[
  2.9x_1 + 0x_2 + 0.9x_3 + 1.1x_4 + 0x_5 \geq 126
  \]

- **Potassium**:  
  \[
  260x_1 + 74x_2 + 70x_3 + 110x_4 + 0x_5 \geq 32,900
  \]

### Variety Constraint

To ensure a more balanced diet, I added a constraint that requires **at least one serving** of each food item per week:

\[
x_1, x_2, x_3, x_4, x_5 \geq 1
\]

## Solution

After solving the linear programming problem using PuLP, the model suggested the following optimal diet:

- **Shin Ramen**: 1 serving
- **Kimchi**: 2.7358491 servings
- **Eggs**: 461.8221 servings
- **Vienna Sausage**: 1 serving
- **Arizona Green Tea**: 1 serving

The **total cost** of this diet was **\$196.63** per week.

## ChatGPT Experience

I also explored using **ChatGPT** by OpenAI to help solve the Diet Problem. ChatGPT was able to assist in formulating the problem and generating Python code with PuLP. However, the model initially had trouble with specifics, such as accurate nutritional values and assumptions, requiring me to provide detailed information. While useful for general problem setup, it required manual adjustments for customization.

The full conversation with ChatGPT and the generated code are available in this repository.

## How to Run

To replicate the solution:

1. Clone this repository:
   ```bash
   git clone <https://github.com/KevinOu27/DietProblem.git>
# DietProblem
# DietProblem
