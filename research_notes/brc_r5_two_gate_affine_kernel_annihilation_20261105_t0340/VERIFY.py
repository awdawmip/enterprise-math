from fractions import Fraction as F
from itertools import product

r = (F(1,2), F(1), F(3,2))
s = (F(1,8), F(1), F(15,8))
w = (F(1,2), F(1,2))
K = ((F(1,4),F(1,2),F(1,4)),(F(5,16),F(6,16),F(5,16)))
M = ((F(37,56),F(14,56),F(5,56)),
     (F(21,56),F(14,56),F(21,56)),
     (F(5,56),F(14,56),F(37,56)))
zero = F(0)
assert all(all(v>0 for v in row) and sum(row)==1 and sum(t*v for t,v in zip(r,row))==1 for row in K)
assert all(all(v>0 for v in row) and sum(row)==1 and sum(t*v for t,v in zip(s,row))==r[j] for j,row in enumerate(M))
assert all(M[0][l]+M[2][l]==2*M[1][l] for l in range(3))

# First-gate action 0: stop and declare P, 1: stop and declare Q, 2: continue.
# Second gate has the same actions, and final label 0 declares P, 1 declares Q.
def verify(first,second,final):
    C=sum((w[h]*int(first[h]==2) for h in range(2)),zero)
    earlyP=sum((w[h]*int(first[h]==0) for h in range(2)),zero)
    earlyQ=sum((w[h]*int(first[h]==1) for h in range(2)),zero)
    barK=[sum((w[h]*K[h][j] for h in range(2)),zero) for j in range(3)]
    A=[sum((w[h]*int(first[h]==2)*K[h][j] for h in range(2)),zero) for j in range(3)]
    B=[C*barK[j] for j in range(3)]
    D=[A[j]-B[j] for j in range(3)]
    assert sum(D)==0 and sum((r[j]*D[j] for j in range(3)),zero)==0
    a=[]; b=[]; d=[]
    U=[]
    for j in range(3):
        massP=sum((w[h]*int(first[h]==2)*K[h][j]*int(second[h][j]==0) for h in range(2)),zero)
        massQ=sum((w[h]*int(first[h]==2)*K[h][j]*int(second[h][j]==1) for h in range(2)),zero)
        massC=sum((w[h]*int(first[h]==2)*K[h][j]*int(second[h][j]==2) for h in range(2)),zero)
        if A[j]:
            a.append(massP/A[j]); b.append(massQ/A[j]); d.append(massC/A[j])
        else:
            a.append(F(1));b.append(zero);d.append(zero)
        U.append(massC)
        assert a[j]+b[j]+d[j]==1
    muF=[sum((w[h]*int(first[h]==2)*K[h][j]*int(second[h][j]==2)*M[j][l]
              for h in range(2) for j in range(3)),zero) for l in range(3)]
    muL=[sum((B[j]*d[j]*M[j][l] for j in range(3)),zero) for l in range(3)]
    N=[sum((w[h]*int(first[h]==2)*K[h][j]*int(second[h][j]==2)*M[j][l]*int(final[h][j][l]==0)
              for h in range(2) for j in range(3)),zero) for l in range(3)]
    p=[N[l]/muF[l] if muF[l] else zero for l in range(3)]
    E=[muF[l]-muL[l] for l in range(3)]
    assert E==[sum((D[j]*d[j]*M[j][l] for j in range(3)),zero) for l in range(3)]
    assert sum(E)==sum((D[j]*d[j] for j in range(3)),zero)
    assert sum((s[l]*E[l] for l in range(3)),zero)==sum((r[j]*D[j]*d[j] for j in range(3)),zero)
    eQF=earlyP+sum((A[j]*a[j] for j in range(3)),zero)+sum(N)
    eQL=earlyP+sum((B[j]*a[j] for j in range(3)),zero)+sum((muL[l]*p[l] for l in range(3)),zero)
    ePF=earlyQ+sum((r[j]*A[j]*b[j] for j in range(3)),zero)+sum((s[l]*(muF[l]-N[l]) for l in range(3)),zero)
    ePL=earlyQ+sum((r[j]*B[j]*b[j] for j in range(3)),zero)+sum((s[l]*muL[l]*(1-p[l]) for l in range(3)),zero)
    TQF=F(1)+C+sum(U)
    TQL=F(1)+C+sum((B[j]*d[j] for j in range(3)),zero)
    TPF=F(1)+C+sum((r[j]*U[j] for j in range(3)),zero)
    TPL=F(1)+C+sum((r[j]*B[j]*d[j] for j in range(3)),zero)
    assert eQF-eQL==sum((D[j]*a[j] for j in range(3)),zero)+sum((E[l]*p[l] for l in range(3)),zero)
    assert ePF-ePL==sum((r[j]*D[j]*b[j] for j in range(3)),zero)+sum((s[l]*E[l]*(1-p[l]) for l in range(3)),zero)
    assert TQF-TQL==sum((D[j]*d[j] for j in range(3)),zero)
    assert TPF-TPL==sum((r[j]*D[j]*d[j] for j in range(3)),zero)
    return (ePF,eQF,TPF,TQF),(ePL,eQL,TPL,TQL),tuple(D),tuple(E)

# Complete finite deterministic check over all 3^2 first-gate and 3^6 second-gate policies;
# final labels are source/history-specific and deliberately not key-lumpable.
counter=0;nonzero=0
for first in product(range(3),repeat=2):
    for flat in product(range(3),repeat=6):
        second=(flat[:3],flat[3:])
        final=tuple(tuple(tuple((h+j+2*l)%2 for l in range(3)) for j in range(3)) for h in range(2))
        a,b,_,_=verify(first,second,final)
        counter+=1
        nonzero+=a!=b
assert counter==6561

# Exact positive-kernel cancellation even though first gate and hidden kernels differ.
# First source continues, second source stops and declares P; at gate 2 everyone
# stops/declares P with probability 1/2 or continues with probability 1/2.
# At gate 3 declare P only if s_l == 1.
C=F(1,2)
A=[w[0]*K[0][j] for j in range(3)]
B=[C*sum((w[h]*K[h][j] for h in range(2)),zero) for j in range(3)]
D=[A[j]-B[j] for j in range(3)]
muF=[sum((A[j]*F(1,2)*M[j][l] for j in range(3)),zero) for l in range(3)]
muL=[sum((B[j]*F(1,2)*M[j][l] for j in range(3)),zero) for l in range(3)]
assert D==[F(-1,64),F(1,32),F(-1,64)] and any(D)
assert muF==muL==[F(3,32),F(1,16),F(3,32)]
O=(F(3,16),F(13,16),F(7,4),F(7,4))
assert O==(sum((s[l]*muF[l] for l in (0,2)),zero),
           F(1,2)+F(1,4)+muF[1], F(1)+C+F(1,4),F(1)+C+F(1,4))

# An explicit nonuniform gate-2 decision re-exposes the intermediate covariance in time:
d=(F(1),F(0),F(1))
assert sum((D[j]*d[j] for j in range(3)),zero)==F(-1,32)
assert sum((r[j]*D[j]*d[j] for j in range(3)),zero)==F(-1,32)

# Converse: a nonaffine column detects some signed zero-moment D.
Q=(F(1),F(-2),F(1))
assert sum(Q)==sum((r[j]*Q[j] for j in range(3)),zero)==0
assert all(sum((Q[j]*M[j][l] for j in range(3)),zero)==0 for l in range(3))
Mbad=(M[0],tuple(M[1][l]+F(1,56)*(1,-2,1)[l] for l in range(3)),M[2])
assert all(all(v>0 for v in row) and sum(row)==1 and sum(t*v for t,v in zip(s,row))==r[j] for j,row in enumerate(Mbad))
assert sum((Q[j]*Mbad[j][0] for j in range(3)),zero)==F(-1,28)
print("PASS_EXACT_R5_TWO_GATE_AFFINE_KERNEL_ANNIHILATION")
print("Q_P_KERNEL_STRICTLY_POSITIVE=",True)
print("FULL_DETERMINISTIC_GATE_POLICIES=",counter)
print("NONZERO_CANONICAL_O4_DIFFERENCES=",nonzero)
print("FIRST_GATE_RESIDUAL_D=",tuple(D))
print("SECOND_GATE_AFFINE_TERMINAL_FULL=",tuple(muF))
print("SECOND_GATE_AFFINE_TERMINAL_LR=",tuple(muL))
print("FULL_AND_LR_EXAMPLE_O4=",O)
print("NONUNIFORM_GATE_TQ_TP_DIFFERENCE=",F(-1,32))
