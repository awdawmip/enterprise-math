#!/usr/bin/env python3
"""PREFIX-591-R6: all-horizon exact rank-33 graded native cubic BRC module."""
from fractions import Fraction as F
from collections import defaultdict
import json
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN,edge,ACTIONS,ZERO_ROOT
assert SCIENCE_PIN=="f42f2906d77f24085c123f3ccfe9667d41caa96d"
assert len(ACTIONS)==6
EXPS=[(a,b,d-a-b) for d in range(4)
      for a in range(d+1) for b in range(d-a+1)]
assert len(EXPS)==20
EDGES=[]
for i in range(96):
    row=[]
    for act in ACTIONS:
        j,w=edge(i,act,ZERO_ROOT)
        dt=192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]
        row.append((j,dt,w[0]+w[1],w[2]+w[3]))
    EDGES.append(row)

def weighted_op(alpha,v):
    a,b,c=alpha
    return [sum((F(t**a*p0**b*p1**c)*v[j] for j,t,p0,p1 in EDGES[i]),F())
            for i in range(96)]

class Basis:
    def __init__(self):
        self.pivots={};self.vectors=[]
    def add(self,vec):
        v=[F(x) for x in vec]
        for p,r in sorted(self.pivots.items()):
            if v[p]:
                q=v[p]
                for j in range(p,96):v[j]-=q*r[j]
        p=next((j for j in range(96) if v[j]),None)
        if p is None:return False
        q=v[p]
        for j in range(p,96):v[j]/=q
        self.pivots[p]=v;self.vectors.append(v)
        return True
    def contains(self,vec):
        v=[F(x) for x in vec]
        for p,r in sorted(self.pivots.items()):
            if v[p]:
                q=v[p]
                for j in range(p,96):v[j]-=q*r[j]
        return not any(v)
    def __len__(self):return len(self.vectors)

W=[]
for d in range(4):
    space=Basis()
    if d==0:space.add([1]*96)
    else:
        for v in W[d-1].vectors:space.add(v)
        for alpha in EXPS:
            h=sum(alpha)
            if 0<h<=d:
                for v in W[d-h].vectors:space.add(weighted_op(alpha,v))
    j=0
    while j<len(space.vectors):
        space.add(weighted_op((0,0,0),space.vectors[j]))
        j+=1
    W.append(space)
assert [len(space) for space in W]==[1,13,32,33]
for d in range(4):
    for alpha in EXPS:
        if d+sum(alpha)<=3:
            assert all(W[d+sum(alpha)].contains(weighted_op(alpha,v))
                       for v in W[d].vectors)
ROWS=[0,2,4,6,7,8,10,12,14,16,18,20,22,24,28,32,34,36,38,
      42,46,48,50,52,54,56,60,64,68,72,76,80,84]
assert sorted(W[3].pivots)==ROWS
COLS=[0,21,22,23,27,29,41,42,43,47,48,49,57,59,63,67,68,69,
      71,74,75,76,83,87,88,89,94,97,98,99,103,107,108]

def integer_moments(initial,n):
    data={(initial,0,0,0):1}
    for _ in range(n):
        nxt=defaultdict(int)
        for (i,t,p0,p1),mass in data.items():
            for j,dt,x,y in EDGES[i]:
                nxt[(j,t+dt,p0+x,p1+y)]+=mass
        data=nxt
    assert sum(data.values())==6**n
    return [sum(m*t**a*p0**b*p1**c for (_,t,p0,p1),m in data.items())
            for a,b,c in EXPS]

lower=[]
for i in ROWS:
    values=[]
    for n in range(9):values.extend(integer_moments(i,n))
    lower.append([values[k] for k in COLS])

def det_mod(mat,p):
    A=[[x%p for x in row] for row in mat]
    n=len(A);det=1
    for j in range(n):
        i=next((i for i in range(j,n) if A[i][j]),None)
        if i is None:return 0
        if i!=j:A[j],A[i]=A[i],A[j];det=-det
        z=A[j][j];det=det*z%p;zin=pow(z,-1,p)
        for i in range(j+1,n):
            if A[i][j]:
                x=A[i][j]*zin%p
                for k in range(j+1,n):
                    A[i][k]=(A[i][k]-x*A[j][k])%p
                A[i][j]=0
    return det%p
assert det_mod(lower,1000003)==325742

result={
 "schema":"PREFIX591_R6_BRC_ALL_HORIZON_CUBIC_LINEAR_OBSERVER_V1",
 "status":"ALL_CHECKS_PASS",
 "science_pin":SCIENCE_PIN,"native_ports":96,"actions":6,"root":"ZERO_ROOT",
 "moment_degree_limit":3,"weighted_operators":len(EXPS),
 "exact_graded_space_dimensions":[len(s) for s in W],
 "all_length_port_function_rank":33,
 "minimal_variable_linear_statistics_for_arbitrary_start_laws":32,
 "all_length_closure_checked":True,
 "native_port_pivot_indices":ROWS,
 "finite_lower_witness_depths":[0,8],
 "finite_lower_modulus":1000003,"finite_lower_minor_mod":325742,
 "theorem_scope":"all n>=0; original zero-root native six-action BRC kernel; third-and-lower moments of T,P0,P1; arbitrary initial-port law",
 "higher_degree_and_other_roots":"OPEN"
}
print("ALL_CHECKS_PASS")
print(json.dumps(result,indent=2))
