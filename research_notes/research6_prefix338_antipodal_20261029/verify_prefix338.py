#!/usr/bin/env python3
"""Exact PREFIX338 checker. Reuses PREFIX336 six certified root boxes, not re-proving their completeness."""
from fractions import Fraction as F
from itertools import product
C = [[F(s) for s in row] for row in [
['-9.872155986','-0.497496459','0.991123454','-1.977834057','3.013046410'],
['-9.851679166','0.672017894','0.997408380','1.897396211','3.094999288'],
['-6.837934178','6.406340759','1.820539644','1.328370101','4.317624519'],
['3.972277190','-3.655156020','5.069231734','1.852070781','7.206948698'],
['3.826943394','0.866306597','5.391314313','-1.020335300','8.029290029'],
['3.472972568','1.984555753','5.333493587','0.744208408','8.062257748']]]
rho, lam, L = F(1,10**8), F(10,61), F(1062562,458329)
A = [[(4,0),(4,0),(0,0)],[(0,0),(-4,0),(4,0)],
     [(-5,3),(0,0),(-3,1)],[(-2,-2),(4,4),(2,2)],
     [(-2,0),(0,0),(5,2)]]
a = [(4,0),(5,-2),(7,-4)]
b = [1360,128,2330,1864,1261]
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
for j,row in enumerate(A):
    z=[mul(x,y) for x,y in zip(row,a)]
    pairs=[mul(z[k],conj(z[l])) for k,l in product(range(3),repeat=2)]
    assert len(pairs)==9 and sum(w[0] for w in pairs)==b[j]
    assert sum(w[1] for w in pairs)==0
q=[lam**2*F(x,64) for x in b]
assert all(F(0)<x<1 for x in q) and q[2]>F(1,4)
bounds=[]
for row in C:
    center=sum(x*x for x in row)
    error=2*rho*sum(abs(x) for x in row)
    bounds.append((lam**2*(center-error),lam**2*(center+error+5*rho*rho)))
assert all(bounds[1][0]>bounds[j][1] for j in range(6) if j!=1)
lo,hi=bounds[1]
assert F(3001374538,10**9)<lo<hi<F(3001374556,10**9)
assert F(3001374538,10**9)>L
# Analytic lemma, not a numeric test: align (Ua)_3 to be real;
# then both +/- phase choices have Im port3=0, hence error=1/2.
# Every other coordinate error <=sqrt(qj)<1.
# Their pairwise distance forces radius^2>=||a||^2+||center||^2.
print('PASS_AUTHOR_SIDE_EXACT_RATIONAL_CONDITIONAL_ON_PREFIX336')
print('45 ordered BRC pairs; 6 boxes; unique maximum box 2')
print('3001374538/10^9 < MEB2 < 3001374556/10^9; MEB2>L')
