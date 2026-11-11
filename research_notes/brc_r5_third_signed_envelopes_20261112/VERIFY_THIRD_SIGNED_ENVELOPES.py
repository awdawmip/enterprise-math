#!/usr/bin/env python3
"""R5: third exact signed affine-prefix cells; exact rational and integer DP."""
from pathlib import Path
from runpy import run_path
from fractions import Fraction as F
from collections import Counter

# The original fixed scientific fixture is at the pinned ancestor commit
# 435e77af0d180eac32bd1f9c4c464bc4010b7551.
parent = (Path(__file__).resolve().parent.parent
          / "brc_r5_sharp_nonlocal_fifteen_ray_20261111"
          / "VERIFY_R5_SHARP_RAY.py")
assert parent.is_file()
z = run_path(str(parent))
X, IX, steps, D, eps_max, obs = (z[k] for k in
                                ("X", "IX", "steps", "D", "eps_max", "obs"))
x = X[IX[(0, 3)]]
assert x == F(155682221, 25142124560000000)
assert eps_max == F(9,115400000)
H = [0]*28
for i,v in ((1,-23),(2,28),(6,-5)):
    H[IX[(i,3)]] = v
    H[IX[(i,1)]] = -v
assert not any(obs(H))

atoms = [tuple(int(36*a*v) for v in h) for j,i,a,h in steps]
assert len(atoms)==15 and all(len(h)==28 for h in atoms)
size=1<<15
P=[(0,)*28]+[None]*(size-1)
for s in range(1,size):
    bit=s&-s
    j=bit.bit_length()-1
    P[s]=tuple(P[s^bit][k]+atoms[j][k] for k in range(28))

# For each nonempty prefix mask s, the first capacity hit is the
# lower envelope of these exact affine lines in r=eta/x.
lines=[()]
for s in range(1,size):
    lines.append(tuple(
        (k, F(36)*X[k]/(-v), F(36)*x*H[k]/(-v))
        for k,v in enumerate(P[s]) if v<0
    ))
    assert lines[s]

def next_cell(start,sign):
    first=None
    switches=[]
    at_start_ties=[]
    for s in range(1,size):
        ls=lines[s]
        val=min(a+start*b for k,a,b in ls)
        winners=[(k,a,b) for k,a,b in ls if a+start*b==val]
        if len({b for k,a,b in winners})>1:
            at_start_ties.append(s)
        k0,a0,b0=(min(winners,key=lambda v:v[2]) if sign>0
                  else max(winners,key=lambda v:v[2]))
        for k,a,b in ls:
            if (b<b0 if sign>0 else b>b0):
                r=(a0-a)/(b-b0)
                if (r>start if sign>0 else r<start):
                    if first is None or (r<first if sign>0 else r>first):
                        first=r;switches=[(s,k0,k)]
                    elif r==first:
                        switches.append((s,k0,k))
    return first,at_start_ties,sorted(set(switches))

def tags(r):
    ts=[None]*size
    for s in range(1,size):
        k,a,b=min(lines[s],key=lambda v:v[1]+r*v[2])
        t=a+r*b
        if t>eps_max:out=("O",0)
        elif t==eps_max:out=("E",0)
        elif b:
            q=x/a
            assert q.denominator==1 and b==-23*a
            out=("Q",int(q))
        else:
            n=36*x/a
            assert n.denominator==1
            out=("F",int(n))
        ts[s]=out
    return ts

def check_endpoint(lo,hi):
    for r in (lo,hi):
        initial=[X[k]+x*r*H[k] for k in range(28)]
        final=[initial[k]+eps_max*D[k] for k in range(28)]
        assert min(initial)>0 and min(final)>=0
        assert final[IX[(0,2)]]==0

def count_orders(ts,r,threshold,inclusive):
    allow=[True]*size
    scale=1-23*r
    for s in range(1,size):
        typ,n=ts[s]
        if typ=="O":continue
        t=(eps_max/x if typ=="E" else
           F(36,n) if typ=="F" else scale/n)
        allow[s]=(t>=threshold if inclusive else t>threshold)
    ways=[0]*size;ways[0]=1
    for s in range(1,size):
        if allow[s]:
            u=s;ans=0
            while u:
                bit=u&-u
                ans+=ways[s^bit]
                u-=bit
            ways[s]=ans
    return ways[-1]

def loss(ts,r,typ,n):
    t=F(36,n) if typ=="F" else (1-23*r)/n
    return count_orders(ts,r,t,True)-count_orders(ts,r,t,False)

def run_side(start,sign,expected_end,expected_masks,expected_transfers):
    end,ties,masks=next_cell(start,sign)
    assert end==expected_end and masks==expected_masks,(end,masks)
    check_endpoint(start,end)
    midpoint=(start+end)/2
    t=tags(midpoint)
    types=Counter(a for a,b in t[1:])
    fixed={n for a,n in t[1:] if a=="F"}
    moving={q for a,q in t[1:] if a=="Q"}
    assert len(fixed)==1144 and moving=={3,12,15}
    assert types["O"]==6809 and types["E"]==299
    events=sorted((F(n-36*q,23*n),q,n)
                  for q in moving for n in fixed
                  if min(start,end)<F(n-36*q,23*n)<max(start,end))
    if sign<0:events.reverse()
    assert len(events)==3
    points=[start]+[r for r,q,n in events]+[end]
    print("DIRECTION",sign,"PREVIOUS",start,"NEXT",end)
    print("START_TIED_MASKS",ties)
    print("NEXT_COORDINATE_SWITCHES",masks)
    print("CHAMBER_TAG_COUNTS",sorted(types.items()))
    print("FIXED_FORMS",len(fixed),"MOVING",sorted(moving))
    transfers=[]
    for i,(r,q,n) in enumerate(events,1):
        before=(points[i-1]+r)/2
        after=(points[i+1]+r)/2
        old=(loss(t,before,"F",n),loss(t,before,"Q",q))
        new=(loss(t,after,"F",n),loss(t,after,"Q",q))
        assert sum(old)==sum(new)
        move=new[1]-old[1]
        transfers.append(move)
        print("COLLISION",r,"Q",q,"F",n,"BEFORE",old,
              "AFTER",new,"TRANSFER_TO_Q",move)
    assert transfers==expected_transfers,transfers
    last=count_orders(t,midpoint,eps_max/x,True)
    assert last==3514190816,last
    print("FULL_RAY_VALID_LABELED_ORDERS",last)
    boundary_pairs=[(q,int(n)) for q in moving
                    for n in [F(36*q,1-23*end)] if n.denominator==1]
    print("BOUNDARY_MOVING_FIXED_COINCIDENCES",sorted(boundary_pairs))
    return t

positive=run_side(F(1,1265),1,F(5,5083),
                  [(14597,14,15),(31509,14,15)],
                  [268206336,339142284,80117424])
negative=run_side(F(-1,2461),-1,F(-1,1633),
                  [(15109,15,14)],
                  [-63350880,-194644632,-179781408])

old_pos=tags((F(1,2507)+F(1,1265))/2)
old_neg=tags((F(-1,4945)+F(-1,2461))/2)
assert sum(a!=b for a,b in zip(old_pos,positive))==7
assert sum(a!=b for a,b in zip(old_neg,negative))==2
print("POSITIVE_CROSSED_MASK_TAG_CHANGES",7)
print("NEGATIVE_CROSSED_MASK_TAG_CHANGES",2)
print("PASS_R5_THIRD_SIGNED_AFFINE_CELLS_AND_SIX_LOSS_TRANSFERS")
