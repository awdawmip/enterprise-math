#!/usr/bin/env python3
"""R749SOW: upper first-onset exact trapezoid, 7D Bareiss certificate.
Source model: frozen 16-atom auxiliary Walsh source observer.
Requires Python 3 standard library only. May take >1 minute.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

T0=Q(5,22);T1=Q(1,4);S0=Q(49,100);S1=Q(1,2); S2=Q(103,200)
def threshold(s):return (1+3*s)/11
def roof(s):return (614-820*s)/825
MASKS=(3,12,15,1,2,4,8)
W=[tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16)]
ZERO=[Q(0)]*16

Q00=list(map(Q,['19/200','1569/17600','289/4400','1781/17600','5/88','1/88','211/8800','5/88','5/88','5/176','61/8800','5/88','1291/17600','289/8800','1609/17600','27/176']))
DT=list(map(Q,['0','0','-29/8800','0','1/176','0','-3/550','27/8800','27/8800','-87/8800','39/8800','1/176','171/8800','-7/4400','-1/44','7/4400']))
DS=list(map(Q,['-1/800','219/17600','-1/400','-131/17600','0','-1/800','0','0','0','0','-1/800','0','197/17600','0','-197/17600','1/800']))

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+t*a+s*b+h*c+u*d+v*e+w*f+z*g)/16 for a,b,c,d,e,f,g in W)
def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),Q(0))/2

def qfree(t,s):
    x=(t-T0)/(T1-T0);y=(s-S0)/(S1-S0)
    return tuple(a+x*b+y*c for a,b,c in zip(Q00,DT,DS))

def qcal(t,s):return law(t,s,(1+t)/3-s)

def free_radius(t,s):return (3-t+s)/8

def cal_radius(t,s):return (1+t)/3

def pair(t,s):return law(t,s,0,-t,-t,1-t,s),law(t,s,0,t,t,t-1,-s)

def cal_witness(t,s):
    return law(t,s,-t,w=-s-t,z=t-1), law(t,s,1+t-s,w=t-s,z=t-s)

def solve(rows,rhs,idx):
    n=7
    a=[list(rows[i])+[rhs[i]] for i in idx]
    last=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for k in range(j+1,n+1):
                z=a[i][k]*p-v*a[j][k]
                assert z%last==0
                a[i][k]=z//last
            a[i][j]=0
        last=p
    if not a[-1][-2]:return None
    x=[Q(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(Q(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),Q(0)))/a[j][j]
    return tuple(x)

def lower_checks():
    corners=[(t,s) for s in (S1,S2) for t in (threshold(s),roof(s))]
    pp_signs=[];a_sign=[];b_sign=[]
    for t,s in corners:
        p,n=pair(t,s);a,b=cal_witness(t,s)
        for z in (p,n,a,b):
            assert min(z)>=0 and sum(z)==1
        assert tv(p,n)==2*free_radius(t,s)
        pp_signs.append(tuple((x>y)-(x<y) for x,y in zip(p,n)))
        center=qcal(t,s)
        a_sign.append(tuple((x>y)-(x<y) for x,y in zip(a,center)))
        b_sign.append(tuple((x>y)-(x<y) for x,y in zip(b,center)))
    assert all(x*y>=0 for z in pp_signs[1:] for x,y in zip(pp_signs[0],z))
    sa=a_sign[-1];sb=b_sign[-1]
    for t,s in corners:
        a,b=cal_witness(t,s)
        for h in (Q(-1,2),Q(0),Q(1,2)):
            q=law(t,s,h)
            la=sum((u*(x-y) for u,x,y in zip(sa,a,q)),Q(0))/2
            lb=sum((u*(x-y) for u,x,y in zip(sb,b,q)),Q(0))/2
            assert la==(h+s+t+1)/4
            assert lb==(1+t-s-h)/2
    return {'free_pair_TV':'(3-t+s)/4','cal_event_A':'(h+s+t+1)/4',
            'cal_event_B':'(1+t-s-h)/2',
            'cal_optimal_h':'(1+t)/3-s',
            'cal_A_sign':sa,'cal_B_sign':sb}

def vertex_certificate():
    # Every source atom imposes signrow . (t,s,h,u,v,w,z) >= -1.
    rows=list(W);rhs=[-1]*16
    rows.extend([(0,2,0,0,0,0,0),(0,-200,0,0,0,0,0),
                 (11,-3,0,0,0,0,0),(-825,-820,0,0,0,0,0)])
    rhs.extend([1,-103,1,-614])
    seen=set();nonsing=feasible=0
    for idx in combinations(range(20),7):
        y=solve(rows,rhs,idx)
        if y is None:continue
        nonsing+=1
        if any(sum((u*v for u,v in zip(row,y)),Q(0))<b for row,b in zip(rows,rhs)):
            continue
        feasible+=1;seen.add(y)
    assert seen
    maxfree=maxcal=Q(-1)
    endpoint={}
    for v in seen:
        t,s=v[:2];p=law(*v)
        f=qfree(t,s);c=qcal(t,s)
        assert min(p)>=0 and sum(p)==1
        assert min(f)>=0 and sum(f)==1
        assert min(c)>=0 and sum(c)==1
        xf=tv(p,f)-free_radius(t,s)
        xc=tv(p,c)-cal_radius(t,s)
        assert xf<=0,(t,s,xf)
        assert xc<=0,(t,s,xc)
        maxfree=max(maxfree,xf);maxcal=max(maxcal,xc)
        key=f'{t}|{s}'
        endpoint[key]=endpoint.get(key,0)+1
    assert maxfree==maxcal==0
    assert len(seen)==sum(endpoint.values())
    return {'bases':comb(20,7),'nonsingular':nonsing,'feasible_bases':feasible,
            'unique_vertices':len(seen),'parameter_endpoints':endpoint,
            'max_excess_free':str(maxfree),'max_excess_calibrated':str(maxcal)}

def main():
    low=lower_checks();upper=vertex_certificate()
    return {'status':'PASS','research_id':'R749SOW',
     'frozen_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
     'parameter_trapezoid':'1/2<=s<=103/200, (1+3s)/11<=t<=(614-820s)/825',
     'rho_free':'(3-t+s)/8','rho_calibrated':'(1+t)/3',
     'gap':'(11*t-3*s-1)/24','area':'63/400000','zero_edge':'11*t-3*s=1',
     'lower':low,'joint_vertex_certificate':upper,
     'scope':'all real t,s in upper-onset trapezoid, auxiliary Walsh model',
     'review':'AUTHOR_EXACT_NOT_REVIEWED', 'native_bridge':'OPEN'}
if __name__=='__main__':print(json.dumps(main(),sort_keys=True,indent=2))
