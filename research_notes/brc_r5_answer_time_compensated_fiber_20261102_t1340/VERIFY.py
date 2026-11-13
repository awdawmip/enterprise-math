"""Exact finite-vertex certificates for R5 compensated answer/time source fibers."""
from fractions import Fraction as F
from itertools import product

S = ("C", "I", "BJ", "IJ")
M = dict(zip(S, (F(1,4), F(1,4), F(1,8), F(1,8))))
ZERO, ONE = F(0), F(1)

def observer(policy, answer, p, q):
    x, jB, jI, kC, kI, kBJ, kIJ = map(F, policy)
    k = dict(zip(S, (kC, kI, kBJ, kIJ)))
    ep = eq = tp = tq = ZERO
    # I: initial half-mass; an I stop answers P at time 1.
    ep += F(1,2)*x
    tp += F(1,2)*x
    tq += F(1,2)*x
    # J: origins B and I, direct terminal branch has mass half of continuation.
    arrivals = {"B": F(1,4), "I": (ONE-x)*F(1,4)}
    masses = {"C": F(1,4), "I": (ONE-x)*F(1,4)}
    for origin, stop in (("B",jB),("I",jI)):
        w = arrivals[origin]
        ep += w*stop
        tp += 2*w*stop
        tq += 2*w*stop
        direct = w*(ONE-stop)/2
        ep += F(3,5)*direct
        eq += F(3,5)*direct # Q(answer Q)=3/5
        tp += 3*direct
        tq += 3*direct
        masses["BJ" if origin=="B" else "IJ"] = direct
    # K: stop answers P at time3; continue answers P at 4 or5.
    for s in S:
        w = masses[s]
        z = k[s]
        ep += w*(z+(ONE-z)*answer[s])
        eq += w*(ONE-z)*(ONE-answer[s])
        tp += w*(3*z+(ONE-z)*(4+p[s]))
        tq += w*(3*z+(ONE-z)*(4+q[s]))
    return ep,eq,tp,tq

def corners(a,p,q):
    full = {v:observer(v,a,p,q) for v in product((0,1),repeat=7)}
    lr = {v:observer((v[0],v[1],v[1],v[2],v[2],v[2],v[2]),a,p,q)
          for v in product((0,1),repeat=3)}
    return full,lr

def dot(n,v): return sum((x*y for x,y in zip(n,v)),ZERO)
def agree(x,y):
    global checks
    checks += 1
    assert x==y, (x,y)

checks=0
# A genuine all-positive compensated example: answer-varying sources with
# (1+p_s)/(1-a_s)=3 and (1+q_s)/(1-a_s)=7/2 for every source.
a = dict(zip(S,(F(1,2),F(9,16),F(3,5),F(7,12))))
p = {s:3*(ONE-a[s])-1 for s in S}
q = {s:F(7,2)*(ONE-a[s])-1 for s in S}
for s in S:
    agree((ONE+p[s])/(ONE-a[s]),F(3))
    agree((ONE+q[s])/(ONE-a[s]),F(7,2))
    agree(ZERO<a[s]<ONE and ZERO<p[s]<ONE and ZERO<q[s]<ONE,True)
full,lr=corners(a,p,q)
agree(len(full),128);agree(len(lr),8)
U0,U1=lr[(0,0,0)],lr[(0,0,1)]
upper=[v for v in full if v[:3]==(0,0,0)]
for v in upper:
    w=full[v]
    alpha=(w[0]-U0[0])/(U1[0]-U0[0])
    agree(ZERO<=alpha<=ONE,True)
    agree(w,tuple(u+alpha*(vv-u) for u,vv in zip(U0,U1)))
for v,w in full.items():
    agree(w[0]+w[1] <= F(21,20), True)
for v,w in lr.items():
    agree(w[0]+w[1] <= F(21,20), True)
N=(-823,-823,-823,822)
W=full[(0,1,0,0,0,0,0)]
fl=max(dot(N,v) for v in full.values())
sl=max(dot(N,v) for v in lr.values())
agree(sl,F(-5839,8));agree(fl,F(-14589,20))
agree(fl-sl,F(17,40))
agree(W,(F(637,960),F(347,960),F(231,64),F(1441,384)))
agree(dot(N,W)-sl,F(17,40))
print("COMPENSATED: ratios (P,Q)=(3,7/2); all 16 FULL upper-face corners on LR edge")
print("COMPENSATED: LR support",sl,"FULL support",fl,"gap",fl-sl)
print("COMPENSATED: witness",W,"normal",N,"distance bound",(fl-sl)/sum(map(abs,N)))

# One-source answer-kernel change: all K time kernels remain source-independent.
# At delta=0 actual real behavioral images coincide by source-flow aggregation.
for delta in (F(-1,4), F(-1,8), F(0), F(1,16), F(1,8), F(1,4)):
    ans={s:F(1,2) for s in S};ans["C"]+=delta
    pp={s:F(1,2) for s in S};qq={s:F(1,3) for s in S}
    f,l=corners(ans,pp,qq)
    agree(max(w[0]+w[1] for w in l.values()),F(21,20))
    if delta:
        sigma=ONE if delta<0 else -ONE
        r=sigma*F(9)/(3-2*delta)
        n=(400+r,F(400),sigma,ZERO)
        goal=F(3,2)*abs(delta)/(3-2*delta)
        lw=max(dot(n,w) for w in l.values())
        fw=max(dot(n,w) for w in f.values())
        agree(lw,dot(n,l[(0,0,0)]))
        agree(lw,dot(n,l[(0,0,1)]))
        agree(fw-lw,goal)
        single=f[(0,0,0,1,0,0,0)]
        agree(dot(n,single)-lw,goal)
        print("ONE-SOURCE delta",delta,"support gap",fw-lw,"normal",n)
    else:
        for v,w in f.items():
            x,jb,ji,kc,ki,kbj,kij=map(F,v)
            totalJ=(2-x)/4
            y=(jb/4+(ONE-x)*ji/4)/totalJ
            wk=(F(1,4), (ONE-x)/4, (ONE-jb)/8, (ONE-x)*(ONE-ji)/8)
            z=sum(t*zz for t,zz in zip(wk,(kc,ki,kbj,kij)))/sum(wk)
            agree(w,observer((x,y,y,z,z,z,z),ans,pp,qq))
print("PASS_EXACT_R5_COMPENSATED_UPPER_FIBER_AND_MIXED_FACET",checks,"exact assertions")
