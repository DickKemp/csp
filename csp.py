
"""
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
the list of variables
the list of constraints
a mapping from each of the variables to the list of constraints that reference that variable
a mapping from each of the variables to the list of possible domain values that the variables can take

assignment is a dict from variable to value
e.g. assignment[WILSON_WALNUT_AFTER] will have value 300

search for solution is a function that looks like this

def search_for_solution(csp, assignment):
"""

# general methods

def not_all_vars_are_assigned(vars, vals):
    for v in vars:
        if v not in vals:
            return True
    return False

def all_vals_are_different(values):
    s = set()
    for v in values:
        s.add(v)
    return len(s) == len(values)

def flatten(l):
    out = []
    for item in l:
        if isinstance(item, (list)):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

def _inner_prod(x1,x2):
    return [flatten([x,y]) for x in x1 for y in x2]

def cross_prod(list_of_lists):
    if len(list_of_lists) == 0:
        return [[]]
    if len(list_of_lists) == 1:
        return [[x] for x in list_of_lists[0]]
    elif len(list_of_lists) == 2:
        return _inner_prod(list_of_lists[0], list_of_lists[1])
    else:
        return _inner_prod(list_of_lists[0], cross_prod(list_of_lists[1:]))

class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.constraints_for_variable = {}
        self.counter = 0
        self.REPORT_INTERVAL = 50000
        for v in variables:
            self.constraints_for_variable[v] = []
        for c in self.constraints:
            if c.var_list is None:
                for v in variables:
                    self.constraints_for_variable[v].append(c)      
            else:
                for v in c.var_list:
                    self.constraints_for_variable[v].append(c)

    def is_variable_consistent(self, var, assignment):
        for constraint in self.constraints_for_variable[var]:
            if not constraint.is_satisfied(assignment):
                return False
        return True

    def assignments_generator(self, constr, assignments):
        """ returns a generator of assignments based on the constraint constr provided as an argument
        all assignments returned are built on top of the assignments provided as an argument
        """
        for assignment in assignments:
            assigned_vars = list(assignment.keys())
            constraint_vars = constr.var_list
            unassigned_constraint_vars = list(set(constraint_vars) - set(assigned_vars))
            domain_val_pairs = [[(v, val) for val in self.domains[v]] for v in unassigned_constraint_vars]
            all_new_assignments = cross_prod(domain_val_pairs)
            for a in all_new_assignments:
                asn = {k:v for (k,v) in a}
                local_assignment = assignment.copy()
                local_assignment.update(asn)
                if constr.is_satisfied(local_assignment):
                    yield(local_assignment)

    def search_for_solution(self, assignment={}, interval=None):
        if len(self.variables) == len(assignment):
            return assignment
        unassigned = list(set(self.variables) - set(assignment.keys()))
        first_variable = unassigned[0]
        for value in self.domains[first_variable]:
            local_assignment = assignment.copy()
            local_assignment[first_variable] = value
            self.report(interval)
            if self.is_variable_consistent(first_variable, local_assignment):
                result = self.search_for_solution(local_assignment)
                if result is not None:
                    return result
        return None

    def report(self, interval=None):
        # report_interval = interval if interval else self.REPORT_INTERVAL  
        self.counter = self.counter + 1
        if self.counter % 50000 == 0:
            print(self.counter)

class Constraint:
    def __init__(self, constraint_fn, var_list=None):
        self.var_list = var_list
        self.constraint_fn = constraint_fn

    def is_satisfied(self, assignment):
        """ this function tests if the constraint is satisfied by the assignment provided as an argument
        If the constraint pertains to a particular set of variables (as indicated by the var_list) then we consider
        the constraint satisfied if any one of those variables is not yet assigned a value.
        Otherwise we run the constraint function to test if the assignment satisfies the constraint.
        """
        if self.var_list and not_all_vars_are_assigned(self.var_list, assignment):
            return True
        else:
            return self.constraint_fn(assignment)

