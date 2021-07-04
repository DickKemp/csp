
from csp import CSP
from csp import Constraint
from csp import all_vals_are_different
from csp import cross_prod
import pprint

""" each of the following symbols is used to note how many of some type of nut was held by one of the squirrels 
either before of after the robbery
e.g. WEBSTER_PECAN_BEFORE will be used to identify the number PECANS that the squirrel WEBSTER had BEFORE the robbery
These symbols are used as the keys into a dictionary where the values will be found
"""
WEBSTER_PECAN_BEFORE = 'Webster_Pecan_Before'
WEBSTER_PECAN_AFTER = 'Webster_Pecan_After'
WEBSTER_ACORN_BEFORE = 'Webster_Acorn_Before'
WEBSTER_ACORN_AFTER = 'Webster_Acorn_After'
WEBSTER_WALNUT_BEFORE = 'Webster_Walnut_Before'
WEBSTER_WALNUT_AFTER = 'Webster_Walnut_After'
WAYNE_PECAN_BEFORE = 'Wayne_Pecan_Before'
WAYNE_PECAN_AFTER = 'Wayne_Pecan_After'
WAYNE_ACORN_BEFORE = 'Wayne_Acorn_Before'
WAYNE_ACORN_AFTER = 'Wayne_Acorn_After'
WAYNE_WALNUT_BEFORE = 'Wayne_Walnut_Before'
WAYNE_WALNUT_AFTER = 'Wayne_Walnut_After'
WILMA_PECAN_BEFORE = 'Wilma_Pecan_Before'
WILMA_PECAN_AFTER = 'Wilma_Pecan_After'
WILMA_ACORN_BEFORE = 'Wilma_Acorn_Before'
WILMA_ACORN_AFTER = 'Wilma_Acorn_After'
WILMA_WALNUT_BEFORE = 'Wilma_Walnut_Before'
WILMA_WALNUT_AFTER = 'Wilma_Walnut_After'
WILSON_PECAN_BEFORE = 'Wilson_Pecan_Before'
WILSON_PECAN_AFTER = 'Wilson_Pecan_After'
WILSON_ACORN_BEFORE = 'Wilson_Acorn_Before'
WILSON_ACORN_AFTER = 'Wilson_Acorn_After'
WILSON_WALNUT_BEFORE = 'Wilson_Walnut_Before'
WILSON_WALNUT_AFTER = 'Wilson_Walnut_After'
WEEZIE_PECAN_BEFORE = 'Weezie_Pecan_Before'
WEEZIE_PECAN_AFTER = 'Weezie_Pecan_After'
WEEZIE_ACORN_BEFORE = 'Weezie_Acorn_Before'
WEEZIE_ACORN_AFTER = 'Weezie_Acorn_After'
WEEZIE_WALNUT_BEFORE = 'Weezie_Walnut_Before'
WEEZIE_WALNUT_AFTER = 'Weezie_Walnut_After'

""" the variables are split into those that hold the count of nuts held by a squirrel BEFORE the robbery
vs. those that hold the count of nuts held AFTER the robbery.
"""

# Variables before the robbery

BEFORE_ROBBERY_VARIABLES = [ 
            WEBSTER_PECAN_BEFORE,
            WEBSTER_ACORN_BEFORE,
            WEBSTER_WALNUT_BEFORE,
            WAYNE_PECAN_BEFORE,
            WAYNE_ACORN_BEFORE,
            WAYNE_WALNUT_BEFORE,
            WILMA_PECAN_BEFORE,
            WILMA_ACORN_BEFORE,
            WILMA_WALNUT_BEFORE,
            WILSON_PECAN_BEFORE,
            WILSON_ACORN_BEFORE,
            WILSON_WALNUT_BEFORE,
            WEEZIE_PECAN_BEFORE,
            WEEZIE_ACORN_BEFORE,
            WEEZIE_WALNUT_BEFORE ]

# Variables after the robbery

AFTER_ROBBERY_VARIABLES = [ 
            WEBSTER_PECAN_AFTER,
            WEBSTER_ACORN_AFTER,
            WEBSTER_WALNUT_AFTER,
            WAYNE_PECAN_AFTER,
            WAYNE_ACORN_AFTER,
            WAYNE_WALNUT_AFTER,
            WILMA_PECAN_AFTER,
            WILMA_ACORN_AFTER,
            WILMA_WALNUT_AFTER,
            WILSON_PECAN_AFTER,
            WILSON_ACORN_AFTER,
            WILSON_WALNUT_AFTER,
            WEEZIE_PECAN_AFTER,
            WEEZIE_ACORN_AFTER,
            WEEZIE_WALNUT_AFTER ]


def setup_squirrel_nut_domain():
    """ this method will initialize the domain of all the variables and return a dictionary
    mapping its variable to a list of possible domain values.

    A domain is the set of possible values that a variable can have.
    So, for example, the number of pecans that any squirrel can have before the robbery is either 350, 300, 275, 250 or 225
    It means that when we are trying to figure out how many pecans WEBSTER had before the robbery we know that it must be
    one of those five possible values from the domain.
    Each type of nut has a set of possible domains for both before and after the robbery
    PECANS_BEFORE_DOMAIN  is the possible count of pecans of any squirrel before the robbery, and 
    its values is the list [350, 300, 275, 250, 225]
    """
    # Possible domain values for the nuts both before and after the robbery
    
    PECANS_BEFORE_DOMAIN  = [350, 300, 275, 250, 225]
    PECANS_AFTER_DOMAIN   = [270, 200, 180, 160, 150]
    ACORNS_BEFORE_DOMAIN  = [500, 490, 450, 425, 400]
    ACORNS_AFTER_DOMAIN   = [430, 390, 380, 375, 350]
    WALNUTS_BEFORE_DOMAIN = [235, 215, 200, 195, 190]
    WALNUTS_AFTER_DOMAIN  = [198, 180, 175, 170, 120]

    """ we then assign each variable one of these possible domains using the squirrel_nut_domain dictionary
    E.g.  we set the domains of both WEBSTER_PECAN_BEFORE and WAYNE_PECAN_BEFORE to be the PECANS_BEFORE_DOMAIN
    """

    # Domains values for each variable
    
    squirrel_nut_domain = {}
    squirrel_nut_domain[WEBSTER_PECAN_BEFORE]  = PECANS_BEFORE_DOMAIN
    squirrel_nut_domain[WAYNE_PECAN_BEFORE]    = PECANS_BEFORE_DOMAIN
    squirrel_nut_domain[WILMA_PECAN_BEFORE]    = PECANS_BEFORE_DOMAIN
    squirrel_nut_domain[WILSON_PECAN_BEFORE]   = PECANS_BEFORE_DOMAIN
    squirrel_nut_domain[WEEZIE_PECAN_BEFORE]   = PECANS_BEFORE_DOMAIN

    squirrel_nut_domain[WEBSTER_PECAN_AFTER]   = PECANS_AFTER_DOMAIN
    squirrel_nut_domain[WAYNE_PECAN_AFTER]     = PECANS_AFTER_DOMAIN
    squirrel_nut_domain[WILMA_PECAN_AFTER]     = PECANS_AFTER_DOMAIN
    squirrel_nut_domain[WILSON_PECAN_AFTER]    = PECANS_AFTER_DOMAIN
    squirrel_nut_domain[WEEZIE_PECAN_AFTER]    = PECANS_AFTER_DOMAIN

    squirrel_nut_domain[WEBSTER_ACORN_BEFORE]  = ACORNS_BEFORE_DOMAIN
    squirrel_nut_domain[WAYNE_ACORN_BEFORE]    = ACORNS_BEFORE_DOMAIN
    squirrel_nut_domain[WILMA_ACORN_BEFORE]    = ACORNS_BEFORE_DOMAIN
    squirrel_nut_domain[WILSON_ACORN_BEFORE]   = ACORNS_BEFORE_DOMAIN
    squirrel_nut_domain[WEEZIE_ACORN_BEFORE]   = ACORNS_BEFORE_DOMAIN

    squirrel_nut_domain[WEBSTER_ACORN_AFTER]   = ACORNS_AFTER_DOMAIN
    squirrel_nut_domain[WAYNE_ACORN_AFTER]     = ACORNS_AFTER_DOMAIN
    squirrel_nut_domain[WILMA_ACORN_AFTER]     = ACORNS_AFTER_DOMAIN
    squirrel_nut_domain[WILSON_ACORN_AFTER]    = ACORNS_AFTER_DOMAIN
    squirrel_nut_domain[WEEZIE_ACORN_AFTER]    = ACORNS_AFTER_DOMAIN

    squirrel_nut_domain[WEBSTER_WALNUT_BEFORE] = WALNUTS_BEFORE_DOMAIN
    squirrel_nut_domain[WAYNE_WALNUT_BEFORE]   = WALNUTS_BEFORE_DOMAIN
    squirrel_nut_domain[WILMA_WALNUT_BEFORE]   = WALNUTS_BEFORE_DOMAIN
    squirrel_nut_domain[WILSON_WALNUT_BEFORE]  = WALNUTS_BEFORE_DOMAIN
    squirrel_nut_domain[WEEZIE_WALNUT_BEFORE]  = WALNUTS_BEFORE_DOMAIN

    squirrel_nut_domain[WEBSTER_WALNUT_AFTER]  = WALNUTS_AFTER_DOMAIN
    squirrel_nut_domain[WAYNE_WALNUT_AFTER]    = WALNUTS_AFTER_DOMAIN
    squirrel_nut_domain[WILMA_WALNUT_AFTER]    = WALNUTS_AFTER_DOMAIN
    squirrel_nut_domain[WILSON_WALNUT_AFTER]   = WALNUTS_AFTER_DOMAIN
    squirrel_nut_domain[WEEZIE_WALNUT_AFTER]   = WALNUTS_AFTER_DOMAIN

    return squirrel_nut_domain


def setup_squirrel_nut_constraints():
    """ this method wil set up the constraints between variables and will return the constraints as
    a list of contraints, where each constraint is an instance of the Constraint class.
    The Constraint instance holds: 
    (1) a function that accepts one parameter which is a set of assignments, and the function returns True if 
    the assignments satisfy the constraints, and
    (2) the list of variables that the constraint is testing
    """
    constraints = []

    # Constraint #0
    # this constraint tests to confirm that the value of each variables before the robbery is unique, and also that the
    # value of each variable after the robbery is unique

    def constraint_0(val):
        vs = [AFTER_ROBBERY_VARIABLES, BEFORE_ROBBERY_VARIABLES]
        for s in vs:
            vals = []
            for v in s:
                if v in val:
                    vals.append(v)
            if len(vals) != len(set(vals)):
                return False
        return True
    constraints.append( Constraint(constraint_0) )

    # Constraint #1
    # tests to confirm that the count of PECANS held by WEBSTER BEFORE plus the count of PECANS help by WAYNE BEFORE equals 650
    x = lambda val : val[WEBSTER_PECAN_BEFORE] + val[WAYNE_PECAN_BEFORE] == 650
    constraints.append( Constraint(x, [WEBSTER_PECAN_BEFORE, WAYNE_PECAN_BEFORE]))
    
    # constratin #2
    # another sum total constraint
    x = lambda val : val[WEBSTER_ACORN_BEFORE] + val[WAYNE_ACORN_BEFORE] == 825
    constraints.append( Constraint(x, [WEBSTER_ACORN_BEFORE, WAYNE_ACORN_BEFORE]))

    # constratin #3
    # another sum total constraint
    x = lambda val : val[WEBSTER_WALNUT_BEFORE] + val[WAYNE_WALNUT_BEFORE] == 435
    constraints.append( Constraint(x, [WEBSTER_WALNUT_BEFORE, WAYNE_WALNUT_BEFORE] ))

    # Constraint #4
    x = lambda val : val[WEBSTER_PECAN_BEFORE] + val[WAYNE_PECAN_BEFORE] == val[WEBSTER_PECAN_AFTER] + val[WAYNE_PECAN_AFTER] + 180
    constraints.append( Constraint(x, [WEBSTER_PECAN_BEFORE, WAYNE_PECAN_BEFORE, WEBSTER_PECAN_AFTER, WAYNE_PECAN_AFTER] ))

    # Constraint #5    
    x = lambda val : val[WEBSTER_ACORN_BEFORE] + val[WAYNE_ACORN_BEFORE] == val[WEBSTER_ACORN_AFTER] + val[WAYNE_ACORN_AFTER] + 100
    constraints.append( Constraint(x, [WEBSTER_ACORN_BEFORE, WAYNE_ACORN_BEFORE, WEBSTER_ACORN_AFTER, WAYNE_ACORN_AFTER] ))

    # Constraint #6
    x = lambda val : val[WEBSTER_WALNUT_BEFORE] + val[WAYNE_WALNUT_BEFORE] == val[WEBSTER_WALNUT_AFTER] + val[WAYNE_WALNUT_AFTER] + 57
    constraints.append( Constraint(x, [WEBSTER_WALNUT_BEFORE, WAYNE_WALNUT_BEFORE, WEBSTER_WALNUT_AFTER, WAYNE_WALNUT_AFTER] ))

    # Constraint #7
    x = lambda val : val[WILSON_PECAN_BEFORE] + 50 ==  val[WEBSTER_PECAN_BEFORE]
    constraints.append( Constraint(x, [WEBSTER_PECAN_BEFORE, WILSON_PECAN_BEFORE]))

    # Constraint #8
    x = lambda val : val[WILMA_PECAN_BEFORE] + 125 ==  val[WAYNE_PECAN_BEFORE]
    constraints.append( Constraint(x, [WILMA_PECAN_BEFORE, WAYNE_PECAN_BEFORE]))
    
    # Constraint #9
    x = lambda val : val[WAYNE_PECAN_AFTER] ==  val[WEEZIE_PECAN_AFTER] + 20
    constraints.append( Constraint(x, [WAYNE_PECAN_AFTER, WEEZIE_PECAN_AFTER]))
    
    # Constraint #10
    x = lambda val : val[WEEZIE_PECAN_AFTER] == val[WILSON_PECAN_AFTER] + 20
    constraints.append( Constraint(x, [WEEZIE_PECAN_AFTER, WILSON_PECAN_AFTER]))
    
    # Constraint #11
    x = lambda val : val[WILSON_ACORN_BEFORE] >  val[WEEZIE_ACORN_BEFORE]
    constraints.append( Constraint(x, [WILSON_ACORN_BEFORE, WEEZIE_ACORN_BEFORE]))

    # Constraint #12
    x = lambda val : val[WEEZIE_ACORN_BEFORE] > val[WILMA_ACORN_BEFORE]
    constraints.append( Constraint(x, [WEEZIE_ACORN_BEFORE, WILMA_ACORN_BEFORE]))

    # Constraint #13
    x = lambda val :  val[WAYNE_ACORN_BEFORE]  == (val[WILSON_ACORN_BEFORE] * 4/5)
    constraints.append( Constraint(x, [WAYNE_ACORN_BEFORE, WILSON_ACORN_BEFORE]))

    # Constraint #14
    x = lambda val : val[WEEZIE_ACORN_AFTER] ==  val[WAYNE_ACORN_AFTER] + 30
    constraints.append( Constraint(x, [WEEZIE_ACORN_AFTER, WAYNE_ACORN_AFTER]))

    # Constraint #15
    x = lambda val : val[WILSON_ACORN_AFTER] == val[WEBSTER_ACORN_AFTER] + 15
    constraints.append( Constraint(x, [WILSON_ACORN_AFTER, WEBSTER_ACORN_AFTER]))

    # Constraint #16
    x = lambda val : val[WAYNE_WALNUT_AFTER] + 2 == val[WAYNE_WALNUT_BEFORE]
    constraints.append( Constraint(x, [WAYNE_WALNUT_AFTER, WAYNE_WALNUT_BEFORE]))

    # Constraint #17
    x = lambda val : val[WEEZIE_WALNUT_AFTER] + 70 == val[WEEZIE_WALNUT_BEFORE]
    constraints.append( Constraint(x, [WEEZIE_WALNUT_AFTER, WEEZIE_WALNUT_BEFORE]))

    # Constraint #18
    x = lambda val : val[WILSON_WALNUT_AFTER] + 20 == val[WILSON_WALNUT_BEFORE]
    constraints.append( Constraint(x, [WILSON_WALNUT_AFTER, WILSON_WALNUT_BEFORE]))
    return constraints

def squirrel_nut_search_brute_force(): 
    """executes a full brute force search of the entire search space of possible 
    combinations

    Returns:
        dict: the assignments of values to the variables reprsenting the solution
    """
    variables = BEFORE_ROBBERY_VARIABLES + AFTER_ROBBERY_VARIABLES
    domain = setup_squirrel_nut_domain()
    constraints = setup_squirrel_nut_constraints()
    csp = CSP(variables, domain, constraints)
    solution = csp.search_for_solution()
    return solution

def merge_list_of_maps(list_of_maps):
    combined = {}
    for amap in list_of_maps:
        combined.update(amap)
    return combined

def squirrel_nut_optimized_search(): 
    """is an optimized search that considers how certain constraints only have an impact on a subset of
    the variables.   We define the set of constraint groups, where each constraint group contains those 
    constraints that are connected by virtue of them each impacting the same variable.
    So, for example, constraint 6 is in the same group as constraint 3, because they each constrain the 
    common variables WEBSTER_WALNUT_BEFORE and WAYNE_WALNUT_BEFORE.  
    Similarly, constraint 16 is also in the same group because it too also constrains the varaible WAYNE_WALNUT_BEFORE.

    constraint #18 is in a group by itself, because it contrains the variables WILSON_WALNUT_AFTER and 
    WILSON_WALNUT_BEFORE, and there are no other constraints that also constrain those two variables.

    Returns:
        dict: the assignments of values to the variables reprsenting the solution
    """
    variables = BEFORE_ROBBERY_VARIABLES + AFTER_ROBBERY_VARIABLES
    domain = setup_squirrel_nut_domain()
    constraints = setup_squirrel_nut_constraints()
    csp = CSP(variables, domain, constraints)

    constraint_groups = []
    constraint_groups.append([5,2,14,15,13,11,12])
    constraint_groups.append([6,3,16])
    constraint_groups.append([4,1,7,8,9,10])
    constraint_groups.append([17])
    constraint_groups.append([18])

    all_group_assignments = []
    for constr_group in constraint_groups:
        assignments_list = [{}]
        for constraint in constr_group:
            assignments = csp.assignments_generator(constraints[constraint], assignments_list)
            assignments_list = list(assignments)
        all_group_assignments.append(assignments_list)
    combined_assignments = cross_prod(all_group_assignments)
    for combination in combined_assignments:
        combined_assignment = merge_list_of_maps(combination)
        solution = csp.search_for_solution(combined_assignment)
        if solution:
            return solution
    return "no solution"

if __name__ == '__main__':
    solution = squirrel_nut_optimized_search()
    pprint.pprint(solution)

