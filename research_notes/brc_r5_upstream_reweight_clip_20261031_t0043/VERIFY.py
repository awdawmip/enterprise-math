#!/usr/bin/env python3
"""Exact rational certificates for the two-source upstream-reweighted three-class stop model.

All arithmetic is Fraction/integer. Brute maxima exhaust 2^18 FULL or 2^7 LR
local deterministic STOP/CONTINUE policies for a fixed exact model.
"""
from fractions import Fraction as F
from itertools import product
from math import lcm

RU=(F(3,4),F(5,4))
RV=(F(1,2),F(1),F(3,2))

def k(t,u):
    return (F(1,2)+t,F(1,2)-2*t,t) if u==0 else (t,F(1,2)-2*t,F(1,2)+t)

def ell(t):
    return (5-2*t)/(6-4*t)

def pos(z):
    return max(F(0),z)

def model(A,B,t0,t1):
    assert F(0)<A<F(1,2) and F(0)<B<F(1,2) and A!=B
    assert all(F(0)<t<F(1,4) for t in (t0,t1))
    aa=(A,F(1,2)-A)
    bb=(B,F(1,2)-B)
    ts=(t0,t1)
    Q={(x,0):aa[x] for x in (0,1)}
    Q.update({(x,1):bb[x] for x in (0,1)})
    assert sum(Q.values())==1
    lr_x=[sum(Q[x,u]*RU[u] for u in (0,1))/(aa[x]+bb[x]) for x in (0,1)]
    assert lr_x[0]!=lr_x[1]
    w=[aa[x]*(F(3,2)-ts[x]) for x in (0,1)]
    lam=sum(w[x]*ell(ts[x]) for x in (0,1))/sum(w)
    assert F(5,6)<lam<F(9,10)
    G={(x,u):RU[u]-lam+sum(k(ts[x],u)[v]*pos(RV[v]-lam) for v in range(3)) for x,u in product((0,1),repeat=2)}
    for x in (0,1):
        assert G[x,0]==(F(3,2)-ts[x])*(ell(ts[x])-lam)
        assert G[x,1]==F(5,2)-2*lam+ts[x]*(lam-F(1,2))>0
    g=(aa[0]*G[0,0],aa[1]*G[1,0])
    assert sum(g)==0
    D=[aa[x]*(RU[0]-lam)+bb[x]*(RU[1]-lam+G[x,1]) for x in (0,1)]
    full=2*(1-lam)+sum(pos(D[x]+pos(g[x])) for x in (0,1))
    lr=2*(1-lam)+max(sum(pos(D) for D in D),sum(pos(D[x]+g[x]) for x in (0,1)))
    gap=full-lr
    assert gap>=0
    # Exact characterization of when THIS lambda creates a strict separating gap.
    if g[0]>0:
        assert (gap>0)==(D[0]+g[0]>0 and D[1]>0)
    if g[1]>0:
        assert (gap>0)==(D[1]+g[1]>0 and D[0]>0)
    if t0!=t1:
        assert (g[0]>0)^(g[1]>0)
    raw=[]
    for x,u,v in product((0,1),(0,1),range(3)):
        q=Q[x,u]*k(ts[x],u)[v]
        p=RV[v]*q
        assert p>0 and q>0
        raw.append((x,u,v,p,q))
    assert sum(z[3] for z in raw)==sum(z[4] for z in raw)==1
    for x,u in product((0,1),repeat=2):
        assert sum(k(ts[x],u)[v]*RV[v] for v in range(3))==RU[u]
    return dict(lam=lam,gap=gap,full=full,lr=lr,raw=raw,D=D,g=g,aa=aa,bb=bb,
                lr_x=lr_x,cone=all(bb[x]>=aa[x]/4 for x in (0,1)))

def brute(raw,lam,full):
    den=lcm(*(n.denominator for row in raw for n in row[3:]))
    fac=lam.denominator
    numer=lam.numerator
    entries=[(x,u,v,int(p*den)*fac-int(q*den)*numer) for x,u,v,p,q in raw]
    nbits=18 if full else 7
    best=None
    arg=None
    for bits in range(1<<nbits):
        total=0
        for x,u,v,weight in entries:
            if full:
                early=(bits>>x)&1
                mid=(bits>>(2+2*x+u))&1
                last=(bits>>(6+6*x+3*u+v))&1
            else:
                early=(bits>>x)&1
                mid=(bits>>(2+u))&1
                last=(bits>>(4+v))&1
            stopped=2 if not early else (3 if not mid else (4 if not last else 5))
            total+=stopped*weight
        if best is None or total>best:
            best=total
            arg=bits
    return F(best,den*fac),arg

if __name__=='__main__':
    # Exact parameter-grid validation of closed formulas and sufficiency region.
    vals=(F(1,8),F(1,4),F(1,3),F(3,8))
    tv=(F(1,16),F(1,8),F(3,16))
    n=0;nc=0;nsep=0;nzero=0
    for A,B,t0,t1 in product(vals,vals,tv,tv):
        if A==B:continue
        r=model(A,B,t0,t1)
        n+=1
        if r['cone']:
            nc+=1
            if t0!=t1:
                nsep+=1
                assert r['gap']==r['aa'][0]*r['aa'][1]*abs(t1-t0)/(
                    r['aa'][0]*(3-2*t0)+r['aa'][1]*(3-2*t1))>0
        if t0==t1:
            assert r['gap']==0
            nzero+=1
    print('EXACT_GRID_MODELS',n,'CONE_MODELS',nc,'CONE_OFFDIAGONAL_SEPARATIONS',nsep,'DIAGONAL_ZERO',nzero)
    chosen=[('new_reweight',F(1,4),F(1,3),F(1,16),F(1,8)),
            ('reverse',F(1,4),F(1,3),F(1,8),F(1,16)),
            ('old_upstream',F(3,8),F(1,8),F(1,16),F(1,8)),
            ('boundary_scope',F(49,100),F(1,100),F(1,16),F(1,8))]
    for name,A,B,t0,t1 in chosen:
        r=model(A,B,t0,t1)
        bf,ifull=brute(r['raw'],r['lam'],True)
        bl,ilr=brute(r['raw'],r['lam'],False)
        assert bf==r['full'] and bl==r['lr']
        print(name,'lam',r['lam'],'gap',r['gap'],'FULL',bf,'LR',bl,'D',r['D'],'g',r['g'],'early_cone',r['cone'])
        if name=='new_reweight':
            assert r['lam']==F(77,90) and r['gap']==F(1,360)
            assert r['gap']/(1+r['lam'])==F(1,668)
            G={(x,u):RU[u]-r['lam']+sum(k((t0,t1)[x],u)[v]*pos(RV[v]-r['lam']) for v in range(3)) for x,u in product((0,1),repeat=2)}
            TP=TQ=F(0)
            for x,u,v,p,q in r['raw']:
                mid=(u==1 or G[x,0]>0)
                tau=3 if not mid else (4 if v==0 else 5)
                TP+=p*tau;TQ+=q*tau
            assert TP-r['lam']*TQ==bf
            print('NEW_WITNESS TP',TP,'TQ',TQ,'H_90_77_GAP',90*r['gap'],'LINF_BOUND',r['gap']/(1+r['lam']))
    print('FULL_POLICY_COUNT_PER_EXHAUSTIVE_MODEL',2**18,'LR_POLICY_COUNT_PER_EXHAUSTIVE_MODEL',2**7)
    print('PASS_EXACT_R5_UPSTREAM_WEIGHTS_TIME_HULL_OPEN_CONE_AND_CLIP_CRITERION')
