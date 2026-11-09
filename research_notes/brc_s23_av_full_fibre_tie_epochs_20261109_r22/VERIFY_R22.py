#!/usr/bin/env python3
"""S23 R22: strict-rational interval certificate + translated tie-carrier epochs.
No floats, no external data, standard-library only. Separate proof in PROOF.md.
"""
from fractions import Fraction as Q
from bisect import bisect_right
from collections import Counter

LO=Q(262204504569236716045286,10**24)
HI=Q(262204504569236716045287,10**24)
M=128
N=493
A=(-43,164)      # a
B=(59,-225)      # b
C=(102,-389)     # c=b-a
D=(16,-61)       # d=a+b
H=( -11,42)      # H=phi_(25+42)-phi_25 clockwise
G=(-27,103)      # G=phi_103-phi_0 clockwise

def val(x, th):return x[0]+x[1]*th
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])

def modphase(k, th):return (k*th)%1
assert LO<HI
for th in (LO,HI):
    a,b,c,d=map(lambda z:val(z,th),(A,B,C,D))
    assert 0<a<c<b<d and a+b==d and b-a==c
    assert val(H,th)==a+2*d
    assert val(G,th)==a+d

# All relevant phase floors and orderings stable at both endpoints.
PHASE=[]
for j in range(N):
    fl=(j*LO)//1
    assert fl==(j*HI)//1
    PHASE.append((-fl,j))
VLO=[val(p,LO) for p in PHASE]
VHI=[val(p,HI) for p in PHASE]
ORDERLO=sorted(range(N), key=VLO.__getitem__)
assert ORDERLO==sorted(range(N), key=VHI.__getitem__)
HIST=sorted(range(M),key=VLO.__getitem__)
HIST_PHASE=[VLO[j] for j in HIST]

def gap(i,j,wrap):
    z=add(sub(PHASE[j],PHASE[i]),(int(wrap),0))
    assert all(0<val(z,th)<1 for th in (LO,HI))
    return z

def partition(t):
    order=sorted(range(t),key=VLO.__getitem__)
    assert order==sorted(range(t),key=VHI.__getitem__)
    arcs={j:[] for j in range(M)}
    for k,u in enumerate(order):
        v=order[(k+1)%t]
        g=gap(u,v,k==t-1)
        anch=HIST[(bisect_right(HIST_PHASE,VLO[u])-1)%M]
        arcs[anch].append((u,v,g))
    assert sum(len(seq) for seq in arcs.values())==t
    return arcs

def calc_risk(arcs):
    r=(1,0)
    for seq in arcs.values():
        winner=max(seq, key=lambda rec: val(rec[2],LO))[2]
        assert all(val(winner,HI)>=val(g,HI) for _,_,g in seq)
        r=sub(r,winner)
    return r

def fingerprint(arcs,owner):
    return [(u,v,g) for u,v,g in arcs[owner]]

# Historical adjacency via *one* global displacement-range certificate per family.
# For s=0..35, (25+s,67+s) has any candidate intruder k=j-(25+s)
# in [-60,102]. This excludes the only two small positive returns, -61 and 103.
for th in (LO,HI):
    assert all(modphase(k,th)>val(H,th) for k in range(-60,103) if k not in (0,42))
    assert modphase(-61,th)<val(H,th)  # j=s-36 first joins at s=36
    assert all(modphase(k,th)>val(G,th) for k in range(-24,128) if k not in (0,103))
    assert min(min(modphase(k,th),1-modphase(k,th)) for k in range(1,M))==val(D,th)

# As a redundant direct confirmation, the tested historical pairs are arcs.
for s in range(36):
    assert HIST[(HIST.index(25+s)+1)%M]==67+s
for s in range(25):
    assert HIST[(HIST.index(s)+1)%M]==103+s
for s in range(67):
    assert HIST[(HIST.index(61+s)+1)%M]==s
# s=36 loses 25+36 -> 67+36 adjacency to historical point phi_0.
assert HIST[(HIST.index(61)+1)%M]==0

BASE={
 (292,25):[(25,189,A),(189,128,D),(128,67,D)],
 (328,0):[(0,164,A),(164,103,D)],
 (353,25):[(25,189,A),(189,128,D),(128,292,A),(292,67,B)],
 (389,61):[(61,225,A),(225,0,B)],
 (456,25):[(25,189,A),(189,353,A),(353,128,B),(128,292,A),(292,67,B)],
 (492,0):[(0,164,A),(164,328,A),(328,103,B)]
}
for (t,o), expect in BASE.items():
    assert fingerprint(partition(t),o)==expect,(t,o,fingerprint(partition(t),o))

# General translated-fiber proof obligation: every base template has unchanged
# translated complete subpartition before its corresponding translated insertion.
# These assertions are optional independent data checks; interval proof above
# establishes historical adjacency without 36/25/67 separate searches.
EPOCHS=[
   (292,0,35,25,0,'PLATEAU_TIE_D'),
   (328,0,24,0,A,'SINGLE_D'),
   (353,0,35,25,A,'SECOND_D'),
   (389,0,66,61,A,'B_TO_C'),
   (456,0,35,25,0,'PLATEAU_TIE_B'),
]
prev=calc_risk(partition(292))
assert prev==(-4928,18796)
count=0
for t0,s0,s1,owner,delta,kind in EPOCHS:
    arc_base=BASE[(t0,owner)]
    for s in range(s0,s1+1):
        t=t0+s
        a0=partition(t)
        expected=[(u+s,v+s,length) for u,v,length in arc_base]
        assert a0[owner+s]==expected,(t,owner+s,a0[owner+s],expected)
        after=partition(t+1)
        r0=calc_risk(a0);r1=calc_risk(after)
        assert sub(r1,r0)==(delta if delta else (0,0)),(t,kind,r0,r1)
        assert r0==prev,(t,kind,r0,prev)
        prev=r1
        count+=1
    print('EPOCH',kind,'new_n=',t0+1,'..',t0+s1+1,'steps=',s1-s0+1,
          'increment=',delta if delta else (0,0),'end_risk=',prev)
assert count==200
assert prev==(-10432,39788)
assert calc_risk(partition(492))==(-10432,39788)
r493=calc_risk(partition(493))
assert sub(r493,prev)==A and r493==(-10475,39952)
print('ADJACENCY_CERTIFICATE: I25 family [-60,102], I0 family [-24,127], I61 min-return 1..127')
print('BASE_TEMPLATES',len(BASE),'FULL_SWEEP_UPDATES',count,'ENDPOINTS',LO,HI)
print('R_292=R_328=(-4928,18796); R_456=R_492=(-10432,39788); R_493=(-10475,39952)')
print('PASS_R22_TRANSLATED_MULTI_MAX_AND_THREE_GROWTH_FAMILIES')
