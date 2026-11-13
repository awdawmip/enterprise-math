"""Exact stop-only natural-route compilation obstruction (standard-library Fraction)."""
from fractions import Fraction as F
from itertools import product, permutations

# Natural diamond: under Q, masses 7,3,3,7 over 20;
# under P, likelihood ratios by U of 1/2,3/2.
Q = {(0,0):F(7,20),(0,1):F(3,20),(1,0):F(3,20),(1,1):F(7,20)}
P = {(x,u): Q[x,u]*(F(1,2) if u==0 else F(3,2)) for x,u in Q}
assert sum(P.values())==sum(Q.values())==1
assert all(w>0 for w in P.values()) and all(w>0 for w in Q.values())
for x in (0,1):
    px=sum(P[x,u] for u in (0,1)); qx=sum(Q[x,u] for u in (0,1))
    assert px/qx==(F(4,5) if x==0 else F(6,5))
for u in (0,1):
    ratios=[P[x,u]/Q[x,u] for x in (0,1)]
    assert ratios==[F(1,2) if u==0 else F(3,2)]*2

c,a,b=F(1,4),F(1,8),F(1,8)
assert all(0 < k < 1 for k in (c,c+a,c+a+b))

def obs(s, ys, early_delta=(F(0),F(0))):
    # s_x=1 means continue after observing X at t=2; s_x=0 stops at t=2.
    # y_xu=1 stops at t=3; y_xu=0 forces a stop at t=4.
    out=[]
    for law in (P,Q):
        e=t=F(0)
        for (x,u),w in law.items():
            v=s[x]*ys[x,u]
            e += w*(c+a*x+early_delta[x]*(1-s[x])+b*x*v)
            t += w*(2+2*s[x]-v)
        out.extend((e,t))
    # (eP,eQ,TP,TQ)
    return out[0],out[2],out[1],out[3]

full=[]; lr=[]
for s_bits in product((0,1),repeat=2):
    s={0:s_bits[0],1:s_bits[1]}
    for y_bits in product((0,1),repeat=4):
        y={(0,0):y_bits[0],(0,1):y_bits[1],(1,0):y_bits[2],(1,1):y_bits[3]}
        full.append((obs(s,y),(s_bits,y_bits)))
    for y_bits in product((0,1),repeat=2):
        y={(x,u):y_bits[u] for x in (0,1) for u in (0,1)}
        lr.append((obs(s,y),(s_bits,y_bits)))
assert len(full)==64 and len(lr)==16
score=lambda o:16*o[0]+o[2]
fmax=max(score(o) for o,_ in full)
lmax=max(score(o) for o,_ in lr)
assert fmax==F(49,5) and lmax==F(19,2) and fmax-lmax==F(3,10)
fw=(obs({0:1,1:1},{(x,u):x for x in (0,1) for u in (0,1)}))
assert fw==(F(2,5), F(3,8), F(17,5), F(7,2))
assert score(fw)==fmax

# General proof identity for P and exact overlap coefficient.
gamma=sum(min(P[0,u],P[1,u]) for u in (0,1))
assert gamma==F(3,10)
assert fmax-lmax==gamma

# Rank via exact Fraction Gaussian elimination.
def rank(rows):
    a=[list(row) for row in rows]
    if not a:return 0
    m,n=len(a),len(a[0]); r=0
    for col in range(n):
        piv=next((i for i in range(r,m) if a[i][col]!=0),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        pv=a[r][col]
        a[r]=[v/pv for v in a[r]]
        for i in range(m):
            if i!=r and a[i][col]!=0:
                coeff=a[i][col]
                a[i]=[v-coeff*w for v,w in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

base=lr[0][0]
aff_rank=rank([[z-b for z,b in zip(o,base)] for o,_ in lr])
assert aff_rank==4

def det4(rows):
    sign_total=F(0)
    for perm in permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        prod=F((-1)**inversions)
        for i,j in enumerate(perm):prod*=rows[i][j]
        sign_total+=prod
    return sign_total

rank_indices=(0,4,5,6,8)
D=det4([[z-b for z,b in zip(lr[i][0],lr[rank_indices[0]][0])]
        for i in rank_indices[1:]])
assert D==F(21,64000)

# Two-dimensional robustness wedge for early P and Q error perturbations.
# Necessary legality is verified for the sampled rational pairs. The
# mathematical statement for every real admissible pair is proved separately.
robust_pairs=((F(0),F(0)),(F(1,32),F(1,16)),
              (F(1,16),F(1,8)),(F(-1,16),F(-1,16)))
for d0,d1 in robust_pairs:
    assert d0/b<=F(1,2) and d1/b<=1
    assert all(0<k<1 for k in (c+d0,c+a+d1,c,c+a,c+a+b))
    ff=[]; ll=[]
    for s_bits in product((0,1),repeat=2):
        surv={0:s_bits[0],1:s_bits[1]}
        for bits in product((0,1),repeat=4):
            y={(0,0):bits[0],(0,1):bits[1],(1,0):bits[2],(1,1):bits[3]}
            ff.append(score(obs(surv,y,(d0,d1))))
        for bits in product((0,1),repeat=2):
            y={(x,u):bits[u] for x in (0,1) for u in (0,1)}
            ll.append(score(obs(surv,y,(d0,d1))))
    assert max(ff)==fmax and max(ll)==lmax

print('PIN_P_Q_MASSES', sorted((f'{x}{u}',str(P[x,u]),str(Q[x,u])) for x,u in Q))
print('FULL_POLICY_COUNT',len(full),'LR_POLICY_COUNT',len(lr))
print('FULL_WITNESS',tuple(map(str,fw)))
print('FULL_SUPPORT',fmax,'LR_SUPPORT',lmax,'EXACT_GAP',fmax-lmax)
print('LR_AFFINE_RANK',aff_rank, 'DET_CERT',D,'INDEX_SET',rank_indices)
print('ROBUST_EARLY_ERROR_PAIRS', len(robust_pairs), 'ALL_SUPPORT_GAP',gamma)
print('L_INFINITY_DISTANCE_LOWER_BOUND',gamma/F(17))
print('PASS_EXACT_R5_STOP_ONLY_CENSOR_COMPILER_NO_GO')
