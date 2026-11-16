"""Exact rational certificate for the R5 fixed-flow, three-label LR cube."""
from fractions import Fraction as Q
from itertools import product

q3 = ((Q(13,20), Q(1,5), Q(3,20)), (Q(1,40), Q(9,20), Q(21,40)))
q4 = (
    ((Q(509,900),Q(382,900),Q(9,900)), (Q(47,180),Q(43,90),Q(47,180)), (Q(9,900),Q(382,900),Q(509,900))),
    ((Q(509,900),Q(382,900),Q(9,900)), (Q(67,162),Q(14,81),Q(67,162)), (Q(9,900),Q(382,900),Q(509,900))),
)
r2 = (Q(3,4),Q(5,4)); r3=(Q(1,2),Q(1),Q(3,2)); r4=(Q(1,10),Q(1),Q(19,10))
R = tuple(sorted(set((Q(1),)+r2+r3+r4)))
W0 = (Q(161801,180000),Q(6499,18000),Q(267,80),Q(137,40))
v=Q(33,40); h=Q(1,1000); old=Q(145,495224)
V=tuple((q3[0][j]+v*q3[1][j])/2 for j in range(3))
assert V==(Q(1073,3200),Q(457,1600),Q(933,3200))

for i in range(2):
    assert all(p>0 for p in q3[i]) and sum(q3[i])==1
    assert sum(q3[i][j]*r3[j] for j in range(3))==r2[i]
    for j in range(3):
        assert all(p>0 for p in q4[i][j]) and sum(q4[i][j])==1
        assert sum(q4[i][j][z]*r4[z] for z in range(3))==r3[j]

# Each history with the same stopped likelihood ratio shares one declaration probability.
def witness(W):
    dp,dq,sp,sq=(W[i]-W0[i] for i in range(4))
    X2=Q(51,1000)-Q(111,70)*(dp+dq)+sp-Q(17,35)*sq
    X0=(10*v-3)/40+2*(sq-sp)+X2
    X1=(4-3*v)/4+2*sp-sq-2*X2
    X=(X0,X1,X2)
    ea=Q(51,250)+Q(23,100)*(dp+dq)-Q(5,9)*sp+Q(21,25)*sq
    D=W[0]+W[1]-1
    eb=2*D-Q(9,5)*ea
    e1=W[1]-ea-eb
    E={r:Q(0) for r in R}
    E[Q(1,10)],E[Q(1,2)],E[Q(1)]=ea,eb,e1
    M={r:Q(0) for r in R}
    M[Q(5,4)]+=(1-v)/2
    for j in range(3):
        M[r3[j]]+=V[j]-X[j]
        for i in range(2):
            xij=(Q(1) if i==0 else v)*q3[i][j]*X[j]/(2*V[j])
            for z in range(3):M[r4[z]]+=xij*q4[i][j][z]
    assert (sum(E.values()),1-sum(r*E[r] for r in R))==(W[1],W[0])
    assert (2+(3+5*v)/8+X[0]/2+X[1]+Q(3,2)*X[2],
            2+(1+v)/2+sum(X))==W[2:]
    assert sum(M.values())==1 and sum(r*M[r] for r in R)==1
    return X,E,M

# All 12 slacks are affine in (dp,dq,sp,sq); vertices certify the full real cube.
keys=['X0','X1','X2','V0-X0','V1-X1','V2-X2',
      'E_1/10','E_1/2','E_1','M_1/10-E','M_1/2-E','M_1-E']
def slacks(W):
    X,E,M=witness(W)
    return (X[0],X[1],X[2],V[0]-X[0],V[1]-X[1],V[2]-X[2],
            E[Q(1,10)],E[Q(1,2)],E[Q(1)],
            M[Q(1,10)]-E[Q(1,10)],M[Q(1,2)]-E[Q(1,2)],M[Q(1)]-E[Q(1)])
mins=[None]*12
for signs in product((-1,1),repeat=4):
    W=tuple(W0[i]+signs[i]*h for i in range(4))
    ss=slacks(W)
    for j,s in enumerate(ss):
        mins[j]=s if mins[j] is None else min(mins[j],s)
assert all(s>=0 for s in mins)
assert all(V[j]>0 for j in range(3))
for signs in product((-1,Q(-1,2),0,Q(1,2),1),repeat=4):
    W=tuple(W0[i]+signs[i]*h for i in range(4))
    assert min(slacks(W))>=0
print('FROZEN_MODEL', 'delta=1/4', 'g=u0=1','u1=33/40')
print('CUBE_CENTER', ', '.join(map(str,W0)))
print('NEW_RADIUS',h,'OLD_RADIUS',old,'GAIN',h/old)
print('MARGIN_CERTIFICATE')
for k,s in zip(keys,mins):print(k,str(s))
print('EXACT_CORNER_CHECKS',16,'EXACT_GRID_CHECKS',625)
print('PASS_EXACT_R5_FIXED_FLOW_THREE_LABEL_CUBE_1_OVER_1000')
