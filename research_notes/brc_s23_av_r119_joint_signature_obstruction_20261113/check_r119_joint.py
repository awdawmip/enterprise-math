from fractions import Fraction as Q
from itertools import product
import json

def frac(z): return z-z.numerator//z.denominator

def M(theta,t,x):
    A=Q(0)
    C=theta
    Y=frac(x+t*theta)
    return A <= Y < C

report=[]
for x in [Q(1,10), Q(1,2), Q(4,5)]:
    samples=set(Q(i,720) for i in range(1,720))
    samples.update([x, Q(1)-x])
    observed={(int(M(th,0,x)),int(M(th,1,x))) for th in samples}
    expected={(0,0),(1,1),(1,0) if x<Q(1,2) else (0,1)}
    assert observed == expected,(x,observed,expected)
    report.append({'x':str(x),'observed':sorted(list(observed)), 'missing':sorted(list(set(product([0,1],[0,1]))-observed))})
print('R119_JOINT_PASS',len(report),report)
with open('verification_r119.json','w') as f:json.dump(report,f,indent=2)
