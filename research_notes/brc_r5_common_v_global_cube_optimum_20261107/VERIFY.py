"""Exact rational certificate for R5 common-v seedless-LR cube optimum.

Mathematical all-real claim follows from two affine support bounds and
16-vertex nonnegative affine slacks. Supplementary rational grid is diagnostic.
"""
from fractions import Fraction as F
from itertools import product

Q3 = ((F(13,20),F(1,5),F(3,20)), (F(1,40),F(9,20),F(21,40)))
Q4 = (
    ((F(509,900),F(382,900),F(9,900)), (F(47,180),F(43,90),F(47,180)), (F(9,900),F(382,900),F(509,900))),
    ((F(509,900),F(382,900),F(9,900)), (F(67,162),F(14,81),F(67,162)), (F(9,900),F(382,900),F(509,900))),
)
R2=(F(3,4),F(5,4)); R3=(F(1,2),F(1),F(3,2)); R4=(F(1,10),F(1),F(19,10))
R=tuple(sorted(set((R2[1],)+R3+R4)))
W0=(F(161801,180000),F(6499,18000),F(267,80),F(137,40))
VFLOW=F(17741,21497)
H=F(3543,3009580)
LAST_H=F(47,40000)
assert H>LAST_H and H/LAST_H==F(7086000,7072513)
for i in range(2):
    assert sum(Q3[i])==1 and all(z>0 for z in Q3[i])
    assert sum(Q3[i][j]*R3[j] for j in range(3))==R2[i]
    for j in range(3):
        assert sum(Q4[i][j])==1 and all(z>0 for z in Q4[i][j])
        assert sum(Q4[i][j][z]*R4[z] for z in range(3))==R3[j]


def upper_functions(v):
    """Affine universal corner bounds for every feasible centered common-v cube.

    The support proof assumes v>=17/40, inferred from T_Q(W0)<=3+v.
    Algebra is affine in v; equalities are checked at endpoints separately.
    """
    return ((F(1589)-1661*v)/185360, 3*(1113*v-887)/80360)


def support_algebra(v):
    c0=F(509,900); c2=F(1,100)
    V0=F(13,40)+v/80; V1=F(1,10)+9*v/40
    p0=F(77,80)-5*v/8; q0=F(37,40)-v/2
    x0=F(3,2)*q0-p0-V1/2
    x2=p0-q0/2-V1/2
    c1V1=F(47,1800)+F(67,720)*v
    ma0=c0*x0+c1V1+c2*x2
    mb0=V0-x0
    assert ma0==(8737-1661*v)/36000
    assert mb0==(5*v-1)/20
    d0=W0[0]+W0[1]-1
    bound1=(W0[1]/2+F(2,5)*ma0-d0)/F(2317,1125)
    bound2=(F(9,10)*ma0+mb0/2-d0)/F(2009,1000)
    assert (bound1,bound2)==upper_functions(v)
    return ma0,mb0

# Verifying at v=0 and v=1 proves identities of affine polynomials in v.
for probe in (F(0),F(1)):
    support_algebra(probe)
assert upper_functions(VFLOW)==(H,H)
assert VFLOW>=F(17,40) and VFLOW<=1
assert F(1019)*F(17,40)-96>0  # coefficient of X1 in M[1/10] positive throughout feasible v.

V=tuple((Q3[0][j]+VFLOW*Q3[1][j])/2 for j in range(3))
MBASE={r:F(0) for r in R}; MBASE[F(5,4)]=(1-VFLOW)/2
B={r:[F(0)]*3 for r in R}
for j in range(3):
    MBASE[R3[j]]+=V[j]
    B[R3[j]][j]-=1
    for i,u in enumerate((F(1),VFLOW)):
        share=(u/2)*Q3[i][j]/V[j]
        for z in range(3):
            B[R4[z]][j]+=share*Q4[i][j][z]
assert sum(MBASE.values())==1
assert sum(r*MBASE[r] for r in R)==1
for j in range(3):
    assert sum(B[r][j] for r in R)==0
    assert sum(r*B[r][j] for r in R)==0
assert B[F(1,10)][0]==F(509,900) and B[F(1,10)][2]==F(1,100)
assert B[F(1,10)][1]*V[1]==F(47,1800)+F(67,720)*VFLOW

BASE_P=2+(3+5*VFLOW)/8
BASE_Q=2+(1+VFLOW)/2
A0=F(81993,1719760)
C0=F(78158903,386946000)
C1=F(1181,902874)
C3=-F(1181,1805748)
C4=F(1181,1203832)
assert C1==F(10,9)*H and C4==F(5,6)*H
LABELS=('X0','X1','X2','V0-X0','V1-X1','V2-X2',
        'Ea','Eb','E1','M_1/10-Ea','M_1/2-Eb','M_1-E1')

def witness(t):
    assert len(t)==4 and all(-1<=z<=1 for z in t)
    w=tuple(W0[k]+H*t[k] for k in range(4))
    x2=A0+H*t[2]-H*t[3]/2
    ea=C0+C1*(t[0]+t[1])+C3*t[2]+C4*t[3]
    p=w[2]-BASE_P; q=w[3]-BASE_Q
    X=(x2+2*(q-p), 2*p-q-2*x2, x2)
    d=w[0]+w[1]-1
    eb=2*d-F(9,5)*ea
    e1=w[1]-ea-eb
    M={r:MBASE[r]+sum(B[r][j]*X[j] for j in range(3)) for r in R}
    E={r:F(0) for r in R}; E[F(1,10)]=ea; E[F(1,2)]=eb; E[F(1)]=e1
    assert X[1]==V[1]
    assert sum(M.values())==1 and sum(r*M[r] for r in R)==1
    assert (sum(E.values()),1-sum(r*E[r] for r in R))==(w[1],w[0])
    assert (BASE_P+X[0]/2+X[1]+F(3,2)*X[2],BASE_Q+sum(X))==w[2:]
    return X+tuple(V[j]-X[j] for j in range(3))+(ea,eb,e1,
        M[F(1,10)]-ea,M[F(1,2)]-eb,M[F(1)]-e1)

corners=[witness(tuple(map(F,t))) for t in product((-1,1),repeat=4)]
mins=[min(corner[k] for corner in corners) for k in range(12)]
expected=(F(2119387,12038320),F(245657,859880),F(552693,12038320),
          F(923197,6019160),F(0),F(364449,1504790),
          F(535597571,2708622000),F(923197,6019160),F(0),
          F(0),F(0),F(46341301,270862200))
assert tuple(mins)==expected and all(x>=0 for x in mins)
for t in product((F(-1),F(-1,2),F(0),F(1,2),F(1)),repeat=4):
    assert all(z>=0 for z in witness(t))

print('FROZEN_GLOBAL_SHA','a01383f825ef9d43b4b754254303298c64041568')
print('FROZEN_EM_SHA','86149263e38c22292c9def1e0f69092efa1be77e')
print('SOURCE_PREDECESSOR','fbe407fab76d396f12efd5c79f2283d6a59a7257')
print('CLASS','g=u0=1; one common v in [0,1] for full cube; shared time-3 LR decisions; all six stopped LR declaration keys allowed')
print('OPTIMAL_V',VFLOW,'OPTIMAL_HALF_RADIUS',H,'CENTER',*W0)
print('SUPPORT_UPPER_U1','(1589-1661*v)/185360')
print('SUPPORT_UPPER_U2','3*(1113*v-887)/80360')
print('CROSSING',*upper_functions(VFLOW))
print('AFFINE_X2',A0,F(0),F(0),H,-H/2)
print('AFFINE_E_1/10',C0,C1,C1,C3,C4)
print('PREVIOUS_HALF_RADIUS',LAST_H,'GAIN_RATIO',H/LAST_H)
for lab,m in zip(LABELS,mins):print('MIN_AT_16_VERTICES',lab,m)
print('CHECKS','conditional LR moments; 16 vertex minima; 625 grid targets; normalization; four-observer recovery; two universal support identities')
print('ALL_REAL_THEOREM','two support bounds for common-v cube and affine corner certificate')
print('PASS_EXACT_R5_COMMON_V_COMPLETE_SIX_LABEL_GLOBAL_CUBE_OPTIMUM')
