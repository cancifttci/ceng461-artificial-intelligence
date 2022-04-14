###  CAN ÇİFTÇİ - 270201080



domains = {
    'Dean'    : [6,7,8,9],
    'Ellison' : [6,7,8,9],
    'Moore'   : [6,7,8,9],
    'Quinn'   : [6,7,8,9],
    'Purple'  : [6,7,8,9],
    'Black'   : [6,7,8,9],
    'Red'     : [6,7,8,9],
    'Green'   : [6,7,8,9]
}

constraints = {
    ('Dean','Purple')   : lambda a, b : a != b,
    ('Purple','Dean')   : lambda b, a : b != a,
    ('Dean','Purple')   : lambda a, b : a == b + 2,
    ('Purple','Dean')   : lambda b, a : b + 2 == a,
    ('Ellison','Quinn') : lambda a, b : a < b,
    ('Quinn','Ellison') : lambda b, a : b > a,
    ('Green','Black')   : lambda a, b : a < b,
    ('Black','Green')   : lambda b, a : b > a,
    ('Green','Black')   : lambda a, b : a + 1 == b,
    ('Black','Green')   : lambda b, a : b == a + 1,
    ('Green','Red')     : lambda a, b : a > b,
    ('Red','Green')     : lambda b, a : b < a,
    ('Green','Red')     : lambda a, b : a == 1 + b,
    ('Red','Green')     : lambda b, a : b + 1 == a,
    ('Dean')            : lambda a    : a != 6,
    ('Dean')            : lambda a    : a != 7,
    ('Purple')          : lambda a    : a != 8,
    ('Purple')          : lambda a    : a != 9,
    ('Quinn')           : lambda a    : a != 6,
    ('Ellison')         : lambda a    : a != 9,
    ('Black')           : lambda a    : a != 6,
    ('Green')           : lambda a    : a != 9,
    ('Green')           : lambda a    : a != 6,
    ('Red')             : lambda a    : a != 9,
    ('Red','Moore')     : lambda a, b : a == 8 or a == b,
    ('Moore','Red')     : lambda b, a : b == a or 8 ==a
}

def recheck(x, y):

    is_revised = False
    x_attributes = domains[x]
    y_attributes = domains[y]
    total_cons = [
        constr for constr in constraints if constr[0] == x and constr[1] == y]
    for x in x_attributes:
        satisfies = False
        for y in y_attributes:
            for key in total_cons:
                cons_fn = constraints[key]
                if cons_fn(x, y):
                    satisfies = True
        if not satisfies:
            x_attributes.remove(x)
            is_revised = True

    return is_revised
def apply_arc_consistency(arcs):

    queue = arcs[:]
    while queue:
        (x, y) = queue.pop(0)
        revised = recheck(x, y)
        if revised:
            neighbors = [neighbor for neighbor in arcs if neighbor[1] == x]
            queue = queue + neighbors


arcs = [('Dean', 'Purple'), ('Purple', 'Dean'), ('Ellison', 'Quinn'), ('Quinn', 'Ellison'),
        ('Green', 'Black'), ('Black', 'Green'), ('Red', 'Green'), ('Green', 'Red'),
        ('Red', 'Moore'), ('Moore', 'Red')]

apply_arc_consistency(arcs)

print(domains)

