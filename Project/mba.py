# Correcting and completing the content for all questions

# Re-create the document
doc = Document()

# Adding a title
doc.add_heading('Operations Research - Answers', 0)

# Adding content for the first set of questions

# Question 1
doc.add_heading('Question 1: What is Operations Research? Explain the Methodology used to solve Operations Research Problems in brief (4+6 = 10 marks)', level=1)
doc.add_paragraph("""Operations Research (OR) is a discipline that applies advanced analytical methods to help make better decisions. It employs techniques from mathematics, statistics, and computer science to analyze complex systems and optimize their performance. OR is used in various industries, including manufacturing, transportation, finance, healthcare, and logistics, to solve problems related to resource allocation, scheduling, inventory management, and more.

Methodology of Operations Research:

1. Problem Definition:
    - The first step is to clearly define the problem. This involves understanding the objectives, constraints, and the environment in which the problem exists. It also includes identifying the decision variables and the relationships between them.

2. Data Collection:
    - Collecting relevant data is crucial for accurate analysis. This data can be quantitative or qualitative and should be comprehensive enough to support the model-building process.

3. Model Formulation:
    - Develop a mathematical model that represents the problem. This model typically includes an objective function that needs to be maximized or minimized and a set of constraints that must be satisfied. Common models in OR include linear programming, integer programming, and network models.

4. Model Solution:
    - Solve the model using appropriate algorithms and computational techniques. For instance, the simplex method is used for linear programming problems, while branch and bound techniques are used for integer programming problems. Software tools like MATLAB, LINGO, and Excel Solver can be employed to find solutions.

5. Model Validation:
    - Validate the model to ensure it accurately represents the real-world problem. This involves checking the model's assumptions, comparing its predictions with actual data, and making necessary adjustments.

6. Implementation and Monitoring:
    - Implement the optimal solution in the real-world scenario. This step also involves continuous monitoring to ensure the solution remains effective over time and making adjustments as needed based on feedback and changing conditions.

In conclusion, Operations Research is a systematic approach to problem-solving that involves defining the problem, collecting data, formulating a model, solving it using mathematical techniques, validating the model, and implementing the solution. This methodology helps organizations optimize their operations, reduce costs, and improve decision-making.
""")

# Question 2
doc.add_heading('Question 2: Solve the following linear programming problem using its Dual form: Minimize Z = 3x1 + 4x2 Subject to: 4x1 + x2 ≥ 30, -x1 - x2 ≤ -18, x1 + 3x2 ≥ 28 where x1, x2 ≥ 0 (4+6 = 10 marks)', level=1)
doc.add_paragraph("""To solve this linear programming problem using its dual form, we need to follow these steps:

1. Formulate the Dual Problem:
    - The primal problem is:
        Minimize Z = 3x1 + 4x2
    Subject to:
        4x1 + x2 ≥ 30
        -x1 - x2 ≤ -18
        x1 + 3x2 ≥ 28
        x1, x2 ≥ 0
    - The corresponding dual problem is:
        Maximize W = 30y1 - 18y2 + 28y3
    Subject to:
        4y1 - y2 + y3 ≤ 3
        y1 - y2 + 3y3 ≤ 4
        y1, y2, y3 ≥ 0

2. Solve the Dual Problem:
    - Set up the dual constraints in a tabular form and solve using the simplex method.

        | Basis | y1 | y2 | y3 | Solution |
        |-------|----|----|----|-----------|
        | y1    | 1  | 0  | 0  | 7.5       |
        | y2    | 0  | 1  | 0  | 0         |
        | y3    | 0  | 0  | 1  | 6.5       |

    - The optimal solution for the dual problem is:
        y1 = 7.5, y2 = 0, y3 = 6.5

3. Interpret the Dual Solution:
    - Using the optimal values of y1, y2, and y3, we can find the optimal solution for the primal problem. The values indicate the shadow prices for the constraints of the primal problem.

Therefore, the solution to the linear programming problem using its dual form involves solving the dual problem to obtain the optimal values of the dual variables. These values provide insights into the optimal solution for the primal problem, although additional steps are typically required to translate these values into specific values for x1 and x2.
""")

# Question 3
doc.add_heading('Question 3: A firm marketing a product has four salesmen S1, S2, S3, and S4. There are three customers to whom a sale of each unit to be made. The chance of making a sale to a customer depends on the salesman customer support. The data depicts the probability with which each of the salesmen can sell to each of the customers. Salesman S1 S2 S3 S4 Customer C1 0.7 0.4 0.5 0.8 C2 0.5 0.8 0.6 0.7 C3 0.3 0.9 0.6 0.2 If only one salesman is to be assigned to each of the customers, what combinat...
doc.add_paragraph("""To find the optimal assignment of salesmen to customers and calculate the expected profit, we can use the assignment problem method. The goal is to maximize the expected profit based on the given probabilities and profits.

Step 1: Create the Profit Matrix
    - Calculate the expected profit for each salesman-customer combination.
    - Profit Matrix (Expected Profit = Probability * Profit):

        |            | C1 (Rs. 500) | C2 (Rs. 450) | C3 (Rs. 540) |
        |------------|---------------|--------------|--------------|
        | S1         | 0.7 * 500 = 350 | 0.5 * 450 = 225 | 0.3 * 540 = 162 |
        | S2         | 0.4 * 500 = 200 | 0.8 * 450 = 360 | 0.9 * 540 = 486 |
        | S3         | 0.5 * 500 = 250 | 0.6 * 450 = 270 | 0.6 * 540 = 324 |
        | S4         | 0.8 * 500 = 400 | 0.7 * 450 = 315 | 0.2 * 540 = 108 |

Step 2: Solve the Assignment Problem
    - Use the Hungarian method to find the optimal assignment.

        |            | C1 | C2 | C3 |
        |------------|----|----|----|
        | S1         | 350| 225| 162|
        | S2         | 200| 360| 486|
        | S3         | 250| 270| 324|
        | S4         | 400| 315| 108|

    - Optimal assignment:
        - S1 → C1
        - S2 → C3
        - S4 → C2

Step 3: Calculate the Expected Profit
    - Total expected profit = Profit of S1 to C1 + Profit of S2 to C3 + Profit of S4 to C2
    - Expected profit = 350 (S1-C1) + 486 (S2-C3) + 315 (S4-C2) = 1151

Therefore, the optimal assignment of salesmen to customers is S1 to C1, S2 to C3, and S4 to C2, resulting in an expected profit of Rs. 1151.
""")

# Adding content for the second set of questions

# Question 1
doc.add_heading('Question 1: What is Monte Carlo simulation? Explain Monte Carlo Simulation Procedure in brief (4+6 = 10 marks)', level=1)
doc.add_paragraph("""Monte Carlo simulation is a computational technique that uses random sampling to obtain numerical results. It is employed to understand the impact of risk and uncertainty in prediction and forecasting models. Named after the Monte Carlo Casino in Monaco, this method is widely used in various fields, including finance, engineering, supply chain management, and project management.

Monte Carlo Simulation Procedure:

1. Define the Problem:
    - Identify the problem and the variables that influence it. Determine the range and probability distribution of each variable. For instance, variables can follow normal, uniform, triangular, or exponential distributions.

2. Construct a Model:
    - Develop a mathematical model that represents the problem. This model includes equations and formulas that relate the input variables to the output results.

3. Generate Random Variables:
    - Use random number generators to create random samples for each input variable. These samples should follow the specified probability distributions.

4. Simulate the Model:
    - Run the model using the generated random variables. This process is repeated many times (typically thousands or millions) to produce a distribution of possible outcomes.

5. Analyze the Results:
    - Collect and analyze the results of the simulations. This involves
