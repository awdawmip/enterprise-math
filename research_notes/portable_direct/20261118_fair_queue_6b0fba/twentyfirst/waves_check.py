"""Exact algebraic triads, Fourier jets of the full four-wave reference, and tail costs."""
import json
from fractions import Fraction as F
from math import comb, factorial
import sympy as s

P=(2,-2,0); Q=(1,1,0); R=(1,0,1); T=(0,1,1)


def add(x,y):
    return tuple(a+b for a,b in zip(x,y))


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def neg(x):
    return tuple(-a for a in x)


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])


def exact_triads():
    def helical(k):
        v=s.Matrix(k); e=s.eye(3)[:,k.index(0)]
        h=(e+s.I*v.cross(e)/s.sqrt(v.dot(v)))/s.sqrt(2)
        assert (s.I*v.cross(h)-s.sqrt(v.dot(v))*h).applyfunc(s.simplify)==s.zeros(3,1)
        return h
    def projected(p,u,q,h):
        k=s.Matrix(add(p,q)); w=s.Matrix(q).dot(u)*h+s.Matrix(p).dot(h)*u
        return (w-k*(k.dot(w)/k.dot(k))).applyfunc(s.simplify)
    hp,hq,hr=map(helical,(P,Q,R))
    first=projected(P,hp,Q,hq)
    reverse=projected(R,hr,Q,hq)
    w=projected(R,hr,add(P,Q),first)
    assert reverse==s.zeros(3,1)
    k=s.Matrix(add(add(P,Q),R))
    energies=[]
    for sign in (1,-1):
        z=(w+sign*s.I*k.cross(w)/s.sqrt(k.dot(k)))/2
        energies.append(s.simplify(z.dot(z.conjugate())))
    assert energies==[s.Rational(1331,900),s.Rational(59,900)]
    # Find all admissible ordered origins at the common output before grouping.
    modes=[P,Q,R,T,neg(P),neg(Q),neg(R),neg(T)]
    paths=[[src,x,y] for src in (Q,neg(Q)) for x in modes for y in modes
           if add(add(src,x),y)==tuple(k)]
    assert len(paths)==2
    return dict(common_k=list(map(int,k)),paths=paths,p_then_r_entries=list(map(str,w)),
                r_then_p_entries=list(map(str,reverse)),helicity_energies=list(map(str,energies)))


def full_jets(count=8):
    # Exact reduction of Z[i,sqrt(2),denominators] at a split prime.  All input
    # signs and eight reference labels remain independent until common output k.
    prime=65537
    iunit=next(x for x in range(1,prime) if x*x%prime==prime-1)
    rt2=next(x for x in range(1,prime) if x*x%prime==2)
    inv=lambda n:pow(n%prime,-1,prime)
    def hel(k):
        e=tuple(int(j==k.index(0)) for j in range(3))
        length=(2*rt2 if dot(k,k)==8 else rt2)
        return tuple((x+iunit*y*inv(length))*inv(rt2)%prime for x,y in zip(e,cross(k,e)))
    modes={k:hel(k) for pos in (P,Q,R,T) for k in (pos,neg(pos))}
    zer=(0,0,0)
    def put(row,k,v):
        row[k]=tuple((x+y)%prime for x,y in zip(row.get(k,zer),v))
    def step(source,picks):
        out={}
        for q,h in source.items():
            for p in picks:
                k=add(p,q)
                if k==zer: continue
                u=modes[p]
                a=dot(u,q); b=dot(h,p)
                raw=tuple((a*x+b*y)%prime for x,y in zip(h,u))
                scale=dot(k,raw)*inv(dot(k,k))
                put(out,k,tuple(-iunit*(x-scale*y) for x,y in zip(raw,k)))
        return {k:v for k,v in out.items() if v!=zer}
    deriv=[{Q:modes[Q],neg(Q):modes[neg(Q)]}]
    pulls=[]; certificates=[]
    ratio=F(1)
    for n in range(count+1):
        k=tuple(x+n*y for x,y in zip(Q,P))
        assert all(k not in earlier for earlier in deriv[:n])
        scalar=2*iunit*(-1)**n*ratio.numerator*inv(ratio.denominator)%prime
        assert dot(P,deriv[n][k])%prime==scalar!=0
        certificates.append(dict(n=n,k=k,fraction=str(ratio),p_component_mod_prime=scalar,
                                 full_jet_nonzero_modes=len(deriv[n])))
        if n==count: break
        pulls.append([step(deriv[n],[P,neg(P)]),step(deriv[n],[Q,neg(Q),R,neg(R),T,neg(T)])])
        out={k:tuple(-dot(k,k)*x%prime for x in h) for k,h in deriv[n].items()}
        for j in range(n+1):
            for row,rate in zip(pulls[j],(8,2)):
                factor=comb(n,j)*pow(-rate,n-j,prime)
                for k,h in row.items(): put(out,k,tuple(factor*x for x in h))
        deriv.append({k:v for k,v in out.items() if v!=zer})
        ratio*=F(4*n*n-3,1+4*(n+1)**2)
    return dict(prime=prime,i=iunit,sqrt2=rt2,jets=certificates)


def kernels_and_bound():
    # Laplace transform by a separate cascade in s shifted by each reference heat rate.
    for n in range(1,16):
        for original in (F(1),F(7,5)):
            for nu in (F(1),F(3,4)):
                val=F(1)
                lap=original
                for j in range(n,-1,-1):
                    val/=lap+nu*(2+8*j*j)
                    lap+=8*nu
                closed=1/(original+nu*(2+8*n))**2
                for j in range(2,n+1): closed/=original+nu*(2+8*n+8*j*(j-1))
                assert val==closed
    m=8
    amp=2*(m+1)*F(3,10)**(m-1)/factorial(m)
    level=(6*(m+1)+1)**3*(3*(m+1)+F(81,8)*(m+1)**3)*amp**2
    rat=F(m+2,m+1)**8*(F(3,10)/(m+1))**2
    assert level/(1-rat)<F(344,100000)**2
    return dict(laplace_checks=60,m=m,weighted_coefficient_upper=str(amp),
                squared_X_tail_upper=str(level/(1-rat)),ratio_upper=str(rat))


if __name__=='__main__':
    data=dict(triads=exact_triads(),native_jets=full_jets(),tail=kernels_and_bound())
    print(json.dumps(data,indent=2,sort_keys=True,default=str))
