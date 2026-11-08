"""Exact n=1,2 stationary-start native BRC paired-mass third cumulants."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, ZERO_ROOT, ACTIONS, edge
import json
assert SCIENCE_PIN=="f42f2906d77f24085c123f3ccfe9667d41caa96d"
E=[]
for i in range(96):
    row=[]
    for a in ACTIONS:
        j,w=edge(i,a,ZERO_ROOT)
        h=64*w[6]-3*w[0]-w[1]-3*w[2]-w[3]
        p=(w[0]+w[1],w[2]+w[3],w[4]+w[5])
        assert sum(p)==1 and all(v in (0,1) for v in p)
        row.append((j,h,p))
    E.append(row)
assert sum(map(len,E))==576
atoms=Counter((h,p) for row in E for (j,h,p) in row)
assert atoms=={(-3,(1,0,0)):93,(-1,(1,0,0)):96,(61,(1,0,0)):3,
               (-3,(0,1,0)):96,(-1,(0,1,0)):96,(0,(0,0,1)):192}
assert sum(n*h for (h,p),n in atoms.items())==-576
assert [sum(n*h*p[j] for (h,p),n in atoms.items()) for j in range(3)]==[-192,-384,0]
def exact_cumulant(a,b,n):
    V=[[0]*96 for _ in range(8)]
    V[0]=[1]*96
    for step in range(n):
        W=[[0]*96 for _ in range(8)]
        for i,row in enumerate(E):
            for j,h,p in row:
                rewards=(h,p[a],p[b])
                for mask in range(8):
                    sub=mask
                    while True:
                        rem=mask^sub
                        fac=1
                        for k in range(3):
                            if (rem>>k)&1: fac*=rewards[k]
                        W[mask][j]+=fac*V[sub][i]
                        if sub==0: break
                        sub=(sub-1)&mask
        V=W
    m=[Q(sum(row),96*6**n) for row in V]
    return (m[7]-m[3]*m[4]-m[5]*m[2]-m[6]*m[1]
            +2*m[1]*m[2]*m[4])/64
A=[[0,1,-1],[1,-1,0],[-1,0,1]]
def calc(n):
    X=[[Q(0)]*3 for _ in range(3)]
    for i,j in combinations_with_replacement(range(3),2):
        X[i][j]=X[j][i]=exact_cumulant(i,j,n)
    return X
assert calc(1)==[[Q(a,576) for a in row] for row in A]
assert calc(2)==[[-Q(a,864) for a in row] for row in A]
assert all(sum(row)==0 for row in calc(1))
assert all(sum(row)==0 for row in calc(2))
print("ALL_CHECKS_PASS")
