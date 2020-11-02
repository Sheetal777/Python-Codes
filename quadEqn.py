# Wayyy too short

import cmath

a = 1
b = 5
c = 6

# Disc
d = (b**2) - (4*a*c)

# solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('Solutions are {0} and {1}'.format(sol1,sol2))
