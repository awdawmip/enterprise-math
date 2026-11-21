"""C87: positive two-dimensional integral for the remaining QT contribution.

At fixed u,t, integrate the squared positive part of a concave broken line
exactly. Whole u,t cells are enclosed by the inherited 112-bit interval kernel.
No subtraction of nearly equal source-volume terms is needed.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
import c84_interval_kernel as k

I,Q=k.I,k.Q
ORDERS=tuple(permutations(range(4)))

def positive(x):return I(max(0,x.lo),max(0,x.hi))
def absolute(x):return I(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),
                         max(abs(x.lo),abs(x.hi)))
def maximum(x,y):return I(max(x.lo,y.lo),max(x.hi,y.hi))

def phi_num(a,b,up):
    """Integral_0^1 ((1-z)a+zb)_+^2 dz, for fixed-point integers a,b.

    Return its fixed-point integer with the requested rounding direction.
    """
    if a<=0 and b<=0:return 0
    if a>=0 and b>=0:n,d=a*a+a*b+b*b,3*Q
    else:
        p=max(a,b);n,d=p**3,3*abs(a-b)*Q
    return -((-n)//d) if up else n//d

def phi(a,b):return I(phi_num(a.lo,b.lo,False),phi_num(a.hi,b.hi,True))

def knots_and_values(u,t,r):
    d=1/u;one=1-t
    knots=(-u,u,3*u-2*d/one,2*d/t-3*u)
    values=(
        r-2*u-positive(d-2*u*one)-positive(d-u*t),
        r-2*u-positive(d-u*one)-positive(d-2*u*t),
        r-F(3,2)*u-positive(d/one-3*u*t)
          -maximum(u,absolute(knots[2]))/2,
        r-F(3,2)*u-positive(d/t-3*u*one)
          -maximum(u,absolute(knots[3]))/2)
    return knots,values

def source_volume_cell(u,t,r):
    """Enclose C(u,t) on a complete rectangular parameter cell."""
    knots,values=knots_and_values(u,t,r)
    if max(v.hi for v in values)<=0:return I.rat(0)
    # Any real order of the four knots is included. Orders excluded here
    # have an interval-separated inversion and are genuinely impossible.
    lower=None;upper=None
    for order in ORDERS:
        if any(knots[order[i]].lo>knots[order[j]].hi
               for i in range(4)for j in range(i+1,4)):continue
        left,right=values[order[0]],values[order[-1]]
        total=positive(left)**3/(3*((1+t)/2))
        total+=positive(right)**3/(3*((2-t)/2))
        for i,j in zip(order,order[1:]):
            width=positive(knots[j]-knots[i])
            total+=width*phi(values[i],values[j])
        total=total/4
        lower=total.lo if lower is None else min(lower,total.lo)
        upper=total.hi if upper is None else max(upper,total.hi)
    assert lower is not None
    return I(max(0,lower),upper)

@lru_cache(None)
def doubled_centered(a,mesh=64):
    """Whole-cell enclosure of QT(A), for 8/3<=A<4."""
    a=F(a);assert F(8,3)<=a<4 and mesh>0
    if a==F(8,3):return I.rat(0)
    r=(2*I.cv(a)).sqrt()
    bottom,top=2/r,r/2
    tmin=min(F(1,3),4/a-1)
    du=(top-bottom)/mesh;dt=I.cv((F(1,2)-tmin)/mesh)
    ans=I.rat(0);active=0
    for i in range(mesh):
        ul=bottom+(top-bottom)*F(i,mesh)
        uh=bottom+(top-bottom)*F(i+1,mesh)
        u=I(ul.lo,uh.hi)
        for j in range(mesh):
            tl=I.cv(tmin+(F(1,2)-tmin)*F(j,mesh))
            th=I.cv(tmin+(F(1,2)-tmin)*F(j+1,mesh))
            t=I(tl.lo,th.hi)
            value=source_volume_cell(u,t,r)
            ans+=value*du*dt
            active+=value.hi>0
    return ans*6/k.ZETA

def source_volume_float(u,t,r):
    """Exploratory evaluation of the same positive broken-line formula."""
    d=1/u
    knots=sorted([-u,u,3*u-2*d/(1-t),2*d/t-3*u])
    def value(h):
        return (r-1.5*u-max(0,d+(1-t)*(h-3*u)/2)
                -max(0,d-t*(h+3*u)/2)-.5*max(u,abs(h)))
    vals=[value(h)for h in knots]
    def ph(a,b):
        if max(a,b)<=0:return 0.
        if min(a,b)>=0:return(a*a+a*b+b*b)/3
        return max(a,b)**3/(3*abs(a-b))
    ans=max(0,vals[0])**3/(3*(1+t)/2)
    ans+=max(0,vals[-1])**3/(3*(2-t)/2)
    ans+=sum((b-a)*ph(x,y)for a,b,x,y in zip(knots,knots[1:],vals,vals[1:]))
    return ans/4

if __name__=='__main__':
    import time
    for a in [F(11,4),F(3),F(7,2),F(255,64)]:
        start=time.time();out=doubled_centered(a,32)
        print(str(a),out.json(),'seconds',time.time()-start,flush=True)
