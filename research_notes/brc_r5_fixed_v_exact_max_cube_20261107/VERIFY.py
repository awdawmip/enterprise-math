"""Exact R5 fixed-v maximum four-observer LR cube: Fraction-only proof checker."""
from fractions import Fraction as Q
from itertools import product

v=Q(33,40)
r2=(Q(3,4),Q(5,4))
r3=(Q(1,2),Q(1),Q(3,2))
r4=(Q(1,10),Q(1),Q(19,10))
R=tuple(sorted(set((r2[1],)+r3+r4)))
q3=((Q(13,20),Q(1,5),Q(3,20)),(Q(1,40),Q(9,20),Q(21,40)))
q4=(
 ((Q(509,900),Q(382,900),Q(9,900)),(Q(47,180),Q(43,90),Q(47,180)),(Q(9,900),Q(382,900),Q(509,900))),
 ((Q(509,900),Q(382,900),Q(9,900)),(Q(67,162),Q(14,81),Q(67,162)),(Q(9,900),Q(382,900),Q(509,900))),
)
for i in range(2):
    assert sum(q3[i])==1 and all(p>0 for p in q3[i])
    assert sum(q3[i][j]*r3[j] for j in range(3))==r2[i]
    for j in range(3):
        assert sum(q4[i][j])==1 and all(p>0 for p in q4[i][j])
        assert sum(q4[i][j][z]*r4[z] for z in range(3))==r3[j]
V=tuple((q3[0][j]+v*q3[1][j])/2 for j in range(3))
assert V==(Q(1073,3200),Q(457,1600),Q(933,3200))
W0=(Q(161801,180000),Q(6499,18000),Q(267,80),Q(137,40))
H=Q(3747,3214400)
base_p=2+(3+5*v)/8
base_q=2+(1+v)/2
m={r:Q(0) for r in R}
m[Q(5,4)]=(1-v)/2
b={r:[Q(0)]*3 for r in R}
for j in range(3):
    m[r3[j]]+=V[j]
    b[r3[j]][j]-=1
    for i,u in enumerate((Q(1),v)):
        coef=(u/2)*q3[i][j]/V[j]
        for z in range(3):
            b[r4[z]][j]+=coef*q4[i][j][z]
assert sum(m.values())==1 and sum(r*m[r] for r in R)==1
for j in range(3):
    assert sum(b[r][j] for r in R)==0
    assert sum(r*b[r][j] for r in R)==0
coeff=[Q(9,10)*b[Q(1,10)][j]-(Q(1,2) if j==0 else 0) for j in range(3)]
assert coeff==[Q(9,1000),Q(2963,9140),Q(9,1000)]
C=Q(1,2)*V[0]+(coeff[1]-coeff[0])*V[1]
assert C==Q(412287,1600000)
D0=W0[0]+W0[1]-1
S0=W0[3]-base_q
assert D0==Q(5199,20000) and S0==Q(41,80)
assert H==(C+coeff[0]*S0-D0)/(2+coeff[0])
assert D0+2*H==C+coeff[0]*(S0-H)
a=(Q(593751,11522960),Q(-8561895,4629925328),Q(-8561895,4629925328),H,Q(-131073807,231496266400))
c=(Q(4233133879,20741328000),Q(12401321,46299253280),Q(12401321,46299253280),Q(-1249,1928640),Q(1418864,1446851665))
def witness(t):
    W=tuple(W0[k]+H*t[k] for k in range(4))
    X2=a[0]+sum(a[k+1]*t[k] for k in range(4))
    Ea=c[0]+sum(c[k+1]*t[k] for k in range(4))
    tp=W[2]-base_p
    tq=W[3]-base_q
    X0=X2+2*(tq-tp)
    X1=2*tp-tq-2*X2
    X=(X0,X1,X2)
    D=W[0]+W[1]-1
    Eb=2*D-Q(9,5)*Ea
    E1=W[1]-Ea-Eb
    E={r:Q(0) for r in R}
    E[Q(1,10)],E[Q(1,2)],E[Q(1)]=Ea,Eb,E1
    M={r:m[r]+sum(b[r][j]*X[j] for j in range(3)) for r in R}
    assert sum(M.values())==1
    assert sum(r*M[r] for r in R)==1
    assert (1-sum(r*E[r] for r in R),sum(E.values()))==W[:2]
    assert (base_p+X[0]/2+X[1]+3*X[2]/2,base_q+sum(X))==W[2:]
    return X+tuple(V[j]-X[j] for j in range(3))+(Ea,Eb,E1)+(
        M[Q(1,10)]-Ea,M[Q(1,2)]-Eb,M[Q(1)]-E1)
labels=('X0','X1','X2','V0-X0','V1-X1','V2-X2','Ea','Eb','E1','Ma-Ea','Mb-Eb','M1-E1')
mins=tuple(min(witness(tuple(map(Q,t)))[j] for t in product((-1,1),repeat=4)) for j in range(12))
assert min(mins)==0 and all(x>=0 for x in mins)
for t in product((Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)),repeat=4):
    assert min(witness(t))>=0
for t2 in (-1,1):
    slack=witness(tuple(map(Q,(1,1,t2,-1))))
    assert slack[4]==slack[9]==slack[10]==0
print('PIN','GLOBAL=a01383f825ef9d43b4b754254303298c64041568','EM=86149263e38c22292c9def1e0f69092efa1be77e')
print('FIXED_FLOW','g=u0=1','u1=33/40')
print('CENTER',*W0)
print('STAGE3_Q_MASS',*V)
print('SUPPORT_COEFFICIENTS',*coeff,'CONSTANT',C)
print('OPTIMAL_HALF_RADIUS',H,'DECIMAL',f'{float(H):.12f}')
print('PREVIOUS_HALF_RADIUS',Q(23,20000),'EXACT_RATIO',H/Q(23,20000))
for name,value in zip(labels,mins):print('MIN_16_CORNERS',name,value)
print('CERTIFIED','16 exact vertices + 625 exact rational grid targets')
print('PASS_EXACT_R5_FIXED_V_GLOBAL_LR_CUBE_OPTIMALITY')
