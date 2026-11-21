"""Exploratory floating evaluation of the exact two-variable formula."""
import math,json,time
from pathlib import Path
from itertools import combinations
import numpy as np
from line_kernel import load_terms

TERMS=[(p,float(c))for p,c in load_terms()]
PAIRS={p:tuple((b[0]-a[0],b[1]-a[1])for a,b in combinations(p,2))for p,c in TERMS}
BREAKS={p:sorted(set(-dx/dy for dx,dy in PAIRS[p]if dy))for p,c in TERMS}

def scaled_spline(poly,r):
    lo=-math.inf;hi=math.inf
    for dx,dy in PAIRS[poly]:
        if not dy:
            if r*abs(dx)>=1:return (),()
        else:
            a,b=sorted(((-1-r*dx)/dy,(1-r*dx)/dy))
            lo=max(lo,a);hi=min(hi,b)
    if lo>=hi:return (),()
    cuts=sorted(set([lo,hi]+[r*t for t in BREAKS[poly]if lo<r*t<hi]))
    slopes=[]
    for a,b in zip(cuts,cuts[1:]):
        z=(a+b)/2
        low=min(poly,key=lambda p:r*p[0]+z*p[1]);high=max(poly,key=lambda p:r*p[0]+z*p[1])
        slopes.append(low[1]-high[1])
    slopes=[0]+slopes+[0]
    knots=[];jumps=[]
    for i,x in enumerate(cuts):
        d=slopes[i+1]-slopes[i]
        if d:knots.append(x);jumps.append(d)
    return knots,jumps

def H(r,x,gamma=.05):
    ans=0.
    for p,c in TERMS:
        zs,As=scaled_spline(p,r);ws,Bs=scaled_spline(p,r*x)
        ans+=c*sum(A*B*abs(x*z-w)**(gamma+2)for z,A in zip(zs,As)for w,B in zip(ws,Bs))
    return ans

def run(n):
    start=time.time();nodes,weights=np.polynomial.legendre.leggauss(n)
    total=0.;minh=(math.inf,None)
    # Split known changes of the polygon width minimum.
    for a,b in zip([0,1/3,.5,2/3],[1/3,.5,2/3,1]):
        for rn,rw in zip(nodes,weights):
            r=(a+b+(b-a)*rn)/2
            xc=sorted(set([1/3,1]+[q/r for q in [1/3,.5,2/3]if 1/3<q/r<1]))
            for xl,xh in zip(xc,xc[1:]):
                for xn,xw in zip(nodes,weights):
                    x=(xl+xh+(xh-xl)*xn)/2;h=H(r,x)
                    if h<minh[0]:minh=(h,(r,x))
                    total+=(b-a)/2*rw*(xh-xl)/2*xw*r**.05*(3*x-1)/x**2*h
    factor=-1/(2*(math.pi**2/6)*.95*1.05*2.05)
    return {'order':n,'I_quarter_minus_mid':factor*total,'unsigned_integral':total,
            'minimum_H_sample':minh,'seconds':time.time()-start,'status':'exploratory_not_certified'}

if __name__=='__main__':
    import sys
    result=run(int(sys.argv[1])if len(sys.argv)>1 else 20)
    Path(__file__).with_name('mellin_exploratory.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
