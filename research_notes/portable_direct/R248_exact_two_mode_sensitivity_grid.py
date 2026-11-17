#!/usr/bin/env python3
"""R248: exact parameter derivative certificate on the 21-point R247 grid.
Only rational integer arithmetic; input family is R247 and frozen science@43ec6098.
"""
from fractions import Fraction as F
from math import lcm
import json,sys,hashlib
sys.set_int_max_str_digits(1000000)
W=(144,576,1440,4320,17280,86400,518400)

class I:
    __slots__=('l','u')
    def __init__(self,l,u=None):
        self.l=F(l);self.u=F(l if u is None else u)
        assert self.l<=self.u
    def __add__(self,other):
        b=as_i(other);return I(self.l+b.l,self.u+b.u)
    __radd__=__add__
    def __neg__(self):return I(-self.u,-self.l)
    def __sub__(self,other):return self+-as_i(other)
    def __rsub__(self,other):return as_i(other)+-self
    def __mul__(self,other):
        b=as_i(other);p=[self.l*b.l,self.l*b.u,self.u*b.l,self.u*b.u]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,other):
        b=as_i(other);assert not(b.l<=0<=b.u)
        return self*I(1/b.u,1/b.l)
    def __rtruediv__(self,other):return as_i(other)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0 and self.l<0<self.u:return I(0,max(self.l**n,self.u**n))
        return I(min(self.l**n,self.u**n),max(self.l**n,self.u**n))
    def __repr__(self):return f'I({float(self.l):.12g},{float(self.u):.12g})'

def as_i(x):return x if isinstance(x,I) else I(x)
def ids(mask):return [0]+[i for i in range(1,7) if mask & (1<<(i-1))]

def params(s):
    s=F(s); den=2615*s-3539
    t=(1691*s-2615)/den;td=F(853776)/den**2
    a=(F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t)
    ad=(F(0),F(0),F(0),F(0),F(1),F(0),td)
    b=(F(13,60),)+tuple(F(5,18)*abs(F(1,2)-x) for x in a[1:])
    bd=(F(0),)+tuple(F(5,18)*(-dx if x<F(1,2) else dx) for x,dx in zip(a[1:],ad[1:]))
    pi=tuple(y/(1-x) for x,y in zip(a,b))
    pid=tuple((dy*(1-x)+y*dx)/(1-x)**2 for x,dx,y,dy in zip(a,ad,b,bd))
    Z=sum((y/(1-x)**2 for x,y in zip(a,b)),F(0))
    Zd=sum((dy/(1-x)**2+2*y*dx/(1-x)**3 for x,dx,y,dy in zip(a,ad,b,bd)),F(0))
    rho=tuple(y/(1-x)**2/Z for x,y in zip(a,b))
    rhod=tuple((dy/(1-x)**2+2*y*dx/(1-x)**3)/Z-r*Zd/Z for x,dx,y,dy,r in zip(a,ad,b,bd,rho))
    assert sum(pi)==1 and sum(pid)==0 and sum(rho)==1 and sum(rhod)==0
    return a,ad,b,bd,pi,pid,Z,Zd,rho,rhod

def exact_observer_and_derivative(s, nvals):
    a,ad,b,bd,pi,pid,Z,Zd,rho,rhod=params(s)
    C=lcm(*[v.denominator for v in (*a,*ad)])
    Q=lcm(*[v.denominator for v in (*pi,*pid)])
    d=C*Q
    h=[int(d*x) for x in a];hd=[int(d*x) for x in ad]
    u=[int(C*(1-x)) for x in a];ud=[int(-C*x) for x in ad]
    v=[int(Q*x) for x in pi];vd=[int(Q*x) for x in pid]
    R=lcm(*[x.denominator for x in (*rho,*rhod)])
    rn=[int(x*R) for x in rho];rdn=[int(x*R) for x in rhod]
    totals={n:[0,0] for n in nvals}; ks={n-1:n for n in nvals}
    for mask in range(63):
        ix=ids(mask);z=[1]*len(ix);zd=[0]*len(ix)
        weight=W[mask.bit_count()]
        for k in range(max(ks)+1):
            if k in ks:
                pair=totals[ks[k]]
                pair[0]+=weight*sum(rn[i]*z[j] for j,i in enumerate(ix))
                pair[1]+=weight*sum(rn[i]*zd[j]+rdn[i]*z[j] for j,i in enumerate(ix))
            if k==max(ks):break
            dot=sum(v[i]*z[j] for j,i in enumerate(ix))
            dotd=sum(v[i]*zd[j]+vd[i]*z[j] for j,i in enumerate(ix))
            zd=[h[i]*zd[j]+hd[i]*z[j]+u[i]*dotd+ud[i]*dot for j,i in enumerate(ix)]
            z=[h[i]*z[j]+u[i]*dot for j,i in enumerate(ix)]
    return {n:(F(vals[0],R*d**(n-1)),F(vals[1],R*d**(n-1))) for n,vals in totals.items()}

def root_interval(a,b,mask,steps=100):
    ix=ids(mask)
    def f(x):return sum((b[i]/(x-a[i]) for i in ix),F(0))-1
    l=max(a[i] for i in ix);u=F(1)
    assert f(u)<0
    for _ in range(steps):
        m=(l+u)/2
        if f(m)>0:l=m
        else:u=m
    assert f(l)>0>f(u)
    return I(l,u)

def mode_and_derivative(par,mask,k):
    a,ad,b,bd,pi,pid,Z,Zd,rho,rhod=par
    x=root_interval(a,b,mask)
    ix=ids(mask)
    T=lambda seq:sum(seq,I(0))
    D=[x-a[i] for i in ix]
    Q=T([b[i]/h**2 for i,h in zip(ix,D)])
    xp=T([bd[i]/h+b[i]*ad[i]/h**2 for i,h in zip(ix,D)])/Q
    S=T([b[i]/((1-a[i])*h) for i,h in zip(ix,D)])
    Sd=T([bd[i]/((1-a[i])*h)+b[i]*ad[i]/((1-a[i])**2*h)+b[i]*(ad[i]-xp)/((1-a[i])*h**2) for i,h in zip(ix,D)])
    Qd=T([bd[i]/h**2+2*b[i]*(ad[i]-xp)/h**3 for i,h in zip(ix,D)])
    A=W[mask.bit_count()]*S**2/(Z*Q)
    Ap=A*(2*Sd/S-Zd/Z-Qd/Q)
    X=A*x**k
    Xp=Ap*x**k+k*A*x**(k-1)*xp
    return X,Xp,x,xp,A

def short_margin(x):
    assert x>0
    return {'lower_bound_log10':len(str(x.numerator))-len(str(x.denominator))-1,
            'numerator_bits':x.numerator.bit_length(),'denominator_bits':x.denominator.bit_length(),
            'sha256':hashlib.sha256((str(x.numerator)+'/'+str(x.denominator)).encode()).hexdigest()}

def run(grid,ns):
    results=[]
    for s in grid:
        par=params(s)
        ph=exact_observer_and_derivative(s,ns)
        row={'s':str(s),'n':{}}
        for n in ns:
            X0,XP0,*_=mode_and_derivative(par,59,n-1)
            X1,XP1,*_=mode_and_derivative(par,55,n-1)
            X=X0+X1;XP=XP0+XP1
            phi,phip=ph[n]
            deriv_numerator=I(phip)*X-I(phi)*XP
            floor=F(63,1000) if n==270 else F(1,100)
            floor_margin=deriv_numerator.l-floor*X.u**2
            assert floor_margin>0,(s,n,'derivative lower bound failed')
            row['n'][str(n)]={'positive':deriv_numerator.l>0,
                'lower_margin':short_margin(deriv_numerator.l) if deriv_numerator.l>0 else str(float(deriv_numerator.l)),
                'certified_derivative_floor':str(floor),
                'floor_margin':short_margin(floor_margin),
                'approx_dE_ds':float(deriv_numerator.l/(X.u**2)),
                'approx_E':float(phi/X.l-1)}
            assert deriv_numerator.l>0,(s,n,deriv_numerator)
        results.append(row)
    return results

if __name__=='__main__':
    import time
    start=time.time();grid=[F(j,1000) for j in range(390,411)]
    data=run(grid,[270,403]);data={'schema':'EM_R248_TWO_MODE_GRID_SENSITIVITY_V1','source_commit':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','cases':data,'all_pass':True}
    open('R248_verification.json','w').write(json.dumps(data,indent=2))
    print('PASS',len(data['cases']),'elapsed',round(time.time()-start,3))
    for row in data['cases']:
        print(row['s'],*[row['n'][str(n)]['approx_dE_ds'] for n in (270,403)])
