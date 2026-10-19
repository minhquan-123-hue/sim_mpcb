#sim human bio system v.0

def cells(first_cell):
    while first_cell != 1000000:
        first_cell *= 2

    tissue = first_cell
    tissue = 1
    return tissue

def tissues(tissue):
    while tissue != 1000000:
        tissue *= 2
        
    organ = tissue
    organ = 1
    return organ

def organs(organ):
    while organ != 20:
        organ += 1
        
    human = organ
    human = 1
    return human