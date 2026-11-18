"""Finite K=1 trajectory and signed stability on all solenoidal modes. Python 3.9+, SymPy."""
from fractions import Fraction as F
from itertools import product
from math import isqrt, lcm
import json
import sympy as sp
ZERO=(F(0),)*3
def kv(k,v):return tuple(k*x for x in v)
def tot(*fields):
 o={}
 for field,scale in fields:
  for k,v in field.items():
   old=o.get(k,ZERO);o[k]=tuple(x+scale*y for x,y in zip(old,v))
 return {k:v for k,v in o.items() if any(v)}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def Q(a,b):
 out={}
 for p,u in a.items():
  for q,v in b.items():
   k=tuple(x+y for x,y in zip(p,q));m=dot(k,k)
   if not m or max(map(abs,k))>1:continue
   t=dot(u,q)
   if not t:continue
   old=out.get(k,ZERO);out[k]=tuple(x+t*y for x,y in zip(old,v))
 ret={}
 for k,w in out.items():
  d=F(dot(k,w),dot(k,k));res=tuple(x-d*j for x,j in zip(w,k))
  if any(res):ret[k]=res
 return ret
def visc(a,nu):return {k:kv(-nu*dot(k,k),v) for k,v in a.items()}
def norm2(a):return sum(dot(v,v) for v in a.values())
def cyclic():
 f={}
 for j in range(3):
  for h in (-1,1):
   k=[0]*3;k[j]=h
   a=[0]*3;a[(j+1)%3]=-F(h,2)
   f[tuple(k)]=tuple(a)
 return f

NU=F(1,2)
T=F(1,8)
X=cyclic()
Y=Q(X,X)
ks=sorted([k for k in product([-1,0,1],repeat=3) if any(k)],key=lambda k:sum(k)%2)


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def make_blocks():
    gram=[]
    radii=[]
    bases=[]
    for k in ks:
        idx=min(range(3),key=lambda j:abs(k[j]))
        unit=tuple(int(i==idx) for i in range(3))
        v=cross(k,unit)
        bases.append([v,cross(k,v)])
        for w in bases[-1]:
            gram.append(dot(w,w))
            radii.append(dot(k,k))
    def strain(f):
        H=sp.zeros(52)
        for i,k in enumerate(ks):
            for j,l in enumerate(ks):
                p=tuple(a-b for a,b in zip(k,l))
                if p not in f:continue
                for s,u in enumerate(bases[i]):
                    for t,v in enumerate(bases[j]):
                        H[2*i+s,2*j+t]=F(dot(u,f[p])*dot(p,v)+dot(u,p)*dot(f[p],v),2)
        assert H==H.T
        return H
    return sp.diag(*gram),sp.diag(*radii),strain(X),strain(Y),bases


def positive_test(matrix):
    # Fraction-free symmetric elimination; positive pivots certify positive definiteness.
    factor=lcm(*(int(sp.denom(x)) for x in matrix))
    a=[[int(x*factor) for x in row] for row in matrix.tolist()]
    n=len(a)
    prev=1
    nnz=sum(bool(x) for row in a for x in row)
    for j in range(n):
        pivot=a[j][j]
        if pivot<=0:return False,j+1,nnz
        for h in range(j+1,n):
            for k in range(h,n):
                val=a[h][k]*pivot-a[h][j]*a[j][k]
                assert val%prev==0
                a[h][k]=a[k][h]=val//prev
        prev=pivot
    return True,n,nnz


def spectral():
    G,D,H,J,bases=make_blocks()
    C=H[:24,24:]
    ge=G[:24,:24];go=G[24:,24:]
    assert H[:24,:24].is_zero_matrix and H[24:,24:].is_zero_matrix
    x=sp.symbols('x')
    candidates=[(4*x-1,3),(8*x-1,6),(768*x*x-128*x+1,3),
                (3072*x**3-1024*x*x+72*x-1,3)]
    pol=sp.Poly((ge.inv()*C*go.inv()*C.T).charpoly(x).as_expr(),x)
    expected=sp.Poly(sp.prod(f**k for f,k in candidates),x).monic()
    assert pol==expected
    assert all(all(c>0 for c in sp.Poly(f.subs(x,x+sp.Rational(1,4)),x).all_coeffs())
               for f,k in candidates[2:])
    # Odd vector y=(cos y,cos z,cos x), doubled coefficients; spatial mass cancels.
    coeff=[]
    for i,k in enumerate(ks[12:],12):
        z=[0,0,0]
        if dot(k,k)==1:
            axis=next(j for j in range(3) if k[j])
            z[(axis-1)%3]=1
        for w in bases[i]:coeff.append(F(dot(w,z),dot(w,w)))
    v=sp.Matrix(coeff)
    assert (C*v).dot(ge.inv()*C*v)*4==v.dot(go*v)
    assert D[24:,24:]*v==v
    endpoints={}
    for name,da,db in [('support_trim',-NU,0),('full',-NU,1),('rounded',-F(3,5),F(6,5))]:
        signed=(1+T*da)*H+T*db*J-NU*G*D
        upper=-F(1,6)
        ok,piv,nnz=positive_test(upper*G-signed)
        assert ok
        endpoints[name]={"upper_log_norm":str(upper),"positive_pivots":piv,"matrix_nonzeros":nnz}
    return {"real_dimension":52,"parity_dimensions":[24,28],
            "strain_offdiagonal_nonzeros":sum(1 for val in H if val),
            "squared_singular_polynomial_factors":[[str(f),k] for f,k in candidates],
            "uniform_viscous_threshold_for_X_squared":"1/8","endpoint_LDL":endpoints}


def root(x):
    x=F(x)
    scale=10**13
    base=isqrt((x.numerator*scale*scale)//x.denominator)
    return F(base,scale), F(base+1,scale) if base**2*x.denominator!=x.numerator*scale**2 else F(base,scale)


def format_bounds(lo,hi,digits=9):
    scale=10**digits
    return [str(F((lo*scale)//1,scale)),str(F(-((-hi*scale)//1),scale))]


def orbit():
    assert norm2(X)==F(3,2) and norm2(Y)==F(3,4)
    assert not tot((Q(X,Y),1),(Q(Y,X),1),(X,F(1,2)))
    assert not Q(Y,Y)
    a,b=[F(1)],[F(0)]
    for j in range(20):
        a.append((-NU*a[j]-sum(a[i]*b[j-i] for i in range(j+1))/2)/(j+1))
        b.append((-2*NU*b[j]+sum(a[i]*a[j-i] for i in range(j+1)))/(j+1))
    z=2*T;J=len(a)-1
    tail=z**(J+1)/(1-z)
    # Bound the derivative tails after division by t for t>0, using |a_j|,|b_j|<=2^j.
    deriv_tail=(z**(J+1)/T**2)*((J+1)/(1-z)+z/(1-z)**2)
    assert 2*a[2]+sum(j*abs(a[j])*T**(j-2) for j in range(3,J+1))+deriv_tail<0
    assert 2*b[2]+sum(j*abs(b[j])*T**(j-2) for j in range(3,J+1))+deriv_tail<0
    assert b[1]-sum(j*abs(b[j])*T**(j-1) for j in range(2,J+1))-T*deriv_tail>0
    assert F(3,5)+a[1]-sum(j*abs(a[j])*T**(j-1) for j in range(2,J+1))-T*deriv_tail>0
    return a,b,tail


def evaluate(a,b,tail,da,db):
    # Error against the exact orbit at final time, independently of the strain proof.
    ap=sum(y*T**j for j,y in enumerate(a))-(1+da*T)
    bp=sum(y*T**j for j,y in enumerate(b))-db*T
    e2=F(3,2)*ap*ap+F(3,4)*bp*bp
    lo,hi=root(e2)
    return lo-F(3,2)*tail,hi+F(3,2)*tail


def kernel_integral(j):
    # Integral_0^T exp(-(T-s)/6) s^j ds with alternating rational remainder.
    c=F(1,6)
    term=T**(j+1)/(j+1)
    acc=term
    for k in range(1,9):
        term*=(-c*T)/(j+k+1)
        acc+=term
    return acc+term*(-c*T)/(j+10),acc


def certify(name,ideal,stored,truth):
    ideal_s=tot((X,ideal[0]),(Y,ideal[1]))
    s=tot((X,stored[0]),(Y,stored[1]))
    full=tot((visc(X,NU),1),(Y,1))
    budget=[tot((ideal_s,1),(full,-1)),tot((s,1),(ideal_s,-1)),
            tot((visc(s,NU),-1),(Q(X,s),-1),(Q(s,X),-1)),tot((Q(s,s),-1))]
    degrees=[0,0,1,2]
    lo=hi=F(0)
    for f,j in zip(budget,degrees):
        low,high=root(norm2(f))
        s0,s1=kernel_integral(j)
        lo+=low*s0;hi+=high*s1
    a,b,tail=truth
    actual=evaluate(a,b,tail,*stored)
    result={"slope_coordinates":[str(t) for t in stored],
            "squared_defect_norms_support_round_time1_time2":[str(norm2(x)) for x in budget],
            "uniform_bound_value_interval":format_bounds(lo,hi),
            "actual_endpoint_error_interval":format_bounds(*actual),
            "endpoint_slack_interval":format_bounds(lo-actual[1],hi-actual[0])}
    if name=='full':
        assert hi<F(14,1000) and lo>F(135,10000)>actual[1]
        A=norm2(budget[2]);B=norm2(budget[3])
        C=sum(dot(w,budget[3].get(k,ZERO)) for k,w in budget[2].items())
        assert C==-F(15,32) and A+3*C*T>0
        u,v=root(A)
        k1,k2,k3=(kernel_integral(j) for j in (1,2,3))
        coherent_lo=u*k1[0]+C*k2[1]/u
        coherent_hi=v*k1[1]+C*k2[0]/v+B*k3[1]/(2*u)
        assert actual[1]<F(132,10000)<coherent_lo<coherent_hi<F(135,10000)<lo
        result.update({"signed_defect_inner_product":str(C),
            "coherent_scalar_propagation_interval":format_bounds(coherent_lo,coherent_hi)})
    if name=='support_trim':
        assert actual[0]>F(9,100)
    return result


def main():
    truth=orbit()
    cases={name:certify(name,ideal,stored,truth) for name,ideal,stored in [
        ('support_trim',(-NU,0),(-NU,0)),('full',(-NU,1),(-NU,1)),
        ('rounded',(-NU,1),(-F(3,5),F(6,5)))]}
    # Rounding the actual nonzero Fourier slopes to one decimal, half away from zero.
    full=tot((X,-NU),(Y,1));rnd=tot((X,-F(3,5)),(Y,F(6,5)))
    def round10(x):
        return (1 if x>=0 else -1)*F((10*abs(x)+F(1,2))//1,10)
    assert {k:tuple(round10(z)for z in w)for k,w in full.items()}==rnd
    print(json.dumps({"cube_cutoff":1,"nu":str(NU),"T":str(T),"spectral":spectral(),
        "orbit_X_Y_norms_squared":["3/2","3/4"],"proof_Taylor_order":len(truth[0])-1,
        "Taylor_component_remainder_at_T":str(truth[2]),"cases":cases},indent=2))


if __name__=='__main__':
    main()
