#!/usr/bin/env python3
"""R749SOS/SOT exact rational certificate, Python 3 standard library only.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

S=Q(1,2)
MID=Q(5,22)
MASKS=(3,12,15,1,2,4,8)
V=[tuple((-1)**((k&m).bit_count()%2) for m in MASKS) for k in range(16)]

def law(t,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+t*a[0]+S*a[1]+h*a[2]+u*a[3]+v*a[4]+w*a[5]+z*a[6])/16 for a in V)

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),Q(0))/2

def pair(t):
    return law(t,0,t,t,S,1-t),law(t,0,-t,-t,-S,t-1)

def special(t):
    return law(t,t-S,w=-S-t,z=-S-t),law(t,t+S,w=t-S,z=t-S)

def zero(t):
    return law(t,Q(1,4)-3*t/2)

def cal(t):
    return law(t,t/3-Q(1,6))

def free(t):
    a=44*t-10
    return tuple((1-a)*x+a*y for x,y in zip(cal(MID),law(Q(7,16),Q(1,16))))

def solve(rows,rhs,ids):
    n=6
    a=[list(rows[i])+[rhs[i]] for i in ids]
    last=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None:
            return None
        if k!=j:
            a[j],a[k]=a[k],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for h in range(j+1,n+1):
                x=a[i][h]*p-v*a[j][h]
                assert x%last==0
                a[i][h]=x//last
            a[i][j]=0
        last=p
    if not a[-1][-2]:
        return None
    x=[Q(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(Q(a[j][n])-sum((a[j][h]*x[h] for h in range(j+1,n)),Q(0)))/a[j][j]
    return tuple(x)

def certificate(lo,hi,centers):
    rows=[(2*a[0],2*a[2],2*a[3],2*a[4],2*a[5],2*a[6]) for a in V]
    rhs=[-2-a[1] for a in V]
    rows.append((lo.denominator,0,0,0,0,0))
    rhs.append(lo.numerator)
    rows.append((-hi.denominator,0,0,0,0,0))
    rhs.append(-hi.numerator)
    found=set()
    nonsingular=feasible=0
    for ids in combinations(range(18),6):
        y=solve(rows,rhs,ids)
        if y is None:
            continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(row,y)),Q(0))<b for row,b in zip(rows,rhs)):
            continue
        feasible+=1
        found.add(y)
    assert found
    bounds={name:Q(-1) for name in centers}
    tight={name:0 for name in centers}
    endpoint={str(lo):0,str(hi):0,'interior':0}
    for y in found:
        t=y[0]
        p=law(*y)
        assert lo<=t<=hi and min(p)>=0 and sum(p)==1
        endpoint[str(t) if t in (lo,hi) else 'interior']+=1
        for name,(fn,radius) in centers.items():
            q=fn(t)
            assert min(q)>=0 and sum(q)==1
            err=tv(p,q)-radius(t)
            bounds[name]=max(bounds[name],err)
            tight[name]+=int(err==0)
            assert err<=0,(name,t,err)
    assert all(v==0 for v in bounds.values())
    return {'bases':comb(18,6),'nonsingular':nonsingular,'feasible_bases':feasible,
            'vertices':len(found),'endpoint_vertices':endpoint,
            'max_excess':{k:str(v) for k,v in bounds.items()},'tight':tight}

def proof_lower():
    for a,b in [(Q(1,6),MID),(MID,Q(1,4))]:
        signs=[]
        for t in (a,b):
            p,m=pair(t)
            assert min(p)>=0 and min(m)>=0
            assert tv(p,m)==(7-2*t)/8
            signs.append([(x>y)-(x<y) for x,y in zip(p,m)])
        assert all(x*y>=0 for x,y in zip(*signs))
    a,b=special(MID)
    q=cal(MID)
    sa=[(x>y)-(x<y) for x,y in zip(a,q)]
    sb=[(x>y)-(x<y) for x,y in zip(b,q)]
    assert set(sa)==set(sb)=={-1,1}
    for t in (MID,Q(23,100),Q(1,4)):
        p,m=special(t)
        assert min(p)>=0 and min(m)>=0
        for h in (Q(-1,2),Q(-1,11),Q(0),Q(1,2)):
            q=law(t,h)
            fa=sum((a*(x-y) for a,x,y in zip(sa,p,q)),Q(0))/2
            fb=sum((a*(x-y) for a,x,y in zip(sb,m,q)),Q(0))/2
            assert fa==Q(3,8)+t/4+h/4
            assert fb==Q(1,4)+t/2-h/2
    return {'pair_TV':'(7-2*t)/8',
     'cal_support_A':'3/8+t/4+h/4',
     'cal_support_B':'1/4+t/2-h/2',
     'cal_support_sign_A':sa,'cal_support_sign_B':sb}

def main():
    lower=proof_lower()
    first=certificate(Q(1,6),MID,{'both':(zero,lambda t:(7-2*t)/16)})
    second=certificate(MID,Q(1,4),{
        'free':(free,lambda t:(7-2*t)/16),
        'cal':(cal,lambda t:(1+t)/3)})
    return {'status':'PASS','research_ids':['R749SOS','R749SOT'],
        'frozen_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'zero_segment':'1/6<=t<=5/22: rho=rho_cal=(7-2*t)/16',
        'positive_segment':'5/22<=t<=1/4: rho=(7-2*t)/16, rho_cal=(1+t)/3',
        'positive_gap':'(22*t-5)/48','lower':lower,
        'joint_certificates':{'zero_segment':first,'positive_segment':second},
        'scope':'16-state frozen auxiliary Walsh source model; s=1/2; all real t in intervals',
        'review':'AUTHOR_EXACT_NOT_REVIEWED','native_bridge':'UNRESOLVED'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
