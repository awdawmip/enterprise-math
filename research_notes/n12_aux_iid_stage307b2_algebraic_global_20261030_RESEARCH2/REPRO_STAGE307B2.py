#!/usr/bin/env python3
"""Stage307-B.2 reproducible exact rational exterior certificate (auxiliary model)."""
from fractions import Fraction as Q
from math import comb
import json
P=(Q(61,160),Q(21,160),Q(9,160),Q(9,160))
bases=((Q(0),Q(23,100),Q(0),Q(1)),(Q(24,100),Q(1),Q(0),Q(1)),
       (Q(23,100),Q(24,100),Q(0),Q(55,100)),
       (Q(23,100),Q(24,100),Q(56,100),Q(1)))
w=(Q(231083940855,10**12),Q(555508857277,10**12))
U=Q(15116534475889766921898005231381567,1250000000000000000000000000000000000)
def b(k,z): return z**k*(1-z)**(3-k)
def r(k,x,y): return Q(4,5)*b(k,x)+Q(1,5)*b(k,y)-P[k]
def d(x,y): return sum((Q(comb(3,k),2)*abs(r(k,x,y)) for k in range(4)),Q(0))
def extrema(k,lo,hi):
    vals=[b(k,lo),b(k,hi)]
    if 0<k<3 and lo<=Q(k,3)<=hi: vals.append(b(k,Q(k,3)))
    return min(vals),max(vals)
def bounds(k,rect):
    xl,xr,yl,yr=rect
    lo1,hi1=extrema(k,xl,xr)
    lo2,hi2=extrema(k,yl,yr)
    return Q(4,5)*lo1+Q(1,5)*lo2-P[k],Q(4,5)*hi1+Q(1,5)*hi2-P[k]
def lower(rect):
    return sum((Q(comb(3,k),2)*max(Q(0),* (lambda a:(a[0],-a[1]))(bounds(k,rect)))
                for k in range(4)),Q(0))
def split(rect):
    a,b,c,d=rect
    if b-a>=d-c:
        m=(a+b)/2
        return (a,m,c,d),(m,b,c,d)
    m=(c+d)/2
    return (a,b,c,m),(a,b,m,d)
def sixth(a):
    return (Q(41,16)-4*a*a)**3-(Q(61,32)-4*a*a*a)**2
def check_local():
    a0,a1=Q(7689,10000),Q(769,1000)
    assert sixth(a0)<0<sixth(a1)
    assert a0>Q(45,100)
    for a in (a0,a1):
        B=Q(41,16)-4*a*a
        H=Q(61,32)-4*a*a*a
        assert Q(44,100)**2<B<Q(45,100)**2 and H>0
    x0,x1,y0,y1=Q(23,100),Q(24,100),Q(55,100),Q(56,100)
    region=x0,x1,y0,y1
    assert bounds(2,region)[0]>0 and bounds(3,region)[1]<0
    assert Q(12,5)*(1-x1)**2>Q(69,50)
    assert Q(12,5)*(1-x0)**2<Q(3,2)
    assert Q(3,5)*(1-y1)**2>Q(11,100)
    assert Q(3,5)*(1-y0)**2<Q(3,20)
    assert Q(4,5)*(1-x1)*(1-3*x1)>Q(17,100)
    assert Q(4,5)*(1-x0)*(1-3*x0)<Q(1,5)
    assert Q(1,5)*(1-y1)*(3*y0-1)>Q(57,1000)
    assert Q(1,5)*(1-y0)*(3*y1-1)<Q(7,100)
    assert Q(69,50)*Q(57,1000)+Q(11,100)*Q(17,100)>Q(9,100)
    assert Q(3,30)<Q(2,5) and Q(55,90)<Q(2,3)
    fx=lambda z:-Q(4,75)*(132*z*z-104*z+17)
    fy=lambda z:-Q(1,75)*(132*z*z-104*z+17)
    assert all(abs(fx(z))<Q(1,40) for z in (x0,x1))
    assert all(abs(fy(z))<Q(1,40) for z in (y0,y1))
    assert x1<Q(104,264)<y0
def main():
    assert d(*w)==U
    check_local()
    totals=[]
    leaves=[]
    maxdepth=0
    for region in bases:
        stack=[(region,'')]
        count=0
        region_leaves=[]
        while stack:
            rect,path=stack.pop()
            count+=1
            maxdepth=max(maxdepth,len(path))
            if lower(rect)>U:
                region_leaves.append(path)
                continue
            assert len(path)<100 and count<100000
            lo,hi=split(rect)
            stack.append((hi,path+'1'))
            stack.append((lo,path+'0'))
        assert sum((Q(1,2**len(path)) for path in region_leaves),Q(0))==1
        assert 2*len(region_leaves)-1==count
        totals.append((count,len(region_leaves)))
        leaves.append(sorted(region_leaves))
    payload={'schema':'EM_STAGE307B2_RATIONAL_EXTERIOR_COVER_V1',
             'base_rectangles':[[str(z) for z in region] for region in bases],
             'strict_lower_bound_threshold':str(U),'leaf_paths':leaves}
    with open('CERT_STAGE307B2.json','w',encoding='utf8') as f:
        json.dump(payload,f,sort_keys=True,separators=(',',':'))
        f.write('\n')
    print('OUTER_REGION_NODES_LEAVES',totals)
    print('OUTER_TOTAL_NODES',sum(c for c,l in totals))
    print('OUTER_TOTAL_LEAVES',sum(l for c,l in totals))
    print('MAX_DEPTH',maxdepth)
    print('ALGEBRAIC_ROOT_A_ISOLATED 7689/10000 769/1000')
    print('RISK_RATIONAL_WITNESS_UPPER',Q(5,8)*U)
    print('STAGE307B2_EXACT_ALGEBRAIC_GLOBAL_OPTIMUM_PASS')
if __name__=='__main__': main()
