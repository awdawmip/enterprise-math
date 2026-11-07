#!/usr/bin/env python3
"""Independent compact exact R367 witness scan; full input is in R365/R366 research bundle."""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import sys

p = Path(sys.argv[1]) if len(sys.argv)>1 else Path('R365_Q345_352_FULL_COEFFICIENTS.txt')
b = p.read_bytes()
assert sha256(b).hexdigest() == '50bf1a56fabe89d4752ed71634cbb95d6c7c320d61b09aba1c501857650555a7'
rows = defaultdict(dict)
for line in b.splitlines():
    r,j,c = map(int,line.split(b','))
    assert 345<=r<=352 and 0<=j<=2*r and c>0 and j not in rows[r]
    rows[r][j] = c
assert set(rows)==set(range(345,353))
assert all(set(d)==set(range(2*r+1)) for r,d in rows.items())
t = min((Fraction(d[j]**2,d[j-1]*d[j+1]),r,j)
        for r,d in rows.items() for j in range(1,2*r))
u = min((Fraction(4*r*d[0]*d[2],(2*r-1)*d[1]**2),r,1)
        for r,d in rows.items())
assert t[1:]==(352,340) and u[1:]==(345,1)
assert 1 < t[0] < u[0]
assert all((729*d[j])**2>(731**2)*d[j-1]*d[j+1]
           for r,d in rows.items() for j in range(1,2*r))
assert all(729**2*4*r*d[0]*d[2] > 731**2*(2*r-1)*d[1]**2
           for r,d in rows.items())
A=rows[352][340]**2; B=rows[352][339]*rows[352][341]
assert t[0]==Fraction(A,B)
assert 728**2*A < 730**2*B and 729**2*A > 731**2*B
print('rows',sum(map(len,rows.values())),'Turan',sum(2*r-1 for r in rows),'ULC',len(rows))
print('T_min_r_j',t[1:],'exact_ratio_num',t[0].numerator,'exact_ratio_den',t[0].denominator)
print('U_min_r_j',u[1:],'exact_ratio_num',u[0].numerator,'exact_ratio_den',u[0].denominator)
print('R367 exact theorem: epsilon*=(sqrt(T)-1)/(sqrt(T)+1), all closed-box perturbations <=epsilon* PF2 and non-PF-infinity')
