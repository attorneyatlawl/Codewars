''' Money, Money, Money


'''

def calculate_years(principal, interest, tax, desired):
    years = 0
    if principal == desired:
        return years
    while principal < desired:
        x = principal * interest
        y = x * tax
        principal = principal + x - y
        years += 1
    return years

# Apparently you could just import Math

from math import ceil, log

def calculate_years(principal, interest, tax, desired):
    if principal >= desired: return 0
    
    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
