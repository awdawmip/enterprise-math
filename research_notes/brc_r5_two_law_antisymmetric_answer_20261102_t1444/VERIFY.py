"""Exact R5 two-law antisymmetric K-answer source-perturbation certificate.

Finite checks support an independent algebraic all-real proof; Fraction only.
"""
from fractions import Fraction as F
from itertools import product, combinations, permutations

S = ('C','I','BJ','IJ')
Z, H, O = F(0), F(1,2), F(1)

def obs(a,b,p,q,policy):
    x,jB,jI,kC,kI,kBJ,kIJ=map(F,policy)
    ks=dict(zip(S,(kC,kI,kBJ,kIJ)))
    ep=H*x; eq=Z; tp=H*x; tq=H*x
    arrivals={'B':F(1,4),'I':(O-x)*F(1,4)}
    masses={'C':F(1,4),'I':(O-x)*F(1,4)}
    for origin,j in (('B',jB),('I',jI)):
        w=arrivals[origin]
        ep += w*j
        tp += 2*w*j; tq += 2*w*j
        direct = w*(O-j)/2
        ep += F(3,5)*direct
        eq += F(3,5)*direct
        tp += 3*direct; tq += 3*direct
        masses['BJ' if origin=='B' else 'IJ']=direct
    for s in S:
        w=masses[s]; k=ks[s]
        ep += w*(k+(O-k)*a[s])
        eq += w*(O-k)*(O-b[s])
        tp += w*(3*k+(O-k)*(4+p[s]))
        tq += w*(3*k+(O-k)*(4+q[s]))
    return ep,eq,tp,tq

def model(delta):
    a={s:H for s in S}
    b={s:H for s in S}
    b['C']-=delta
    b['I']+=delta
    p={s:H for s in S}
    q={s:F(1,3) for s in S}
    return a,b,p,q

def lrpol(x,y,z): return (x,y,y,z,z,z,z)

def det4(M):
    out=Z
    for v in permutations(range(4)):
        sign=(-1)**sum(v[i]>v[j] for i in range(4) for j in range(i+1,4))
        val=F(sign)
        for i in range(4): val*=M[i][v[i]]
        out+=val
    return out

def rank4(points):
    base=points[0]
    d=[tuple(y-x for x,y in zip(base,z)) for z in points[1:]]
    for subset in combinations(range(len(d)),4):
        m=[[d[k][i] for k in subset] for i in range(4)]
        z=det4(m)
        if z: return subset,z
    return None,Z

def full_jacobian(delta):
    a,b,p,q=model(delta)
    mid=[H]*7
    cols=[]
    for i in range(7):
        lo=mid.copy(); hi=mid.copy(); lo[i]=Z; hi[i]=O
        loV=obs(a,b,p,q,lo); hiV=obs(a,b,p,q,hi)
        cols.append(tuple(v-u for u,v in zip(loV,hiV)))
    for ix in combinations(range(7),4):
        d=det4([[cols[k][i] for k in ix] for i in range(4)])
        if d: return ix,d
    return None,Z

checks=0
for delta in [F(-3,8),F(-1,4),F(-1,8),F(-1,80),Z,F(1,80),F(1,16),F(1,10),F(1,8),F(1,4),F(3,8)]:
    a,b,p,q=model(delta)
    assert all(0<a[s]<1 and 0<b[s]<1 and 0<p[s]<1 and 0<q[s]<1 for s in S);checks+=1
    Fpol={v:obs(a,b,p,q,v) for v in product((0,1),repeat=7)}
    Lpol={v:obs(a,b,p,q,lrpol(*v)) for v in product((0,1),repeat=3)}
    assert len(Fpol)==128 and len(Lpol)==8;checks+=1
    hF=max(w[0]+w[1] for w in Fpol.values())
    hL=max(w[0]+w[1] for w in Lpol.values())
    theoryF=F(21,20)+abs(delta)/4
    theoryL=F(21,20)+(max(Z, delta/F(4)-F(1,40)) if delta>0 else Z)
    assert (hF,hL)==(theoryF,theoryL), (delta,hF,hL,theoryF,theoryL);checks+=1
    gap= (F(-delta,4) if delta<0 else min(delta/4,F(1,40)))
    assert hF-hL==gap; checks+=1
    wkey=(0,0,0,0,1,0,0) if delta>=0 else (0,0,0,1,0,0,0)
    W=Fpol[wkey]
    assert W[0]+W[1]-hL == gap;checks+=1
    for v,w in Fpol.items():
        assert w[0]+w[1] <= theoryF;checks+=1
    for v,w in Lpol.items():
        assert w[0]+w[1] <= theoryL;checks+=1
    lr_rank=rank4(list(Lpol.values()))
    full_rank=full_jacobian(delta)
    print('delta',delta,'full',hF,'LR',hL,'gap',gap,'witness',W, 'LRdet',lr_rank,'FULLJdet',full_rank)
    if delta==F(1,8):
        assert gap==F(1,40) and W[0]+W[1]-hL==F(1,40)
        print('EXAMPLE_POSITIVE_W',W,'EXACT_distance_lower_bound',gap/2);checks+=1
    if delta==Z:
        for v,w in Fpol.items():
            x,jb,ji,kc,ki,kbj,kij=map(F,v)
            J_mass=(2-x)/4
            y=(jb/4+(O-x)*ji/4)/J_mass
            Kmass=(F(1,4),(O-x)/4,(O-jb)/8,(O-x)*(O-ji)/8)
            z=sum(m*k for m,k in zip(Kmass,(kc,ki,kbj,kij)))/sum(Kmass)
            assert w==obs(a,b,p,q,lrpol(x,y,z));checks+=1
print('PASS_EXACT_R5_TWO_LAW_ANTISYMMETRIC_K_ANSWER',checks,'exact assertions')
