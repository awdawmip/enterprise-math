"""R5 seedless-LR improved cube: exact Fraction-only certificate, no floating proof steps."""
from fractions import Fraction as F
from itertools import product

Q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
Q4=(
 ((F(509,900),F(382,900),F(9,900)),(F(47,180),F(43,90),F(47,180)),(F(9,900),F(382,900),F(509,900))),
 ((F(509,900),F(382,900),F(9,900)),(F(67,162),F(14,81),F(67,162)),(F(9,900),F(382,900),F(509,900))),
)
R2=(F(3,4),F(5,4));R3=(F(1,2),F(1),F(3,2));R4=(F(1,10),F(1),F(19,10))
R=tuple(sorted(set((R2[1],)+R3+R4)))
VFLOW=F(1651,2000); H=F(47,40000)
W0=(F(161801,180000),F(6499,18000),F(267,80),F(137,40))
assert H>F(3747,3214400)
for i in range(2):
    assert sum(Q3[i])==1 and all(x>0 for x in Q3[i])
    assert sum(Q3[i][j]*R3[j] for j in range(3))==R2[i]
    for j in range(3):
        assert sum(Q4[i][j])==1 and all(x>0 for x in Q4[i][j])
        assert sum(Q4[i][j][z]*R4[z] for z in range(3))==R3[j]
V=tuple((Q3[0][j]+VFLOW*Q3[1][j])/2 for j in range(3))
assert V==(F(53651,160000), F(22859,80000),F(46671,160000))
BASE_P=2+(3+5*VFLOW)/8; BASE_Q=2+(1+VFLOW)/2
M0={r:F(0) for r in R}; M0[F(5,4)]=(1-VFLOW)/2
B={r:[F(0)]*3 for r in R}
for j in range(3):
    M0[R3[j]]+=V[j]
    B[R3[j]][j]-=1
    for i,u in enumerate((F(1),VFLOW)):
        share=(u/2)*Q3[i][j]/V[j]
        for z in range(3): B[R4[z]][j]+=share*Q4[i][j][z]
assert sum(M0.values())==1 and sum(r*M0[r] for r in R)==1
for j in range(3):
    assert sum(B[r][j] for r in R)==0
    assert sum(r*B[r][j] for r in R)==0

# For t in [-1,1]^4, X2 and the Q stopped declaration mass at LR=1/10.
A=(F(7611,160000), F(0),F(0), H,-H/2)
C=(F(201971,1000000),F(47,36000),F(47,36000),-F(47,72000),F(96681,100000000))
LABELS=('X0','X1','X2','V0-X0','V1-X1','V2-X2',
        'Ea','Eb','E1','M_a-Ea','M_b-Eb','M_1-E1')

def witness(t):
    assert len(t)==4 and all(-1<=z<=1 for z in t)
    w=tuple(W0[k]+H*t[k] for k in range(4))
    x2=A[0]+sum(A[k+1]*t[k] for k in range(4))
    ea=C[0]+sum(C[k+1]*t[k] for k in range(4))
    p=w[2]-BASE_P; q=w[3]-BASE_Q
    X=(x2+2*(q-p), 2*p-q-2*x2, x2)
    d=w[0]+w[1]-1
    eb=2*d-F(9,5)*ea
    e1=w[1]-ea-eb
    M={r:M0[r]+sum(B[r][j]*X[j] for j in range(3)) for r in R}
    E={r:F(0) for r in R}; E[F(1,10)]=ea; E[F(1,2)]=eb; E[F(1)]=e1
    assert sum(M.values())==1 and sum(r*M[r] for r in R)==1
    assert (sum(E.values()), 1-sum(r*E[r] for r in R))==(w[1],w[0])
    assert (BASE_P+X[0]/2+X[1]+3*X[2]/2,BASE_Q+sum(X))==w[2:]
    return X+tuple(V[j]-X[j] for j in range(3))+(ea,eb,e1)+(
        M[F(1,10)]-ea, M[F(1,2)]-eb,M[F(1)]-e1)

corners=[witness(tuple(map(F,t))) for t in product((-1,1),repeat=4)]
mins=[min(slack[k] for slack in corners) for k in range(12)]
assert all(x>=0 for x in mins)
assert mins[4]==0 and min(mins[6:])>0
for t in product((F(-1),F(-1,2),F(0),F(1,2),F(1)),repeat=4):
    assert all(s>=0 for s in witness(t))
print('FROZEN_GLOBAL_SHA','a01383f825ef9d43b4b754254303298c64041568')
print('FROZEN_EM_SHA','86149263e38c22292c9def1e0f69092efa1be77e')
print('SOURCE_PREDECESSOR','f4b6612c6bbc767fbbe37148309dd24d47f0c1a1')
print('VFLOW',VFLOW,'HALF_RADIUS',H,'CENTER',*W0)
print('STAGE3_Q_MASS',*V)
print('X2_AFFINE',*A)
print('EA_AFFINE',*C)
print('PREVIOUS_HALF_RADIUS',F(3747,3214400),'RADIUS_GAIN_RATIO',H/F(3747,3214400))
for name,value in zip(LABELS,mins):print('MIN_AT_16_VERTICES',name,value)
print('CHECKS','16 exact vertices; 625 rational interior targets; conditional LR moments; stopped mass normalization; four-observer recovery')
print('ALL_REAL_CUBE_PROOF','affine slacks nonnegative at all 16 vertices')
print('PASS_EXACT_R5_VARIABLE_V_THREE_LABEL_CUBE_47_OVER_40000')
