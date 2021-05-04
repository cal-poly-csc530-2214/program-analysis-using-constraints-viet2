from z3 import *

s = Solver()

# 2nd order constraints:
#   true => I[-50/x]
#   I and x<0 => I[(y+1)/y, (x+y)/x]
#   I and x>=0 => y>0
# If I = a1*x + a2*y + a3 >= 0 or a4*x + a5*y + a6 >= 0 the 1st order
# constraints are:

x, y, a1, a2, a3, a4, a5, a6 = Ints('x y a1 a2 a3 a4 a5 a6')
constraints = [Implies(True, Or(-50*a1 + a2*y + a3 >= 0, -50*a4 + a5*y + a6 >= 0)),
               Implies(And(Or(a1*x + a2*y + a3 >= 0, a4*x + a5*y + a6 >= 0), x < 0), Or(a1*(x+y) + a2*(y+1) + a3 >= 0, a4*(x+y) + a5*(y+1) + a6 >= 0)),
               Implies(And(Or(a1*x + a2*y + a3 >= 0, a4*x + a5*y + a6 >= 0), x >= 0), y > 0)]

s.add(*constraints)
print(s.check())
