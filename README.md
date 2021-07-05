# Constraint Satisfaction Problem (CSP) framework

Solves the Squirrel nut perplexor using a constraint satisfaction framework

The logic is something like this:
we have a list of variables that we would like to assign values to
we also have an "assignment", which maps each of some subset of variables to a specific value
we start with an empty assignment, namely no variable is yet assigned a value

we call a function "search_for_solution" that we will pass in an assignment, which initially will be the empty assignment
if the assignment which has been passed in is fully assigned, then the function will return that assignement, as it a solution

the function will compare the list of variables that have been assigned values to the complete list of variables to identify
the list of variables which have yet to be assigned.

then it will pick the first unassigned variable and then go in a loop assigning it each time to one of its possible domain values
it then checks to see if this newly assigned variable is consistent with all of the constraints that the variable impacts, 
and if it is consistent, it will update the assignment with the new var/val and then recursively call the search_for_solutions function
it captures the return values from the recursive call, and if it is not None, then it will return that soluton

a constraint will be a function that takes an assignment and will return True or False depending on whether or 
not the assignment is consistent with the constraint
if all of the variables of the constraint are assigned values, then the constraint just uses those values to check for consistency with the constraint
if there are variables in the constraint which are not yet assigned values, then we default to just saying that the constraint is satisfied, 
for the reason that we can't yet say that it is not violated

we should have an object called CSP that holds the information about this problem, including:
1. the list of variables
2. the list of constraints
3. a mapping from each of the variables to the list of constraints that reference that variable
4. a mapping from each of the variables to the list of possible domain values that the variables can take

an assignment is a dict from variable to value
e.g. assignment[WILSON_WALNUT_AFTER] will have value 300

To use the framework to search for a solution, you need to specify 
1. varialbles:  a list of the variables
2. domain: a disctionary that maps each variable to its list of domain values
3. constraints: a list of the constraints

With that you can search for a solution as follows:

    csp = CSP(variables, domain, constraints)
    solution = csp.search_for_solution()

the return value will be the assignment, which is a dictionary that assigns a value to each of the variables.

below is the solution for Squirrels & Nuts:

    {'Wayne_Acorn_After': 350, 
    'Wayne_Acorn_Before': 400,
    'Wayne_Pecan_After': 200, 
    'Wayne_Pecan_Before': 350,
    'Wayne_Walnut_After': 198,
    'Wayne_Walnut_Before': 200,
    'Webster_Acorn_After': 375,
    'Webster_Acorn_Before': 425,
    'Webster_Pecan_After': 270,
    'Webster_Pecan_Before': 300,
    'Webster_Walnut_After': 180,
    'Webster_Walnut_Before': 235,
    'Weezie_Acorn_After': 380,
    'Weezie_Acorn_Before': 490,
    'Weezie_Pecan_After': 180,
    'Weezie_Pecan_Before': 350,
    'Weezie_Walnut_After': 120,
    'Weezie_Walnut_Before': 190,
    'Wilma_Acorn_After': 430,
    'Wilma_Acorn_Before': 450,
    'Wilma_Pecan_After': 270,
    'Wilma_Pecan_Before': 225,
    'Wilma_Walnut_After': 198,
    'Wilma_Walnut_Before': 235,
    'Wilson_Acorn_After': 390,
    'Wilson_Acorn_Before': 500,
    'Wilson_Pecan_After': 160,
    'Wilson_Pecan_Before': 250,
    'Wilson_Walnut_After': 180,
    'Wilson_Walnut_Before': 200}
