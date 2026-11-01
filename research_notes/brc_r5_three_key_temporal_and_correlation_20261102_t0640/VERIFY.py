from fractions import Fraction as Q
from itertools import product
from itertools import combinations
O,Z,H=Q(1),Q(0),Q(1,2)
checks=0
def ck(test,desc):
    global checks
    checks+=1
    assert test,desc

def add(*vs):return tuple(sum(v[i] for v in vs) for i in range(4))
def mul(a,v):return tuple(a*t for t in v)
def det(M):
    if len(M)==1:return M[0][0]
    return sum((-1)**j*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(len(M)))
def LR(x,y,z):return x,y,z,x*y
def FULL(x,u,v,z):
    masses=((O-x)*(O-u),(O-x)*u,x*(O-v),x*v)
    ck(all(t>=0 for t in masses) and sum(masses)==O,'positive BRC carrier')
    return (masses[2]+masses[3],masses[1]+masses[3],z,masses[3])
LV={LR(*map(Q,v)) for v in product((0,1),repeat=3)}
FV={FULL(*map(Q,v)) for v in product((0,1),repeat=4)}
ck(len(LV)==8 and LV==FV,'same binary hull vertices')
W=FULL(H,Z,O,H)
ck(W==(H,H,H,H),'joint witness')
ck(W==tuple((a+b)/2 for a,b in zip(LR(Z,Z,H),LR(O,O,H))),'hull membership')
# Q(sqrt(5)) two-component exact arithmetic
A=(-O,H) # distance sqrt(5)/2 - 1
def qmul(a,b):return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
ck((qmul(A,A)[0]+2*A[0],qmul(A,A)[1]+2*A[1])==(Q(1,4),Z),'sharp distance polynomial')
ck((qmul((-H,H),(-H,H))[0]+(-H),qmul((-H,H),(-H,H))[1]+H)==(O,Z),'s^2+s=1')
print('ABSTRACT: FULL/LR hull equal, W=',W,'distance=(sqrt(5)-2)/2')

# Finite two-law stopping DAG with actual decision keys I(t=1), J(t=2), K(t=3).
# Root: I=1/2, bypass-to-J=1/4, bypass-to-K=1/4; natural branches
# I->J and J->K each have probability 1/2 under BOTH measures.
K={'C':(Q(3,4),Q(1,4),Q(1,4),Q(3,4)),
   'I':(Q(1,4),Q(3,4),Q(3,4),Q(1,4)),
   'BJ':(Q(2,3),Q(1,3),Q(1,3),Q(2,3)),
   'IJ':(Q(1,3),Q(2,3),Q(2,3),Q(1,3))}
J={'B':(Q(2,5),Q(3,5)),'I':(Q(3,5),Q(2,5))}
ck(all(Z<t<O for row in list(K.values())+list(J.values()) for t in row),'all natural terminal probabilities interior')
def stop(t):return O,Z,Q(t),Q(t)
def answer(t,p,q):return p,O-q,Q(t),Q(t)
def knode(source,v):
    p,q,dp,dq=K[source]
    return add(mul(v,stop(3)),mul(O-v,(p,O-q,Q(4)+dp,Q(4)+dq)))
def jnode(source,u,v):
    p,q=J[source]
    cont=add(mul(H,knode(source+'J' if source=='I' else 'BJ',v)),mul(H,answer(3,p,q)))
    return add(mul(u,stop(2)),mul(O-u,cont))
def physical(x,jb,ji,kc,ki,kbj,kij):
    I=add(mul(x,stop(1)),mul(O-x,add(mul(H,jnode('I',ji,kij)),mul(H,knode('I',ki)))))
    return add(mul(H,I),mul(Q(1,4),jnode('B',jb,kbj)),mul(Q(1,4),knode('C',kc)))
def common(x,y,z):return physical(x,y,y,z,z,z,z)
def td(x,jb,ji,kc,ki,kbj,kij):
    return (-Q(1,8)*(O-kc)+Q(1,8)*(O-x)*(O-ki)
            -Q(1,24)*(O-jb)*(O-kbj)+Q(1,24)*(O-x)*(O-ji)*(O-kij))
def tdl(x,y,z):return -x*(O-z)*(4-y)/24
all7={v:physical(*v) for v in product((Z,O),repeat=7)}
all3={v:common(*v) for v in product((Z,O),repeat=3)}
ck(len(all7)==128 and len(all3)==8,'strategy count')
ck(set(all3.values()).issubset(set(all7.values())),'LR subset')
for v,w in all7.items():ck(w[2]-w[3]==td(*v),'full physical branch time')
for v,w in all3.items():ck(w[2]-w[3]==tdl(*v),'LR physical branch time')
for vals in product((Z,H,O),repeat=7):
    w=physical(*vals)
    ck(w[2]-w[3]==td(*vals),'full interior time identity')
for vals in product((Z,Q(1,4),H,Q(3,4),O),repeat=3):
    w=common(*vals)
    ck(w[2]-w[3]==tdl(*vals),'LR interior time identity')
W3=physical(Z,O,Z,O,Z,O,Z)
ck(W3==(Q(163,240),Q(43,240),Q(163,48),Q(155,48)),'explicit DAG witness')
ck(max(v[2]-v[3] for v in all7.values())==Q(1,6),'FULL support')
ck(max(v[2]-v[3] for v in all3.values())==Z,'LR support')
keys=[(Z,Z,Z),(Z,Z,O),(Z,O,Z),(O,Z,Z),(O,Z,O)]
base=all3[keys[0]]
cols=[tuple(all3[k][i]-base[i] for i in range(4)) for k in keys[1:]]
ck(det([[cols[j][i] for j in range(4)] for i in range(4)])==Q(1,5120),'LR hull affine rank four')
print('STOPPING DAG: 128 FULL corners, 8 LR corners, 4D LR hull')
print('h_FULL(TP-TQ)=1/6; h_LR(TP-TQ)=0; witness=',W3)
print('LR exact identity: TP-TQ=-x*(1-z)*(4-y)/24')
print('DAG infinity-distance certificate >=1/12')
print('checks=',checks)
print('PASS_EXACT_R5_TWO_MEASURE_THREE_KEY_AND_CORRELATION_BENCHMARK')
