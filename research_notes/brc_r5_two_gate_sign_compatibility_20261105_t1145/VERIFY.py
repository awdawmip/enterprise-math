from fractions import Fraction as F
from itertools import product

R=(F(1,2),F(1),F(3,2))
S=(F(1,4),F(1,2),F(1),F(3,2),F(7,4))
W=(F(1,2),F(1,2))
K=((F(1,4),F(1,2),F(1,4)),(F(3,8),F(1,4),F(3,8)))
LOW=(F(11,15),F(1,15),F(1,15),F(1,15),F(1,15))
HIGH=tuple(reversed(LOW))
MID_A=(F(1,10),F(1,10),F(3,5),F(1,10),F(1,10))
MID_B=(F(1,8),F(3,16),F(3,8),F(3,16),F(1,8))
M=((LOW,MID_A,HIGH),(LOW,MID_B,HIGH))
n=(F(-1),F(-1),F(-1),F(27,32))
k=F(1)
def c(r): return r-F(27,32)
def C(r): return -min(r,k)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def pos(x):return max(x,F(0))

# Conditional source-specific probability kernels and change of measure.
for h in range(2):
    assert sum(K[h])==1 and dot(K[h],R)==1
    for j,r in enumerate(R):
        assert all(q>0 for q in M[h][j]); assert sum(M[h][j])==1
        assert dot(M[h][j],S)==r
        assert sum((s*q/r for s,q in zip(S,M[h][j])),F(0))==1

A=[dot(K[h],tuple(C(r) for r in R))-C(F(1)) for h in range(2)]
B=[[dot(M[h][j],tuple(C(s) for s in S))-C(r) for j,r in enumerate(R)] for h in range(2)]
D=[[B[h][j]-c(r) for j,r in enumerate(R)] for h in range(2)]
X=[A[h]-c(F(1))+dot(K[h],tuple(pos(D[h][j]) for j in range(3))) for h in range(2)]
mu=dot(W,X)
eta=sum((sum((W[h]*K[h][j]*pos(D[h][j]) for h in range(2)),F(0)) - pos(sum((W[h]*K[h][j]*D[h][j] for h in range(2)),F(0))) for j in range(3)),F(0))
baseline=C(F(1))-c(F(1))
full=baseline+dot(W,tuple(pos(x) for x in X))
lr=baseline+pos(mu-eta)
assert A==[F(1,8),F(3,16)], (A,B)
assert B[0]==[F(1,12),F(1,8),F(1,12)]
assert B[1]==[F(1,12),F(3,16),F(1,12)]
assert X==[F(29,384),F(51,256)], X
assert eta==F(1,256) and mu>eta>0
assert full-lr==F(1,256)

def obs(first, second, labels):
    ep=eq=tp=tq=F(0)
    def collect(qmass, pmass, time, dec):
        nonlocal ep,eq,tp,tq
        assert qmass>=0 and pmass>=0
        tp+=pmass*time; tq+=qmass*time
        if dec=='P':eq+=qmass
        else:ep+=pmass
    for h in range(2):
        if first[h]!='continue':
            collect(W[h],W[h],1,first[h]);continue
        for j,r in enumerate(R):
            qmass=W[h]*K[h][j]
            pmass=qmass*r
            action=second[h][j]
            if action!='continue':
                collect(qmass,pmass,2,action)
            else:
                for l,s in enumerate(S):
                    collect(qmass*M[h][j][l], qmass*s*M[h][j][l],3,labels[l])
    return (ep,eq,tp,tq)

labels=tuple('Q' if s<1 else 'P' for s in S)
first=('continue','continue')
second=(('continue','P','P'),('continue','continue','P'))
witness=obs(first,second,labels)
assert dot(witness,n)==full, (witness,full,dot(witness,n))

max_lr=None; argmax_count=0; count=0
for firstaction in ('P','Q','continue'):
    for acts in product(('P','Q','continue'), repeat=3):
        for lab in product(('P','Q'),repeat=5):
            p=obs((firstaction,firstaction),(acts,acts),lab)
            v=dot(p,n); count+=1
            if max_lr is None or v>max_lr: max_lr=v;argmax_count=1
            elif v==max_lr: argmax_count+=1
assert count==2592
assert max_lr==lr,(max_lr,lr)
print('A =',A)
print('B_A =',B[0],'; B_B =',B[1])
print('D_A =',D[0],'; D_B =',D[1])
print('X =',X,'mu =',mu,'eta =',eta)
print('h_FULL =',full,'h_LR =',lr,'gap =',full-lr)
print('W_FULL =',witness,'dot(n,W) =',dot(n,witness))
print('seedless_LR_deterministic_count =',count,'argmax_count =',argmax_count)
print('dist_inf_lower_bound =', (full-lr)/sum(map(abs,n)))
print('PASS_EXACT_R5_TWO_GATE_SIGN_COMPATIBILITY')
