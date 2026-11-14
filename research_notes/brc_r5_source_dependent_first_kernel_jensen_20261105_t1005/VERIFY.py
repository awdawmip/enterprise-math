from fractions import Fraction as F
from itertools import product

# Source-dependent first kernels: Q probability; P(r) = r Q(r).
R = (F(1,2), F(1), F(3,2))
S = (F(1,4), F(1,2), F(1), F(3,2), F(7,4))
weights = (F(1,2), F(1,2))
K = ((F(1,4),F(1,2),F(1,4)), (F(3,8),F(1,4),F(3,8)))
epsilon = F(1,16)
V = (
    (F(11,15),F(1,15),F(1,15),F(1,15),F(1,15)),
    tuple(F(1,5) for _ in S),
    (F(1,15),F(1,15),F(1,15),F(1,15),F(11,15))
)
M = tuple(tuple((1-epsilon if s==r else 0)+epsilon*v for s,v in zip(S,V[j])) for j,r in enumerate(R))

assert sum(weights)==1
for Kh in K:
    assert all(x>0 for x in Kh)
    assert sum(Kh)==1 and sum(x*r for x,r in zip(Kh,R))==1
for j,m in enumerate(M):
    assert all(x>0 for x in m)
    assert sum(m)==1 and sum(x*s for x,s in zip(m,S))==R[j]
    assert sum(s*m[i]/R[j] for i,s in enumerate(S))==1  # P conditional normalization

k,c=F(1),F(5,32)
C=lambda x:-min(x,k)
G0=tuple(sum(x*C(r) for x,r in zip(Kh,R))-C(1) for Kh in K)
G2=tuple(sum(v*C(s) for v,s in zip(m,S))-C(r) for m,r in zip(M,R))
assert G0==(F(1,8),F(3,16))
assert G2==(F(1,192),F(1,64),F(1,192))
assert all(g<=c*r for g,r in zip(G2,R))
Gbar=sum(w*g for w,g in zip(weights,G0))
assert Gbar==c==F(5,32)
pos=lambda x:max(x,F(0))
full_support=C(F(1))-c+sum(w*pos(g-c) for w,g in zip(weights,G0))
lr_support=C(F(1))-c+pos(Gbar-c)
assert (full_support,lr_support,full_support-lr_support)==(F(-73,64),F(-37,32),F(1,64))

P,Q,D = 'P','Q','C'
def observe(first, second, terminal):
    out=[F(0),F(0),F(0),F(0)]
    def accumulate(q,r,t,declare):
        if declare == P: out[1]+=q
        elif declare == Q: out[0]+=q*r
        else: raise AssertionError(declare)
        out[2]+=q*r*t;out[3]+=q*t
    for h in range(2):
        if first[h]!=D:
            accumulate(weights[h],F(1),1,first[h]);continue
        for j,r in enumerate(R):
            q=weights[h]*K[h][j]
            action=second[h][j]
            if action!=D:
                accumulate(q,r,2,action);continue
            for v,s in zip(M[j],S):
                accumulate(q*v,s,3,terminal[h][S.index(s)])
    return tuple(out)

def score(vec): return -vec[0]-k*vec[1]-c*vec[2]

# Legal FULL witness (declares at t=2), irrelevant disabled keys assigned P.
fw=observe((P,D),((P,P,P),(Q,P,P)),((P,)*len(S),(P,)*len(S)))
assert fw==(F(3,32),F(13,16),F(3,2),F(3,2))
assert score(fw)==full_support

# Independently enumerate ALL deterministic seedless LR strategies.
max_score=None;max_count=0;policy_count=0
for first_act in (P,Q,D):
    for second_acts in product((P,Q,D),repeat=len(R)):
        for terminal_acts in product((P,Q),repeat=len(S)):
            policy_count+=1
            point=observe((first_act,)*2,(second_acts,)*2,(terminal_acts,)*2)
            val=score(point)
            if max_score is None or val>max_score:
                max_score=val;max_count=1
            elif val==max_score: max_count+=1
assert policy_count==3*(3**len(R))*(2**len(S))==2592
assert max_score==lr_support

# Independent Bellman recursion for FULL and seedless supports.
term_good=tuple(sum(v*C(s) for v,s in zip(m,S)) for m in M)
second_best=tuple(max(C(r)-2*c*r,term_good[j]-3*c*r) for j,r in enumerate(R))
source_opt=tuple(max(C(F(1))-c,sum(x*y for x,y in zip(Kh,second_best))) for Kh in K)
assert sum(w*v for w,v in zip(weights,source_opt))==full_support
kbar=tuple(sum(weights[h]*K[h][j] for h in range(2)) for j in range(len(R)))
seedless_opt=max(C(F(1))-c,sum(x*y for x,y in zip(kbar,second_best)))
assert seedless_opt==lr_support

norm_l1=F(2)+c
assert norm_l1==F(69,32)
assert (full_support-lr_support)/norm_l1==F(1,138)
# The epsilon-family proof is analytic; these exact samples test its endpoint and interior.
for eta in (F(1,100),F(1,16),F(1,4),F(1,2),F(5,8)):
    etaM=tuple(tuple((1-eta if s==r else 0)+eta*v for s,v in zip(S,V[j])) for j,r in enumerate(R))
    gains=tuple(sum(v*C(s) for v,s in zip(row,S))-C(r) for row,r in zip(etaM,R))
    assert all(x>0 for row in etaM for x in row)
    assert gains==(eta/F(12),eta/F(4),eta/F(12))
    assert all(g<=c*r for g,r in zip(gains,R))
    assert max(g/r for g,r in zip(gains,R))==eta/F(4)
print('K_A, K_B =', K)
print('terminal common S =',S)
print('terminal common M =',M)
print('G0_A, G0_B, Gbar =',*G0,Gbar)
print('G2 =',G2,'ratios G2/r =',tuple(g/r for g,r in zip(G2,R)))
print('normal = (-1,-1,-5/32,0); full=',full_support,'seedless LR=',lr_support,'gap=',full_support-lr_support)
print('FULL witness O4 =',fw,'l1 normal =',norm_l1,'distinf lower bound =',F(1,138))
print('exhaustive seedless deterministic strategies=',policy_count,'maximizers=',max_count)
print('epsilon-family Fraction sample checks = 5, including eta=5/8 endpoint')
print('PASS_EXACT_R5_SOURCE_DEPENDENT_FIRST_KERNEL_JENSEN')