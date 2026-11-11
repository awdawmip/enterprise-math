#!/usr/bin/env python3
"""Exact 15-label phase-collision census on the frozen R5 P/Q-BRC observer.
Self-contained: standard library Fraction; integer Boolean-lattice DP.
Frozen inputs: original R5 PR #2102 (commit 435e77af0d180eac32bd1f9c4c464bc4010b7551).
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter

R=(2,10,15,20,25,30,38)
PORTS=(1,2,3,5)
J=(1,2,5)
V=tuple((i,j) for j in PORTS for i in range(7))
IX={v:k for k,v in enumerate(V)}
X=tuple(map(F,('250555781039/3397584400000,854053219229681/5470110884000000,'
 '155682221/156288882400000,1/800000,1/800000,19487331497/781444412000000,'
 '1001314300627/47566181600000,1/800000,6101786845061/95132363200000,'
 '19640941861/6795168800000,1/800000,1/800000,1/800000,1326387507069/95132363200000,'
 '155682221/25142124560000000,155682221/25142124560000000,'
 '969901373288483/5782688648800000,1627075388860003/11721666180000000,'
 '14139282599219/169879220000000,165067666637733/7814444120000000,'
 '1696529496568917/144567216220000000,31271973479/25142124560000000,'
 '12993863727852929/4047882054160000000,7517305745629/5782688648800000,'
 '36686587724849/3907222060000000,1308842702731/169879220000000,'
 '331925821992147/7814444120000000,54684907960963337/2023941027080000000').split(',')))
assert len(X)==28
x=X[IX[(0,3)]]
assert x==F(155682221,25142124560000000)
H=[0]*28
for i,a in [(1,-23),(2,28),(6,-5)]:
    H[IX[(i,3)]]=a
    H[IX[(i,1)]]=-a
assert sum(H)==0

def basis(i):
    a=[0]*7
    a[0]=R[i]-R[6]
    a[i]=R[6]-R[0]
    a[6]=R[0]-R[i]
    return a

def atom(j,i):
    a=[0]*28
    for k,v in enumerate(basis(i)):
        a[IX[(k,j)]]+=v
        a[IX[(k,3)]]-=v
    return a

coeff={1:(12,8,1,13,8),2:(3,13,7,4,2),5:(-15,-21,-8,-17,-10)}
steps=[tuple(c*v for v in atom(j,i)) for j in J for i,c in enumerate(coeff[j],1)]
assert len(steps)==15
S=1<<15
P=[[0]*28 for _ in range(S)]
for mask in range(1,S):
    t=mask&-mask
    j=t.bit_length()-1
    prev=P[mask^t]
    P[mask]=[prev[k]+steps[j][k] for k in range(28)]
epsmax=F(9,115400000)
assert min(X[k]+epsmax*F(P[-1][k],36) for k in range(28))==0


# Extension of immutable R5 28-coordinate/15-label frozen model.
# Scientific pins: GK a01383f825ef9d43b4b754254303298c64041568
# and EM 86149263e38c22292c9def1e0f69092efa1be77e.
# The exact prefix above is copied unchanged from PR #2123.
def min3(mask, r):
    p=P[mask]
    q=[]
    if p[7]<0:
        q.append((F(36*X[7],-p[7]),7))
    if p[14]<0:
        q.append((F(36*x,-p[14]),14))
    if p[15]<0:
        q.append((F(36*x*(1-23*r),-p[15]),15))
    return min(q) if q else None

def certify_chamber(lo, hi, expected):
    """All 32767 masks, 28 coordinates, two exact rational endpoints."""
    assert lo<hi
    middle=(lo+hi)/2
    masses=[[X[k]+t*x*H[k] for k in range(28)] for t in (lo,hi)]
    counts=Counter()
    for mask in range(1,S):
        p=P[mask]
        w=min3(mask,middle)
        if w is None or w[0]>epsmax:
            for mass in masses:
                assert all(mass[k]+epsmax*F(p[k],36)>0 for k in range(28)),(mask,"outside",lo,hi)
            counts["outside"]+=1
        else:
            _,winner=w
            counts[winner]+=1
            for mass in masses:
                t=F(36*mass[winner],-p[winner])
                assert t<=epsmax,(mask,"became_outside")
                for k in range(28):
                    if p[k]<0:
                        assert t<=F(36*mass[k],-p[k]),(mask,k,lo,hi)
    assert counts==Counter(expected),(lo,hi,counts)
    print("CHAMBER_CERTIFIED",lo,hi,dict(counts))

chambers=[
    (F(1,2507),F(1,1265),{14:14655,15:11004,7:299,"outside":6809}),
    (F(1,1265),F(5,5083),{14:14648,15:11011,7:299,"outside":6809}),
    (-F(1,2461),-F(1,4945),{14:14664,15:10995,7:299,"outside":6809}),
    (-F(1,1633),-F(1,2461),{14:14666,15:10993,7:299,"outside":6809})
]
for lo,hi,expected in chambers:
    certify_chamber(lo,hi,expected)

def wall_ties(r):
    hit=[]
    for mask in range(1,S):
        p=P[mask]
        if p[14]>=0 or p[15]>=0:continue
        t0=F(36*x,-p[14])
        t1=F(36*x*(1-23*r),-p[15])
        if t0==t1 and t0<=epsmax and min3(mask,r)[0]==t0:
            hit.append(mask)
    return hit

assert wall_ties(F(1,1265))==[6516,6714,18788,18986,23214,28732,30846]
assert wall_ties(-F(1,2461))==[10926,28966]
print("FIRST_POSITIVE_NEW_WALL",F(1,1265),"MASKS",wall_ties(F(1,1265)))
print("FIRST_NEGATIVE_NEW_WALL",-F(1,2461),"MASKS",wall_ties(-F(1,2461)))

def labels(r):
    tags=[("Z",0)]*S
    for mask in range(1,S):
        w=min3(mask,r)
        if w is None or w[0]>epsmax:
            tags[mask]=("O",0)
        else:
            k=w[1];p=P[mask]
            if k==7:tags[mask]=("E",0)
            elif k==14:tags[mask]=("F",-p[14])
            else:
                assert k==15 and (-p[15])%36==0
                tags[mask]=("Q",(-p[15])//36)
    return tags

def time_over_x(tag,r):
    kind,n=tag
    if kind=="O":return epsmax/x+1
    if kind=="E":return epsmax/x
    if kind=="F":return F(36,n)
    if kind=="Q":return F(1-23*r,n)
    raise AssertionError(tag)

def path_count(tags,r,theta,inclusive):
    values=[time_over_x(t,r) for t in tags]
    ways=[0]*S;ways[0]=1
    for mask in range(1,S):
        permitted=(values[mask]>=theta) if inclusive else (values[mask]>theta)
        if not permitted:continue
        b=mask;v=0
        while b:
            least=b&-b
            v+=ways[mask^least]
            b-=least
        ways[mask]=v
    return ways[-1]

def drop(r,kind,n,tags):
    theta=F(36,n) if kind=="F" else F(1-23*r,n)
    return path_count(tags,r,theta,True)-path_count(tags,r,theta,False)

def crossing(a,mid,b,n,q):
    ra=(a+mid)/2; rb=(mid+b)/2
    ta,tb=labels(ra),labels(rb)
    ca=(drop(ra,"F",n,ta),drop(ra,"Q",q,ta))
    cb=(drop(rb,"F",n,tb),drop(rb,"Q",q,tb))
    assert sum(ca)==sum(cb)
    print("CROSSING",mid,"FIXED",n,"MOVING",q,"BEFORE",ca,"AFTER",cb,
          "TRANSFER_TO_MOVING_IN_INCREASING_R",cb[1]-ca[1],"TOTAL",sum(ca))
    return ca,cb

pos=crossing(F(1,2507),F(1,1265),F(5,5083),110,3)
neg=crossing(-F(1,1633),-F(1,2461),-F(1,4945),107,3)
assert pos==((216738876,12939867720),(193333788,12963272808))
assert neg==((126633932,12847872840),(83034876,12891471896))
assert sum(pos[0])==13156606596
assert sum(neg[0])==12974506772

for lo,hi,_ in chambers:
    for r in (lo,hi):
        assert min(X[k]+r*x*H[k] for k in range(28))>0
        assert min(X[k]+r*x*H[k]+epsmax*F(P[-1][k],36) for k in range(28))==0
print("PASS_R5_EXACT_NEXT_TWO_AFFINE_WALLS_AND_ORDER_TRANSFER")


# Further outward adjacent closed chambers: +5/5083 -> +1/851,
# and -1/1219 -> -1/1633. Both are full 28-coordinate certificates.
certify_chamber(F(5,5083),F(1,851),
                {14:14646,15:11013,7:299,"outside":6809})
certify_chamber(-F(1,1219),-F(1,1633),
                {14:14667,15:10992,7:299,"outside":6809})
assert wall_ties(F(5,5083))==[14597,31509]
assert wall_ties(-F(1,1633))==[15109]
print("SECOND_POSITIVE_NEW_WALL",F(5,5083),"MASKS",wall_ties(F(5,5083)))
print("SECOND_NEGATIVE_NEW_WALL",-F(1,1633),"MASKS",wall_ties(-F(1,1633)))

def immediate_crossing(wall,left,right,pairs,expected):
    """Take nearest F/Q phase collision on either side, not a distant sample."""
    assert left<wall<right
    midway=(left+wall)/2
    t=labels(midway)
    ns={n for typ,n in t if typ=="F"}
    qs={q for typ,q in t if typ=="Q"}
    all_crossings=sorted({F(n-36*q,23*n) for n in ns for q in qs})
    before=max([left]+[v for v in all_crossings if left<v<wall])
    after=min([right]+[v for v in all_crossings if wall<v<right])
    sample_before=(before+wall)/2
    sample_after=(after+wall)/2
    tags_before=labels(sample_before)
    tags_after=labels(sample_after)
    actual_pairs=sorted((n,q) for n in ns for q in qs if F(n-36*q,23*n)==wall)
    assert actual_pairs==sorted(pairs),(wall,actual_pairs)
    print("SIMULTANEOUS_PHASE_PAIRS",wall,actual_pairs,
          "NEIGHBOR_PHASE_ROOTS",before,after)
    for n,q in pairs:
        a=(drop(sample_before,"F",n,tags_before),
           drop(sample_before,"Q",q,tags_before))
        b=(drop(sample_after,"F",n,tags_after),
           drop(sample_after,"Q",q,tags_after))
        assert (a,b)==expected[(n,q)],(wall,(n,q),a,b)
        assert sum(a)==sum(b)
        print("IMMEDIATE_TRANSFER",wall,"F",n,"Q",q,
              "BEFORE",a,"AFTER",b,
              "TO_MOVING_IN_INCREASING_R",b[1]-a[1],"PAIR_TOTAL",sum(a))

immediate_crossing(
    F(1,1265),F(1,2507),F(5,5083),
    [(110,3),(440,12),(550,15)],
    {(110,3):((216738876,12939867720),(193333788,12963272808)),
     (440,12):((936566072,140525965632),(805044224,140657487480)),
     (550,15):((956531904,383921342928),(695889312,384181985520))})
immediate_crossing(
    -F(1,2461),-F(1,1633),-F(1,4945),
    [(107,3),(428,12),(535,15)],
    {(107,3):((126633932,12847872840),(83034876,12891471896)),
     (428,12):((657640968,137055984032),(501071304,137212553696)),
     (535,15):((1929707664,377728635456),(880505088,378777838032))})
immediate_crossing(
    F(5,5083),F(1,1265),F(1,851),
    [(442,12)],
    {(442,12):((338727248,140996629764),(227619620,141107737392))})
immediate_crossing(
    -F(1,1633),-F(1,1219),-F(1,2461),
    [(426,12)],
    {(426,12):((746030624,136660470420),(545161644,136861339400))})
print("PASS_R5_SIX_CLOSED_AFFINE_CHAMBERS_EIGHT_PHASE_COLLISION_TRANSFERS")
