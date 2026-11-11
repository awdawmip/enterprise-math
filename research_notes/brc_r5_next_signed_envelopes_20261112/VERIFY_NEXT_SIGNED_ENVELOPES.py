#!/usr/bin/env python3
"""R5: sharp next two signed affine-prefix envelopes and ten collision transfers.

Run from an enterprise-math checkout containing the immutable parent at
research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py.
Parent scientific bytes: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
This checker is not a native X6 dynamics computation.
"""
from pathlib import Path
from runpy import run_path
from fractions import Fraction as F
from collections import Counter

source=(Path(__file__).resolve().parent.parent
        /"brc_r5_sharp_nonlocal_fifteen_ray_20261111"/"VERIFY_R5_SHARP_RAY.py")
assert source.is_file(), ("Missing frozen parent verifier",str(source))
original=run_path(str(source))
for key in ("X","IX","R","V","J","PORTS","steps","D","eps_max","obs"):
    globals()[key]=original[key]

H=[0]*28
for target,val in ((1,-23),(2,28),(6,-5)):
    H[IX[(target,3)]]=val
    H[IX[(target,1)]]=-val
x=X[IX[(0,3)]]
assert x==F(155682221,25142124560000000) and not any(obs(H))
size=1<<len(steps)
step_int=[tuple(int(36*a*v) for v in z) for _,_,a,z in steps]
P=[[0]*28 for _ in range(size)]
for mask in range(1,size):
    bit=mask&-mask
    j=bit.bit_length()-1
    prev=P[mask^bit]
    P[mask]=[prev[k]+step_int[j][k] for k in range(28)]

def lines(mask):
    for k,v in enumerate(P[mask]):
        if v<0:
            yield (k,F(36)*X[k]/(-v),F(36)*x*H[k]/(-v))

def next_envelope(start,sign):
    candidates=[];ties=[]
    for mask in range(1,size):
        rows=list(lines(mask))
        time=min(a+start*b for k,a,b in rows)
        winners=[(k,a,b) for k,a,b in rows if a+start*b==time]
        if len(set(b for k,a,b in winners))>1:ties.append(mask)
        win=(min(winners,key=lambda z:z[2]) if sign>0
             else max(winners,key=lambda z:z[2]))
        wk,wa,wb=win
        for k,a,b in rows:
            if (b<wb if sign>0 else b>wb):
                r=(wa-a)/(b-wb)
                if (r>start if sign>0 else r<start):
                    candidates.append((r,mask,wk,k))
    point=(min if sign>0 else max)(z[0] for z in candidates)
    masks=sorted(set(mask for r,mask,wk,k in candidates if r==point))
    return point,ties,masks

pos=next_envelope(F(1,2507),1)
neg=next_envelope(F(-1,4945),-1)
assert pos==(F(1,1265),[11236,29474],
             [6516,6714,18788,18986,23214,28732,30846]),pos
assert neg==(F(-1,2461),[14357,26629],[10926,28966]),neg
print("POSITIVE_NEXT_PREFIX_ENVELOPE",pos)
print("NEGATIVE_NEXT_PREFIX_ENVELOPE",neg)

def tags(r):
    result=[None]*size
    for mask in range(1,size):
        k,a,b=min(lines(mask),key=lambda z:z[1]+r*z[2])
        t=a+r*b
        if t>eps_max:v=('O',0)
        elif t==eps_max:v=('E',0)
        elif b:
            q=x/a
            assert q.denominator==1 and b==-23*a
            v=('Q',int(q))
        else:
            n=36*x/a
            assert n.denominator==1
            v=('F',int(n))
        result[mask]=v
    return result

def spectrum_inside(r):
    ts=tags(r)
    unique=set(ts[1:]);counts=Counter(t[0] for t in ts[1:])
    assert len(unique)==1149 and counts['O']==6809 and counts['E']==299
    fixed={n for kind,n in unique if kind=='F'}
    moving={n for kind,n in unique if kind=='Q'}
    assert len(fixed)==1144 and moving=={3,12,15}
    return ts,fixed,counts

plus,fp,cp=spectrum_inside(F(1,1886))
minus,fm,cm=spectrum_inside(F(-1,3500))
assert fp==fm
assert min(X[k]+r*x*H[k] for r in
           (F(1,2507),F(1,1265),F(-1,4945),F(-1,2461))
           for k in range(28))>0
assert min(X[k]+r*x*H[k]+eps_max*D[k] for r in
           (F(1,2507),F(1,1265),F(-1,4945),F(-1,2461))
           for k in range(28))>=0
print("INSIDE_CHAMBER_TAG_COUNTS",cp,cm)

def collisions(lo,hi,fixed):
    return sorted((F(n-36*q,23*n),q,n) for q in (3,12,15) for n in fixed
                  if lo<F(n-36*q,23*n)<hi)

pos_events=collisions(F(1,2507),F(1,1265),fp)
neg_events=collisions(F(-1,2461),F(-1,4945),fm)
assert pos_events==[(F(1,2093),15,546),(F(5,10051),12,437),
 (F(7,12581),15,547),(F(1,1679),12,438),(F(2,3151),15,548),
 (F(7,10097),12,439),(F(1,1403),15,549)]
assert neg_events==[(F(-1,3082),15,536),
 (F(-1,3289),12,429),(F(-1,4117),15,537)]
print("NEW_POSITIVE_COLLISIONS",[(str(r),q,n) for r,q,n in pos_events])
print("NEW_NEGATIVE_COLLISIONS",[(str(r),q,n) for r,q,n in neg_events])

def schedule_count(ts,r,threshold,inclusive):
    bound=F(1)-23*r
    allow=[True]*size
    for mask in range(1,size):
        kind,n=ts[mask]
        if kind=='O':continue
        value=eps_max/x if kind=='E' else F(36,n) if kind=='F' else bound/n
        allow[mask]=(value>=threshold if inclusive else value>threshold)
    dp=[0]*size;dp[0]=1
    for mask in range(1,size):
        if allow[mask]:
            z=0;m=mask
            while m:
                bit=m&-m;z+=dp[mask^bit];m-=bit
            dp[mask]=z
    return dp[-1]

def loss(ts,r,kind,n):
    t=F(36,n) if kind=='F' else (F(1)-23*r)/n
    return schedule_count(ts,r,t,True)-schedule_count(ts,r,t,False)

def validate_events(ts,events,start,end):
    seq=(events if start<end else list(reversed(events)))
    points=[start]+[r for r,q,n in seq]+[end]
    transfers=[]
    for i,(r,q,n) in enumerate(seq,1):
        before=(points[i-1]+r)/2
        after=(points[i+1]+r)/2
        pre=(loss(ts,before,'F',n),loss(ts,before,'Q',q))
        post=(loss(ts,after,'F',n),loss(ts,after,'Q',q))
        assert sum(pre)==sum(post)
        transfers.append(post[1]-pre[1])
        print("NEW_COLLISION",r,"Q",q,"F",n,
              "BEFORE",pre,"AFTER",post,"TRANSFER",transfers[-1])
    return transfers

transfers_pos=validate_events(plus,pos_events,F(1,2507),F(1,1265))
transfers_neg=validate_events(minus,neg_events,F(-1,4945),F(-1,2461))
assert transfers_pos==[27345600,817628752,1336050192,44684640,
                      333390528,135540768,337459680]
assert transfers_neg==[-88495488,-344005152,-266265216]
assert schedule_count(plus,F(1,1886),eps_max/x,True)==3514190816
assert schedule_count(minus,F(-1,3500),eps_max/x,True)==3514190816
print("PASS_R5_NEXT_TWO_AFFINE_ENVELOPES_AND_10_COLLISION_TRANSFERS")
