"""R45 standalone exact source-class / boundary-risk regression (Python stdlib)."""
from bisect import bisect_right
from fractions import Fraction

D=10**24
L=Fraction(262204504569236716045286,D)
U=Fraction(262204504569236716045287,D)

def ff(t,x):return (t*x)%1

def owner(m,t,x,H=None):
    if H is None:H=sorted(ff(z,x) for z in range(m))
    return (bisect_right(H,ff(t,x))-1)%m

def pair_at(m,x):
    a,i,c,j=0,1,1,1
    while i+j<m:
        if x>Fraction(a+c,i+j):a,i=a+c,i+j
        else:c,j=a+c,i+j
    return a,i,c,j

def gap_maxima(m,n,x,H):
    order=sorted(range(n),key=lambda t:ff(t,x));g=[[] for _ in range(m)]
    lengths={}
    for pos,t in enumerate(order):
        z=order[(pos+1)%n]
        expr=(int(t*x//1-z*x//1+(pos==n-1)),z-t)
        lengths[t]=expr;g[owner(m,t,x,H)].append(expr)
    maxima=[max(r,key=lambda e:e[0]+e[1]*x) for r in g]
    return lengths,(1-sum(a for a,b in maxima),-sum(b for a,b in maxima))

def check(m,end,x):
    H=sorted(ff(z,x) for z in range(m))
    a,i,c,j=pair_at(m,x);n0=m;R=(0,0);trans=[]
    for n in range(m,end+1):
        if n==n0:
            stage_start=m if n0==m else n0-1
            tau=[None]*m
            for t in range(stage_start-i,j):tau[owner(m,t,x,H)]=t
            F0=sum(t is None for t in tau)
            startR=R
        F=sum(t is None or t<n-i for t in tau)
        u=(-a,i);v=(c,-j);w=(c-a,i-j)
        d=u if u[0]+u[1]*x<v[0]+v[1]*x else v
        R=(startR[0]+(F-F0)*d[0],startR[1]+(F-F0)*d[1])
        gaps,checkR=gap_maxima(m,n,x,H)
        assert R==checkR,(m,n,R,checkR)
        assert {t for t,g in gaps.items() if g==w}==set(range(n-i,j))
        if n==i+j and n<end:
            large=u if u[0]+u[1]*x>v[0]+v[1]*x else v
            small=v if large==u else u
            if large==u:
                new=(a+c,i+j,c,j);span=range(0,j)
            else:
                new=(a,i,a+c,i+j);span=range(j,i+j)
            assert {t for t,g in gaps.items() if g==large}==set(span)
            Fn=m-len({owner(m,t,x,H) for t in span})
            bridge=(1-m*small[0]-(m-Fn)*(large[0]-small[0]),
                    -m*small[1]-(m-Fn)*(large[1]-small[1]))
            assert bridge==R
            trans.append((n,Fn))
            a,i,c,j=new;n0=n+1
    return R,trans

if __name__=='__main__':
    for theta in (L,(L+U)/2,U):
        r,tr=check(128,389,theta)
        assert r==(-7551,28800)
        assert tr==[(164,67),(225,0)],tr
        print('PASS_R45_FROZEN_STAGE_BRIDGE',r,tr)
    for m,end in ((8,80),(16,120)):
        print('PASS_R45_AUXILIARY',m,check(m,end,(L+U)/2))
